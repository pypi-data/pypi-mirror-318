import sys
import networkx as nx
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QSlider, QMenuBar, QMenu, QDialog, 
                            QFormLayout, QLineEdit, QPushButton, QFileDialog,
                            QLabel, QComboBox, QMessageBox, QTableView, QInputDialog,
                            QMenu, QTabWidget)
from PyQt6.QtCore import (QPoint, Qt, QAbstractTableModel, QTimer)
import numpy as np
import time
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from qtrangeslider import QRangeSlider
from nettracer3d import nettracer as n3d
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd
from PyQt6.QtGui import (QFont, QCursor)
import tifffile

class ImageViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NetTracer3D")
        self.setGeometry(100, 100, 1400, 800)
        
        # Initialize channel data and states
        self.channel_data = [None] * 4
        self.channel_visible = [False] * 4
        self.current_slice = 0
        self.active_channel = 0  # Initialize active channel
        
        # Initialize selection state
        self.selecting = False
        self.selection_start = None
        self.selection_rect = None
        self.click_start_time = None  # Add this to track when click started
        self.selection_threshold = 1.0  # Time in seconds before starting rectangle selection
        
        # Initialize zoom mode state
        self.zoom_mode = False
        self.original_xlim = None
        self.original_ylim = None

        # Pan mode state
        self.pan_mode = False
        self.panning = False
        self.pan_start = None
        
        # Store brightness/contrast values for each channel
        self.channel_brightness = [{
            'min': 0,
            'max': 1
        } for _ in range(4)]
        
        # Create the brightness dialog but don't show it yet
        self.brightness_dialog = BrightnessContrastDialog(self)
        
        
        # Create control panel
        control_panel = QWidget()
        control_layout = QHBoxLayout(control_panel)
        
        # Create active channel selector
        active_channel_widget = QWidget()
        active_channel_layout = QHBoxLayout(active_channel_widget)
        
        active_label = QLabel("Active Image:")
        active_channel_layout.addWidget(active_label)
        
        self.active_channel_combo = QComboBox()
        self.active_channel_combo.addItems(["Nodes", "Edges", "Network Overlay", "Label Overlay"])
        self.active_channel_combo.setCurrentIndex(0)
        self.active_channel_combo.currentIndexChanged.connect(self.set_active_channel)
        # Initially disable the combo box
        self.active_channel_combo.setEnabled(False)
        active_channel_layout.addWidget(self.active_channel_combo)
        
        control_layout.addWidget(active_channel_widget)

        # Create zoom button and pan button
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)

        # Create zoom button
        self.zoom_button = QPushButton("🔍")
        self.zoom_button.setCheckable(True)
        self.zoom_button.setFixedSize(40, 40)
        self.zoom_button.clicked.connect(self.toggle_zoom_mode)
        control_layout.addWidget(self.zoom_button)

        self.pan_button = QPushButton("✋")
        self.pan_button.setCheckable(True)
        self.pan_button.setFixedSize(40, 40)
        self.pan_button.clicked.connect(self.toggle_pan_mode)
        buttons_layout.addWidget(self.pan_button)

        control_layout.addWidget(buttons_widget)
                
        # Create channel buttons
        self.channel_buttons = []
        self.delete_buttons = []  # New list to store delete buttons
        self.channel_names = ["Nodes", "Edges", "Network Overlay", "Label Overlay"]

        # Create channel toggles with delete buttons
        for i in range(4):
            # Create container for each channel's controls
            channel_container = QWidget()
            channel_layout = QHBoxLayout(channel_container)
            channel_layout.setSpacing(2)  # Reduce spacing between buttons
            
            # Create toggle button
            btn = QPushButton(f"{self.channel_names[i]}")
            btn.setCheckable(True)
            btn.setEnabled(False)
            btn.clicked.connect(lambda checked, ch=i: self.toggle_channel(ch))
            self.channel_buttons.append(btn)
            channel_layout.addWidget(btn)
            
            # Create delete button
            delete_btn = QPushButton("×")  # Using × character for delete
            delete_btn.setFixedSize(20, 20)  # Make it small and square
            delete_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    color: gray;
                    font-weight: bold;
                }
                QPushButton:hover {
                    color: red;
                }
                QPushButton:disabled {
                    color: lightgray;
                }
            """)
            delete_btn.setEnabled(False)
            delete_btn.clicked.connect(lambda checked, ch=i: self.delete_channel(ch))
            self.delete_buttons.append(delete_btn)
            channel_layout.addWidget(delete_btn)
            
            control_layout.addWidget(channel_container)

        # Create the main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        
        # Create left panel for image and controls
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # Create matplotlib canvas for image display
        self.figure = Figure(figsize=(8, 8))
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        left_layout.addWidget(self.canvas)

        
        left_layout.addWidget(control_panel)

        # Add timer for debouncing slice updates
        self._slice_update_timer = QTimer()
        self._slice_update_timer.setSingleShot(True)  # Only fire once after last trigger
        self._slice_update_timer.timeout.connect(self._do_slice_update)
        self.pending_slice = None  # Store the latest requested slice
        
        # Create container for slider and arrow buttons
        slider_container = QWidget()
        slider_layout = QHBoxLayout(slider_container)
        slider_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add left arrow button
        self.left_arrow = QPushButton("←")
        self.left_arrow.setFixedSize(30, 30)
        self.left_arrow.pressed.connect(self.start_left_scroll)
        self.left_arrow.released.connect(self.stop_continuous_scroll)
        slider_layout.addWidget(self.left_arrow)
        
        # Add slider for depth navigation
        self.slice_slider = QSlider(Qt.Orientation.Horizontal)
        self.slice_slider.setEnabled(False)
        self.slice_slider.valueChanged.connect(self.update_slice)
        slider_layout.addWidget(self.slice_slider)
        
        # Add right arrow button
        self.right_arrow = QPushButton("→")
        self.right_arrow.setFixedSize(30, 30)
        self.right_arrow.pressed.connect(self.start_right_scroll)
        self.right_arrow.released.connect(self.stop_continuous_scroll)
        slider_layout.addWidget(self.right_arrow)
        
        # Initialize continuous scroll timer
        self.continuous_scroll_timer = QTimer()
        self.continuous_scroll_timer.timeout.connect(self.continuous_scroll)
        self.scroll_direction = 0  # 0: none, -1: left, 1: right
        
        left_layout.addWidget(slider_container)

        
        main_layout.addWidget(left_panel)
        
        # Create right panel
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Create tabbed data widget for top right
        self.tabbed_data = TabbedDataWidget(self)
        right_layout.addWidget(self.tabbed_data)
        # Initialize data_table property to None - it will be set when tabs are added
        self.data_table = None
        
        # Create table control panel
        table_control = QWidget()
        table_control_layout = QHBoxLayout(table_control)
        
        # Create toggle buttons for tables
        self.network_button = QPushButton("Network")
        self.network_button.setCheckable(True)
        self.network_button.setChecked(True)
        self.network_button.clicked.connect(self.show_network_table)
        
        self.selection_button = QPushButton("Selection")
        self.selection_button.setCheckable(True)
        self.selection_button.clicked.connect(self.show_selection_table)
        
        # Add buttons to control layout
        table_control_layout.addWidget(self.network_button)
        table_control_layout.addWidget(self.selection_button)
        
        # Add control panel to right layout
        right_layout.addWidget(table_control)
        
        # Create both table views
        self.network_table = CustomTableView(self)
        self.selection_table = CustomTableView(self)
        empty_df = pd.DataFrame(columns=['Node 1A', 'Node 1B', 'Edge 1C'])
        self.selection_table.setModel(PandasModel(empty_df))
        self.network_table.setAlternatingRowColors(True)
        self.selection_table.setAlternatingRowColors(True)
        self.network_table.setSortingEnabled(True)
        self.selection_table.setSortingEnabled(True)
        
        # Initially show network table and hide selection table
        right_layout.addWidget(self.network_table)
        right_layout.addWidget(self.selection_table)
        self.selection_table.hide()
        
        # Store reference to currently active table
        self.active_table = self.network_table
        
        main_layout.addWidget(right_panel)
        
        # Create menu bar
        self.create_menu_bar()

        # Initialize clicked values dictionary
        self.clicked_values = {
            'nodes': [],
            'edges': []
        }
        
        # Connect mouse events
        self.canvas.mpl_connect('button_press_event', self.on_mouse_press)
        self.canvas.mpl_connect('button_release_event', self.on_mouse_release)
        self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        #self.canvas.mpl_connect('button_press_event', self.on_mouse_click)

        # Initialize measurement points tracking
        self.measurement_points = []  # List to store point pairs
        self.current_point = None  # Store first point of current pair
        self.current_pair_index = 0  # Track pair numbering
        


        # Add these new methods for handling neighbors and components (FOR RIGHT CLICKIGN)
        self.show_neighbors_clicked = None
        self.show_component_clicked = None

        # Initialize highlight overlay
        self.highlight_overlay = None
        self.highlight_bounds = None  # Store bounds for positioning

    def start_left_scroll(self):
        """Start scrolling left when left arrow is pressed."""
        # Single increment first
        current_value = self.slice_slider.value()
        if current_value > self.slice_slider.minimum():
            self.slice_slider.setValue(current_value - 1)
        # Then start continuous scroll
        self.scroll_direction = -1
        self.continuous_scroll_timer.start(200)  # 200ms interval for steady pace
        
    def start_right_scroll(self):
        """Start scrolling right when right arrow is pressed."""
        # Single increment first
        current_value = self.slice_slider.value()
        if current_value < self.slice_slider.maximum():
            self.slice_slider.setValue(current_value + 1)
        # Then start continuous scroll
        self.scroll_direction = 1
        self.continuous_scroll_timer.start(200)  # 200ms interval for steady pace
        
    def stop_continuous_scroll(self):
        """Stop continuous scrolling when arrow is released."""
        self.continuous_scroll_timer.stop()
        self.scroll_direction = 0
        
    def continuous_scroll(self):
        """Handle continuous scrolling while arrow is held."""
        current_value = self.slice_slider.value()
        new_value = current_value + self.scroll_direction
        
        if self.scroll_direction < 0 and new_value >= self.slice_slider.minimum():
            self.slice_slider.setValue(new_value)
        elif self.scroll_direction > 0 and new_value <= self.slice_slider.maximum():
            self.slice_slider.setValue(new_value)
        
    def create_highlight_overlay(self, node_indices=None, edge_indices=None):
        """
        Create a binary overlay highlighting specific nodes and/or edges using boolean indexing.
        
        Args:
            node_indices (list): List of node indices to highlight
            edge_indices (list): List of edge indices to highlight
        """
        if node_indices is None:
            node_indices = []
        if edge_indices is None:
            edge_indices = []
            
        if not node_indices and not edge_indices:
            self.highlight_overlay = None
            self.highlight_bounds = None
            self.update_display()
            return
            
        # Get the shape of the full array from any existing channel
        for channel in self.channel_data:
            if channel is not None:
                full_shape = channel.shape
                break
        else:
            return  # No valid channels to get shape from
            
        # Initialize full-size overlay
        self.highlight_overlay = np.zeros(full_shape, dtype=np.uint8)
        
        # Add nodes to highlight using boolean indexing
        if node_indices and self.channel_data[0] is not None:
            mask = np.isin(self.channel_data[0], node_indices)
            self.highlight_overlay[mask] = 255
                
        # Add edges to highlight using boolean indexing
        if edge_indices and self.channel_data[1] is not None:
            mask = np.isin(self.channel_data[1], edge_indices)
            self.highlight_overlay[mask] = 255
        
        # Update display
        self.update_display()



#METHODS RELATED TO RIGHT CLICK:
    
    def create_context_menu(self, event):
        """Create and show context menu at mouse position."""
        if self.channel_data[self.active_channel] is not None:
            x_idx = int(round(event.xdata))
            y_idx = int(round(event.ydata))
            
            try:
                # Create context menu
                context_menu = QMenu(self)
                
                # Create "Show Neighbors" submenu
                neighbors_menu = QMenu("Show Neighbors", self)
                
                # Add submenu options
                show_neighbor_nodes = neighbors_menu.addAction("Show Neighboring Nodes")
                show_neighbor_all = neighbors_menu.addAction("Show Neighboring Nodes and Edges")
                
                context_menu.addMenu(neighbors_menu)

                component_menu = QMenu("Show Connected Component(s)", self)
                show_component_nodes = component_menu.addAction("Just nodes")
                show_component_edges = component_menu.addAction("Nodes + Edges")
                context_menu.addMenu(component_menu)

                community_menu = QMenu("Show Community(s)", self)
                show_community_nodes = community_menu.addAction("Just nodes")
                show_community_edges = community_menu.addAction("Nodes + Edges")
                context_menu.addMenu(community_menu)

                # Create measure menu
                measure_menu = QMenu("Measure", self)

                if self.current_point is None:
                    # If no point is placed, show option to place first point
                    show_point_menu = measure_menu.addAction("Place Measurement Point")
                    show_point_menu.triggered.connect(
                        lambda: self.place_point(x_idx, y_idx, self.current_slice))
                else:
                    # If first point is placed, show option to place second point
                    show_point_menu = measure_menu.addAction("Place Second Point")
                    show_point_menu.triggered.connect(
                        lambda: self.place_point(x_idx, y_idx, self.current_slice))

                show_remove_menu = measure_menu.addAction("Remove Measurement Points")
                context_menu.addMenu(measure_menu)
                
                # Connect actions to callbacks
                show_neighbor_nodes.triggered.connect(self.handle_show_neighbors)
                show_neighbor_all.triggered.connect(lambda: self.handle_show_neighbors(edges=True))
                show_component_nodes.triggered.connect(self.handle_show_component)
                show_component_edges.triggered.connect(lambda: self.handle_show_component(edges = True))
                show_community_nodes.triggered.connect(self.handle_show_communities)
                show_community_edges.triggered.connect(lambda: self.handle_show_communities(edges = True))
                show_remove_menu.triggered.connect(self.handle_remove_points)
                
                cursor_pos = QCursor.pos()
                context_menu.exec(cursor_pos)
                
            except IndexError:
                pass


    def place_point(self, x, y, z):
        """Place a measurement point at the specified coordinates."""
        if self.current_point is None:
            # This is the first point
            self.current_point = (x, y, z)
            self.ax.plot(x, y, 'yo', markersize=8)
            # Add pair index label above the point
            self.ax.text(x, y+5, str(self.current_pair_index), 
                        color='white', ha='center', va='bottom')
            self.canvas.draw()

        else:
            # This is the second point
            x1, y1, z1 = self.current_point
            x2, y2, z2 = x, y, z
            
            # Calculate distance
            distance = np.sqrt(((x2-x1)*my_network.xy_scale)**2 + ((y2-y1)*my_network.xy_scale)**2 + ((z2-z1)*my_network.z_scale)**2)
            
            # Store the point pair
            self.measurement_points.append({
                'pair_index': self.current_pair_index,
                'point1': self.current_point,
                'point2': (x2, y2, z2),
                'distance': distance
            })
            
            # Draw second point and line
            self.ax.plot(x2, y2, 'yo', markersize=8)
            # Add pair index label above the second point
            self.ax.text(x2, y2+5, str(self.current_pair_index), 
                        color='white', ha='center', va='bottom')
            if z1 == z2:  # Only draw line if points are on same slice
                self.ax.plot([x1, x2], [y1, y2], 'r--', alpha=0.5)
            self.canvas.draw()
            
            # Update measurement display
            self.update_measurement_display()
            
            # Reset for next pair
            self.current_point = None
            self.current_pair_index += 1

    def handle_remove_points(self):
        """Remove all measurement points."""
        self.measurement_points = []
        self.current_point = None
        self.current_pair_index = 0
        self.update_display()
        self.update_measurement_display()

    # Modify the update_measurement_display method:
    def update_measurement_display(self):
        """Update the measurement information display in the top right widget."""
        if not self.measurement_points:
            # Create empty DataFrame with no specific headers
            df = pd.DataFrame()
        else:
            # Create data for DataFrame with measurement-specific headers
            data = []
            for point in self.measurement_points:
                x1, y1, z1 = point['point1']
                x2, y2, z2 = point['point2']
                data.append({
                    'Pair ID': point['pair_index'],
                    'Point 1 (X,Y,Z)': f"({x1:.1f}, {y1:.1f}, {z1})",
                    'Point 2 (X,Y,Z)': f"({x2:.1f}, {y2:.1f}, {z2})",
                    'Distance': f"{point['distance']:.2f}",
                    'xy_scale (used for distance calc)': f"{my_network.xy_scale}",
                    'z_scale (used for distance calc)': f"{my_network.z_scale}"
                })
            df = pd.DataFrame(data)
        
        # Create new table for measurements
        table = CustomTableView(self)
        table.setModel(PandasModel(df))
        
        # Add to tabbed widget
        self.tabbed_data.add_table("Measurements", table)
        
        # Adjust column widths to content
        for column in range(table.model().columnCount(None)):
            table.resizeColumnToContents(column)


    def show_network_table(self):
        """Switch to display the main network table."""
        if not self.network_button.isChecked():
            self.network_button.setChecked(True)
            return
        self.selection_button.setChecked(False)
        self.network_table.show()
        self.selection_table.hide()
        self.active_table = self.network_table

    def show_selection_table(self):
        """Switch to display the selection table."""
        if not self.selection_button.isChecked():
            self.selection_button.setChecked(True)
            return
        self.network_button.setChecked(False)
        self.network_table.hide()
        self.selection_table.show()
        self.active_table = self.selection_table

    def handle_show_neighbors(self, edges=False):
        """Handle the Show Neighbors action."""

        try:
            if len(self.clicked_values['nodes']) > 0:  # Check if we have any nodes selected
                neighbors = set()  # Use a set from the start to avoid duplicates
                original_nodes = self.clicked_values['nodes']
                
                # Get neighbors from network for all selected nodes
                for original_node in original_nodes:
                    neighbors.update(my_network.network.neighbors(original_node))
                self.clicked_values['nodes'] += neighbors
                
                # Get the existing DataFrame from the model
                original_df = self.network_table.model()._data
                
                # Create mask for rows where one column is any original node AND the other column is any neighbor
                mask = (
                    (original_df.iloc[:, 0].isin(original_nodes) & original_df.iloc[:, 1].isin(neighbors)) |
                    (original_df.iloc[:, 1].isin(original_nodes) & original_df.iloc[:, 0].isin(neighbors))
                )
                
                # Filter the DataFrame to only include direct connections
                filtered_df = original_df[mask].copy()
                
                # Create new model with filtered DataFrame and update selection table
                new_model = PandasModel(filtered_df)
                self.selection_table.setModel(new_model)
                
                # Switch to selection table
                self.selection_button.click()

                print(f"Found {len(filtered_df)} direct connections between nodes {original_nodes} and their neighbors")

                do_highlight = True


            elif len(self.clicked_values['nodes']) == 0 and len(self.clicked_values['edges']) > 0: #If we only have an edge selected, just give its neighbors, but selected nodes take priority
                neighbors = set()  # Use a set from the start to avoid duplicates
                original_edges = self.clicked_values['edges']

                original_nodes = []
                
                # Get the existing DataFrame from the model
                original_df = self.network_table.model()._data
                
                # Create mask for rows where one column is any original node AND the other column is any neighbor
                mask = (
                    (original_df.iloc[:, 2].isin(original_edges))
                )

                # Filter the DataFrame to only include direct connections
                filtered_df = original_df[mask].copy()

                neighbors = set(filtered_df.iloc[:, 0].to_list() + filtered_df.iloc[:, 1].to_list()) #Get neighboring nodes of this edge


                self.clicked_values['nodes'] += neighbors


                # Create new model with filtered DataFrame and update selection table
                new_model = PandasModel(filtered_df)
                self.selection_table.setModel(new_model)
                
                # Switch to selection table
                self.selection_button.click()

                do_highlight = True #A few variables to tell the highlighter what to do
                edges = True
                edge_indices = self.clicked_values['edges']

            else:

                do_highlight = False

            if do_highlight:
              
                # Create highlight overlay for visualization
                if edges:
                    edge_indices = filtered_df.iloc[:, 2].unique().tolist()
                    self.clicked_values['edges'] = edge_indices
                    self.create_highlight_overlay(
                        node_indices=list(original_nodes) + list(neighbors), 
                        edge_indices=edge_indices
                    )
                else:
                    self.create_highlight_overlay(
                        node_indices=list(original_nodes) + list(neighbors)
                )
            
                
        except Exception as e:
            print(f"Error processing neighbors: {e}")

    
    def handle_show_component(self, edges = False):
        """Handle the Show Component action."""

        try:

            if len(self.clicked_values['nodes']) == 0: #If we haven't clicked anything, this will return the largest connected component

                G = my_network.isolate_connected_component(gen_images = False)

                # Get the existing DataFrame from the model
                original_df = self.network_table.model()._data

                # Create mask for rows where one column is any original node AND the other column is any neighbor
                mask = (
                    (original_df.iloc[:, 0].isin(G.nodes()) & original_df.iloc[:, 1].isin(G.nodes()))
                    )
                
                # Filter the DataFrame to only include direct connections
                filtered_df = original_df[mask].copy()

                # Create new model with filtered DataFrame and update selection table
                new_model = PandasModel(filtered_df)
                self.selection_table.setModel(new_model)
                
                # Switch to selection table
                self.selection_button.click()


            else: #If we have clicked any nodes, we get the components of the clicked objects instead

                G = nx.Graph()

                for node in self.clicked_values['nodes']:

                    if node in G: #Meaning we've already done this component
                        continue
                    else: #Otherwise, get the graph and add it to the subgraph(s)
                        G1 = my_network.isolate_connected_component(gen_images = False, key = node)
                        G = nx.compose(G1, G)

                # Get the existing DataFrame from the model
                original_df = self.network_table.model()._data

                # Create mask for rows where one column is any original node AND the other column is any neighbor
                mask = (
                    (original_df.iloc[:, 0].isin(G.nodes()) & original_df.iloc[:, 1].isin(G.nodes()))
                    )
                
                # Filter the DataFrame to only include direct connections
                filtered_df = original_df[mask].copy()
                
                # Create new model with filtered DataFrame and update selection table
                new_model = PandasModel(filtered_df)
                self.selection_table.setModel(new_model)
                
                # Switch to selection table
                self.selection_button.click()

            if edges:
                edge_indices = filtered_df.iloc[:, 2].unique().tolist()
                self.clicked_values['edges'] = edge_indices
                self.create_highlight_overlay(
                    node_indices=G.nodes(),
                    edge_indices=edge_indices
                )
                self.clicked_values['nodes'] = G.nodes()
            else:
                self.create_highlight_overlay(
                    node_indices = G.nodes()
            )
                self.clicked_values['nodes'] = G.nodes()

        except Exception as e:

            print(f"Error finding component: {e}")

    def handle_show_communities(self, edges = False):

        def invert_dict(d):
            """For inverting the community dictionary"""
            inverted = {}
            for key, value in d.items():
                inverted.setdefault(value, []).append(key)
            return inverted

        try:

            if len(self.clicked_values['nodes']) > 0:

                if my_network.communities is None:
                    self.show_partition_dialog()

                communities = invert_dict(my_network.communities)

                targets = []

                for node in self.clicked_values['nodes']: #Get the communities we need

                    if node in targets:
                        continue
                    else:
                        targets.append(my_network.communities[node])

                nodes = []

                for com in targets: #Get the nodes for each community in question

                    for node in communities[com]:

                        nodes.append(node)

                nodes = list(set(nodes))

                # Get the existing DataFrame from the model
                original_df = self.network_table.model()._data

                # Create mask for rows for nodes in question
                mask = (
                    (original_df.iloc[:, 0].isin(nodes) & original_df.iloc[:, 1].isin(nodes))
                    )
                
                # Filter the DataFrame to only include direct connections
                filtered_df = original_df[mask].copy()
                
                # Create new model with filtered DataFrame and update selection table
                new_model = PandasModel(filtered_df)
                self.selection_table.setModel(new_model)
                
                # Switch to selection table
                self.selection_button.click()

                if edges:
                    edge_indices = filtered_df.iloc[:, 2].unique().tolist()
                    self.clicked_values['edges'] = edge_indices
                    self.create_highlight_overlay(
                        node_indices=nodes,
                        edge_indices=edge_indices
                    )
                    self.clicked_values['nodes'] = nodes
                else:
                    self.create_highlight_overlay(
                        node_indices = nodes
                )
                    self.clicked_values['nodes'] = nodes

        except Exception as e:
            print(f"Error showing communities: {e}")

        
    def toggle_zoom_mode(self):
        """Toggle zoom mode on/off."""
        self.zoom_mode = self.zoom_button.isChecked()
        if self.zoom_mode:
            self.pan_button.setChecked(False)
            self.pan_mode = False
            self.canvas.setCursor(Qt.CursorShape.CrossCursor)
        else:
            self.canvas.setCursor(Qt.CursorShape.ArrowCursor)

    def toggle_pan_mode(self):
        """Toggle pan mode on/off."""
        self.pan_mode = self.pan_button.isChecked()
        if self.pan_mode:
            self.zoom_button.setChecked(False)
            self.zoom_mode = False
            self.canvas.setCursor(Qt.CursorShape.OpenHandCursor)
        else:
            self.canvas.setCursor(Qt.CursorShape.ArrowCursor)

    def on_mouse_press(self, event):
        """Handle mouse press events."""
        if event.inaxes != self.ax:
            return
                
        if self.zoom_mode:
            # Handle zoom mode press
            if self.original_xlim is None:
                self.original_xlim = self.ax.get_xlim()
                self.original_ylim = self.ax.get_ylim()
            
            current_xlim = self.ax.get_xlim()
            current_ylim = self.ax.get_ylim()
            xdata = event.xdata
            ydata = event.ydata
            
            if event.button == 1:  # Left click - zoom in
                x_range = (current_xlim[1] - current_xlim[0]) / 4
                y_range = (current_ylim[1] - current_ylim[0]) / 4
                
                self.ax.set_xlim([xdata - x_range, xdata + x_range])
                self.ax.set_ylim([ydata - y_range, ydata + y_range])
                
            elif event.button == 3:  # Right click - zoom out
                x_range = (current_xlim[1] - current_xlim[0])
                y_range = (current_ylim[1] - current_ylim[0])
                
                new_xlim = [xdata - x_range, xdata + x_range]
                new_ylim = [ydata - y_range, ydata + y_range]
                
                if (new_xlim[0] <= self.original_xlim[0] or 
                    new_xlim[1] >= self.original_xlim[1] or
                    new_ylim[0] <= self.original_ylim[0] or
                    new_ylim[1] >= self.original_ylim[1]):
                    self.ax.set_xlim(self.original_xlim)
                    self.ax.set_ylim(self.original_ylim)
                else:
                    self.ax.set_xlim(new_xlim)
                    self.ax.set_ylim(new_ylim)
            
            self.canvas.draw()
                
        elif self.pan_mode:
            self.panning = True
            self.pan_start = (event.xdata, event.ydata)
            self.canvas.setCursor(Qt.CursorShape.ClosedHandCursor)
        
        elif event.button == 3:  # Right click (for context menu)
            self.create_context_menu(event)
        
        elif event.button == 1:  # Left click
            # Store initial click position but don't start selection yet
            self.selection_start = (event.xdata, event.ydata)
            self.selecting = False  # Will be set to True if the mouse moves while button is held

    def on_mouse_move(self, event):
        """Handle mouse movement events."""
        if event.inaxes != self.ax:
            return
                
        if self.selection_start and not self.selecting and not self.pan_mode and not self.zoom_mode:
            # If mouse has moved more than a tiny amount while button is held, start selection
            if (abs(event.xdata - self.selection_start[0]) > 1 or 
                abs(event.ydata - self.selection_start[1]) > 1):
                self.selecting = True
                self.selection_rect = plt.Rectangle(
                    (self.selection_start[0], self.selection_start[1]), 0, 0,
                    fill=False, color='white', linestyle='--'
                )
                self.ax.add_patch(self.selection_rect)
                
        if self.selecting and self.selection_rect is not None:
            # Update selection rectangle
            x0 = min(self.selection_start[0], event.xdata)
            y0 = min(self.selection_start[1], event.ydata)
            width = abs(event.xdata - self.selection_start[0])
            height = abs(event.ydata - self.selection_start[1])
            
            self.selection_rect.set_bounds(x0, y0, width, height)
            self.canvas.draw()

        elif self.panning and self.pan_start is not None:
            # Calculate the movement
            dx = event.xdata - self.pan_start[0]
            dy = event.ydata - self.pan_start[1]
            
            # Get current view limits
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            
            # Calculate new limits
            new_xlim = [xlim[0] - dx, xlim[1] - dx]
            new_ylim = [ylim[0] - dy, ylim[1] - dy]
            
            # Get image bounds
            if self.channel_data[0] is not None:  # Use first channel as reference
                img_height, img_width = self.channel_data[0][self.current_slice].shape
                
                # Ensure new limits don't go beyond image bounds
                if new_xlim[0] < 0:
                    new_xlim = [0, xlim[1] - xlim[0]]
                elif new_xlim[1] > img_width:
                    new_xlim = [img_width - (xlim[1] - xlim[0]), img_width]
                    
                if new_ylim[0] < 0:
                    new_ylim = [0, ylim[1] - ylim[0]]
                elif new_ylim[1] > img_height:
                    new_ylim = [img_height - (ylim[1] - ylim[0]), img_height]
            
            # Apply new limits
            self.ax.set_xlim(new_xlim)
            self.ax.set_ylim(new_ylim)
            self.canvas.draw()
            
            # Update pan start position
            self.pan_start = (event.xdata, event.ydata)

    def on_mouse_release(self, event):
        """Handle mouse release events."""
        if self.pan_mode:
            self.panning = False
            self.pan_start = None
            self.canvas.setCursor(Qt.CursorShape.OpenHandCursor)
        elif event.button == 1:  # Left button release
            if self.selecting and self.selection_rect is not None:
                # Get the rectangle bounds
                x0 = min(self.selection_start[0], event.xdata)
                y0 = min(self.selection_start[1], event.ydata)
                width = abs(event.xdata - self.selection_start[0])
                height = abs(event.ydata - self.selection_start[1])
                
                # Get current slice data for active channel
                if self.channel_data[self.active_channel] is not None:
                    data = self.channel_data[self.active_channel][self.current_slice]
                    
                    # Convert coordinates to array indices
                    x_min = max(0, int(x0))
                    y_min = max(0, int(y0))
                    x_max = min(data.shape[1], int(x0 + width))
                    y_max = min(data.shape[0], int(y0 + height))
                    
                    # Extract unique non-zero values in selection rectangle
                    selected_region = data[y_min:y_max, x_min:x_max]
                    selected_values = np.unique(selected_region)
                    selected_values = selected_values[selected_values != 0]  # Remove background
                    
                    # Check if ctrl is pressed
                    ctrl_pressed = 'ctrl' in event.modifiers
                    
                    # Update clicked_values based on active channel
                    if self.active_channel == 0:  # Nodes
                        if not ctrl_pressed:
                            self.clicked_values['nodes'] = []  # Clear existing selection if ctrl not pressed
                        self.clicked_values['nodes'].extend(selected_values)
                        # Remove duplicates while preserving order
                        self.clicked_values['nodes'] = list(dict.fromkeys(self.clicked_values['nodes']))
                        self.create_highlight_overlay(node_indices=self.clicked_values['nodes'])
                        
                        # Try to highlight the last selected value in tables
                        if self.clicked_values['nodes']:
                            self.highlight_value_in_tables(self.clicked_values['nodes'][-1])
                            
                    elif self.active_channel == 1:  # Edges
                        if not ctrl_pressed:
                            self.clicked_values['edges'] = []  # Clear existing selection if ctrl not pressed
                        self.clicked_values['edges'].extend(selected_values)
                        # Remove duplicates while preserving order
                        self.clicked_values['edges'] = list(dict.fromkeys(self.clicked_values['edges']))
                        self.create_highlight_overlay(edge_indices=self.clicked_values['edges'])
                        
                        # Try to highlight the last selected value in tables
                        if self.clicked_values['edges']:
                            self.highlight_value_in_tables(self.clicked_values['edges'][-1])
            
            elif not self.selecting and self.selection_start:  # If we had a click but never started selection
                # Handle as a normal click
                self.on_mouse_click(event)
            
            # Clean up
            self.selection_start = None
            self.selecting = False
            if self.selection_rect is not None:
                self.selection_rect.remove()
                self.selection_rect = None
                self.canvas.draw()


    def highlight_value_in_tables(self, clicked_value):
        """Helper method to find and highlight a value in both tables."""
        
        if not self.network_table.model() and not self.selection_table.model():
            return False

        found = False
        tables_to_check = [self.network_table, self.selection_table]
        active_table_index = tables_to_check.index(self.active_table)
        
        # Reorder tables to check active table first
        tables_to_check = tables_to_check[active_table_index:] + tables_to_check[:active_table_index]
        
        for table in tables_to_check:
            
            if table.model() is None:
                continue
                
            df = table.model()._data

            
            # Create appropriate masks based on active channel
            if self.active_channel == 0:  # Nodes channel
                col1_matches = df[df.columns[0]] == clicked_value
                col2_matches = df[df.columns[1]] == clicked_value
                all_matches = col1_matches | col2_matches

            elif self.active_channel == 1:  # Edges channel
                all_matches = df[df.columns[2]] == clicked_value

            else:
                continue

            if all_matches.any():
                # Get indices from the current dataframe's index
                match_indices = df[all_matches].index.tolist()
                
                # If this is the active table, handle selection and scrolling
                if table == self.active_table:
                    current_row = table.currentIndex().row()
                    
                    # Convert match_indices to row numbers (position in the visible table)
                    row_positions = [df.index.get_loc(idx) for idx in match_indices]
                    
                    # Find next match after current position
                    if current_row >= 0:
                        next_positions = [pos for pos in row_positions if pos > current_row]
                        row_pos = next_positions[0] if next_positions else row_positions[0]
                    else:
                        row_pos = row_positions[0]
                    
                    # Update selection and scroll
                    model_index = table.model().index(row_pos, 0)
                    table.scrollTo(model_index)
                    table.clearSelection()
                    table.selectRow(row_pos)
                    table.setCurrentIndex(model_index)

                
                # Update bold formatting regardless of whether it's the active table
                table.model().set_bold_value(clicked_value, self.active_channel)
                found = True

        return found
        
    def on_mouse_click(self, event):
        """Handle mouse clicks for zooming and data inspection."""
        if event.inaxes != self.ax:
            return
            
        if self.zoom_mode:
            # Existing zoom functionality
            if self.original_xlim is None:
                self.original_xlim = self.ax.get_xlim()
                self.original_ylim = self.ax.get_ylim()
            
            current_xlim = self.ax.get_xlim()
            current_ylim = self.ax.get_ylim()
            xdata = event.xdata
            ydata = event.ydata
            
            if event.button == 1:  # Left click - zoom in
                x_range = (current_xlim[1] - current_xlim[0]) / 4
                y_range = (current_ylim[1] - current_ylim[0]) / 4
                
                self.ax.set_xlim([xdata - x_range, xdata + x_range])
                self.ax.set_ylim([ydata - y_range, ydata + y_range])
                
            elif event.button == 3:  # Right click - zoom out
                x_range = (current_xlim[1] - current_xlim[0])
                y_range = (current_ylim[1] - current_ylim[0])
                
                new_xlim = [xdata - x_range, xdata + x_range]
                new_ylim = [ydata - y_range, ydata + y_range]
                
                if (new_xlim[0] <= self.original_xlim[0] or 
                    new_xlim[1] >= self.original_xlim[1] or
                    new_ylim[0] <= self.original_ylim[0] or
                    new_ylim[1] >= self.original_ylim[1]):
                    self.ax.set_xlim(self.original_xlim)
                    self.ax.set_ylim(self.original_ylim)
                else:
                    self.ax.set_xlim(new_xlim)
                    self.ax.set_ylim(new_ylim)
            
            self.canvas.draw()
        
        elif event.button == 3:  # Right click
            self.create_context_menu(event)

        else:  # Not in zoom mode - handle value inspection
            if self.channel_data[self.active_channel] is not None:
                try:
                    # Get clicked value
                    x_idx = int(round(event.xdata))
                    y_idx = int(round(event.ydata))
                    if self.channel_data[self.active_channel][self.current_slice, y_idx, x_idx] != 0:
                        clicked_value = self.channel_data[self.active_channel][self.current_slice, y_idx, x_idx]
                    else:
                        self.clicked_values = {
                            'nodes': [],
                            'edges': []
                        }
                        self.create_highlight_overlay()
                        return
                    
                    # Check if Ctrl key is pressed (using matplotlib's key_press system)
                    ctrl_pressed = 'ctrl' in event.modifiers  # Note: changed from 'control' to 'ctrl'
                    
                    # Store or remove the clicked value in the appropriate list
                    if self.active_channel == 0:
                        if ctrl_pressed:
                            if clicked_value in self.clicked_values['nodes']:
                                # Remove value if it's already selected
                                self.clicked_values['nodes'].remove(clicked_value)
                            else:
                                # Add value if it's not already selected
                                self.clicked_values['nodes'].append(clicked_value)
                        else:
                            # Reset both lists and start new selection
                            self.clicked_values = {'nodes': [clicked_value], 'edges': []}
                        # Get latest value (or the last remaining one if we just removed an item)
                        latest_value = self.clicked_values['nodes'][-1] if self.clicked_values['nodes'] else None
                    elif self.active_channel == 1:
                        if ctrl_pressed:
                            if clicked_value in self.clicked_values['edges']:
                                # Remove value if it's already selected
                                self.clicked_values['edges'].remove(clicked_value)
                            else:
                                # Add value if it's not already selected
                                self.clicked_values['edges'].append(clicked_value)
                        else:
                            # Reset both lists and start new selection
                            self.clicked_values = {'nodes': [], 'edges': [clicked_value]}
                        # Get latest value (or the last remaining one if we just removed an item)
                        latest_value = self.clicked_values['edges'][-1] if self.clicked_values['edges'] else None
                    
                    # Try to find and highlight the latest value in the current table
                    found = self.highlight_value_in_tables(latest_value)
                    
                    # If not found in current table but it exists in the other table, offer to switch
                    if not found:
                        other_table = self.selection_table if self.active_table == self.network_table else self.network_table
                        if other_table.model() is not None:
                            df = other_table.model()._data
                            if self.active_channel == 0:
                                exists_in_other = (df[df.columns[0]] == latest_value).any() or (df[df.columns[1]] == latest_value).any()
                            else:
                                exists_in_other = (df[df.columns[2]] == latest_value).any()
                                
                            if exists_in_other:
                                # Switch to the other table
                                if other_table == self.network_table:
                                    self.network_button.click()
                                else:
                                    self.selection_button.click()
                                # Now highlight in the newly active table
                                self.highlight_value_in_tables(latest_value)

                    # Highlight the clicked element in the image using the stored lists
                    if self.active_channel == 0:
                        self.create_highlight_overlay(node_indices=self.clicked_values['nodes'])
                    elif self.active_channel == 1:
                        self.create_highlight_overlay(edge_indices=self.clicked_values['edges'])

                                
                except IndexError:
                    pass  # Clicked outside image boundaries
                
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")

        # Create Save submenu
        save_menu = file_menu.addMenu("Save")
        network_save = save_menu.addAction("Save Network3D Object")
        network_save.triggered.connect(lambda: self.save_network_3d(False))
        for i in range(4):
            save_action = save_menu.addAction(f"Save {self.channel_names[i]}")
            save_action.triggered.connect(lambda checked, ch=i: self.save(ch, False))
        highlight_save = save_menu.addAction("Save Highlight Overlay")
        highlight_save.triggered.connect(lambda checked, ch=4: self.save(ch, False))

        # Create Save As submenu
        save_as_menu = file_menu.addMenu("Save As")
        network_saveas = save_as_menu.addAction("Save Network3D Object As")
        network_saveas.triggered.connect(lambda: self.save_network_3d(True))
        for i in range(4):
            save_action = save_as_menu.addAction(f"Save {self.channel_names[i]} As")
            save_action.triggered.connect(lambda checked, ch=i: self.save(ch))
        highlight_save = save_as_menu.addAction("Save Highlight Overlay As")
        highlight_save.triggered.connect(lambda checked, ch=4: self.save(ch))
        
        # Create Load submenu
        load_menu = file_menu.addMenu("Load")
        network_load = load_menu.addAction("Load Network3D Object")
        network_load.triggered.connect(self.load_from_network_obj)
        for i in range(4):
            load_action = load_menu.addAction(f"Load {self.channel_names[i]}")
            load_action.triggered.connect(lambda checked, ch=i: self.load_channel(ch))
        load_action = load_menu.addAction("Load Network")
        load_action.triggered.connect(self.load_network)

        
        # Analysis menu
        analysis_menu = menubar.addMenu("Analyze")
        network_menu = analysis_menu.addMenu("Network")
        netshow_action = network_menu.addAction("Show Network")
        netshow_action.triggered.connect(self.show_netshow_dialog)
        partition_action = network_menu.addAction("Community Partition")
        partition_action.triggered.connect(self.show_partition_dialog)
        stats_menu = analysis_menu.addMenu("Stats")
        allstats_action = stats_menu.addAction("Calculate All Stats")
        allstats_action.triggered.connect(self.stats)

        # Process menu
        process_menu = menubar.addMenu("Process")
        calculate_menu = process_menu.addMenu("Calculate")
        calc_all_action = calculate_menu.addAction("Calculate All (Find Node-Edge-Node Network)")
        calc_all_action.triggered.connect(self.show_calc_all_dialog)
        centroid_action = calculate_menu.addAction("Calculate Centroids (Active Image)")
        centroid_action.triggered.connect(self.show_centroid_dialog)

        image_menu = process_menu.addMenu("Image")
        resize_action = image_menu.addAction("Resize (Up/Downsample)")
        resize_action.triggered.connect(self.show_resize_dialog)
        dilate_action = image_menu.addAction("Dilate")
        dilate_action.triggered.connect(self.show_dilate_dialog)
        binarize_action = image_menu.addAction("Binarize")
        binarize_action.triggered.connect(self.show_binarize_dialog)
        label_action = image_menu.addAction("Label Objects")
        label_action.triggered.connect(self.show_label_dialog)
        skeletonize_action = image_menu.addAction("Skeletonize")
        skeletonize_action.triggered.connect(self.show_skeletonize_dialog)
        watershed_action = image_menu.addAction("Watershed")
        watershed_action.triggered.connect(self.show_watershed_dialog)


        gennodes_action = process_menu.addAction("Generate Nodes (From 'Edge' Vertices)")
        gennodes_action.triggered.connect(self.show_gennodes_dialog)

        
        # Image menu
        image_menu = menubar.addMenu("Image")
        brightness_action = image_menu.addAction("Adjust Brightness/Contrast")
        brightness_action.triggered.connect(self.show_brightness_dialog)
        show3d_action = image_menu.addAction("Show 3D (beta)")
        show3d_action.triggered.connect(self.show3d_dialog)

    def stats(self):
        """Method to get and display the network stats"""
        # Get the stats dictionary
        stats = my_network.get_network_stats()
        
        # Convert the dictionary into a DataFrame format
        df = pd.DataFrame({
            'Metric': stats.keys(),
            'Value': stats.values()
        })
        
        # Format any floating point numbers
        df['Value'] = df['Value'].apply(lambda x: f"{x:.3f}" if isinstance(x, float) else str(x))
        
        # Create new table
        table = CustomTableView(self)
        table.setModel(PandasModel(df))
        
        # Add to tabbed widget
        self.tabbed_data.add_table("Network Stats", table)
        
        # Adjust column widths to content
        for column in range(table.model().columnCount(None)):
            table.resizeColumnToContents(column)

    def format_for_upperright_table(self, some_dict, metric='Metric', value='Value'):
        # Transform the data into two columns
        df = pd.DataFrame({
            metric: some_dict.keys(),
            value: some_dict.values()
        })
        
        # Format any floating point numbers
        df[value] = df[value].apply(lambda x: f"{x:.3f}" if isinstance(x, float) else str(x))
        
        # Create new table
        table = CustomTableView(self)
        table.setModel(PandasModel(df))
        
        # Add to tabbed widget with appropriate name
        self.tabbed_data.add_table(f"{metric} Analysis", table)
        
        # Adjust column widths to content
        for column in range(table.model().columnCount(None)):
            table.resizeColumnToContents(column)


    def show_watershed_dialog(self):
        """Show the watershed parameter dialog."""
        dialog = WatershedDialog(self)
        dialog.exec()

    def show_calc_all_dialog(self):
        """Show the calculate all parameter dialog."""
        dialog = CalcAllDialog(self)
        dialog.exec()

    def show_centroid_dialog(self):
        """show the centroid dialog"""
        dialog = CentroidDialog(self)
        dialog.exec()

    def show_dilate_dialog(self):
        """show the dilate dialog"""
        dialog = DilateDialog(self)
        dialog.exec()

    def show_label_dialog(self):
        """Show the label dialog"""
        dialog = LabelDialog(self)
        dialog.exec()

    def show_skeletonize_dialog(self):
        """show the skeletonize dialog"""
        dialog = SkeletonizeDialog(self)
        dialog.exec()

    def show_gennodes_dialog(self):
        """show the gennodes dialog"""
        gennodes = GenNodesDialog(self)
        gennodes.exec()


    def show_binarize_dialog(self):
        """show the binarize dialog"""
        dialog = BinarizeDialog(self)
        dialog.exec()


    def show_resize_dialog(self):
        """show the resize dialog"""
        dialog = ResizeDialog(self)
        dialog.exec()
    
    def show_brightness_dialog(self):
        """Show the brightness/contrast control dialog."""
        self.brightness_dialog.show()

    def show3d_dialog(self):
        """Show the 3D control dialog"""
        dialog = Show3dDialog(self)
        dialog.exec()
    

    # Modify load_from_network_obj method
    def load_from_network_obj(self):
        try: 
            directory = QFileDialog.getExistingDirectory(
                self,
                f"Select Directory for Network3D Object",
                "",
                QFileDialog.Option.ShowDirsOnly
            )

            my_network.assemble(directory)

            # Load image channels
            try:
                self.load_channel(0, my_network.nodes, True)
            except Exception as e:
                print(e)
            try:
                self.load_channel(1, my_network.edges, True)
            except Exception as e:
                print(e)
            try:
                self.load_channel(2, my_network.network_overlay, True)
            except Exception as e:
                print(e)
            try:
                self.load_channel(3, my_network.id_overlay, True)
            except Exception as e:
                print(e)

            # Update slider range based on new data
            for channel in self.channel_data:
                if channel is not None:
                    self.slice_slider.setEnabled(True)
                    self.slice_slider.setMinimum(0)
                    self.slice_slider.setMaximum(channel.shape[0] - 1)
                    self.slice_slider.setValue(0)
                    self.current_slice = 0
                    break

            # Display network_lists in the network table
            try:
                if hasattr(my_network, 'network_lists'):
                    model = PandasModel(my_network.network_lists)
                    self.network_table.setModel(model)
                    # Adjust column widths to content
                    for column in range(model.columnCount(None)):
                        self.network_table.resizeColumnToContents(column)
            except Exception as e:
                print(f"Error loading network table: {e}")

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error Loading Network 3D Object",
                f"Failed to load Network 3D Object: {str(e)}"
            )


    def load_network(self):
        """Load in the network from a .xlsx (need to add .csv support)"""

        try:

            filename, _ = QFileDialog.getOpenFileName(
                self,
                f"Load Network",
                "",
                "Spreadsheets (*.xlsx *.csv)"
            )

            my_network.load_network(file_path = filename)

            # Display network_lists in the network table
            try:
                if hasattr(my_network, 'network_lists'):
                    model = PandasModel(my_network.network_lists)
                    self.network_table.setModel(model)
                    # Adjust column widths to content
                    for column in range(model.columnCount(None)):
                        self.network_table.resizeColumnToContents(column)
            except Exception as e:
                print(f"Error loading network table: {e}")

        except Exception as e:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.critical(
                self,
                "Error Loading File",
                f"Failed to load network: {str(e)}"
            )



    def set_active_channel(self, index):
        """Set the active channel and update UI accordingly."""
        self.active_channel = index
        # Update button appearances to show active channel
        for i, btn in enumerate(self.channel_buttons):
            if i == index and btn.isEnabled():
                btn.setStyleSheet("background-color: lightblue;")
            else:
                btn.setStyleSheet("")

    def load_channel(self, channel_index, channel_data=None, data=False):
        """Load a channel and enable active channel selection if needed."""

        try:
            if not data:  # For solo loading
                import tifffile
                filename, _ = QFileDialog.getOpenFileName(
                    self,
                    f"Load Channel {channel_index + 1}",
                    "",
                    "TIFF Files (*.tif *.tiff)"
                )
                self.channel_data[channel_index] = tifffile.imread(filename)
                if channel_index == 0:
                    my_network.nodes = self.channel_data[channel_index]
                elif channel_index == 1:
                    my_network.edges = self.channel_data[channel_index]
                elif channel_index == 2:
                    my_network.network_overlay = self.channel_data[channel_index]
                elif channel_index == 3:
                    my_network.id_overlay = self.channel_data[channel_index]
            else:
                self.channel_data[channel_index] = channel_data
            
            # Enable the channel button
            self.channel_buttons[channel_index].setEnabled(True)
            self.delete_buttons[channel_index].setEnabled(True) 

            
            # Enable active channel selector if this is the first channel loaded
            if not self.active_channel_combo.isEnabled():
                self.active_channel_combo.setEnabled(True)
            
            # Update slider range if this is the first channel loaded
            if not self.slice_slider.isEnabled():
                self.slice_slider.setEnabled(True)
                self.slice_slider.setMinimum(0)
                self.slice_slider.setMaximum(self.channel_data[channel_index].shape[0] - 1)
                self.slice_slider.setValue(0)
                self.current_slice = 0
            else:
                self.slice_slider.setEnabled(True)
                self.slice_slider.setMinimum(0)
                self.slice_slider.setMaximum(self.channel_data[channel_index].shape[0] - 1)
                self.slice_slider.setValue(0)
                self.current_slice = 0

            
            # If this is the first channel loaded, make it active
            if all(not btn.isEnabled() for btn in self.channel_buttons[:channel_index]):
                self.set_active_channel(channel_index)
            
            #self.update_display(preserve_zoom=(current_xlim, current_ylim))
            self.update_display()

                
        except Exception as e:
            if not data:
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.critical(
                    self,
                    "Error Loading File",
                    f"Failed to load tiff file: {str(e)}"
                )

    def delete_channel(self, channel_index):
        """Delete the specified channel and update the display."""
        # Confirm deletion
        reply = QMessageBox.question(
            self,
            'Delete Channel',
            f'Are you sure you want to delete the {self.channel_names[channel_index]} channel?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            # Set channel data to None
            self.channel_data[channel_index] = None
            
            # Update corresponding network property
            if channel_index == 0:
                my_network.nodes = None
            elif channel_index == 1:
                my_network.edges = None
            elif channel_index == 2:
                my_network.network_overlay = None
            elif channel_index == 3:
                my_network.id_overlay = None
            
            # Disable buttons
            self.channel_buttons[channel_index].setEnabled(False)
            self.channel_buttons[channel_index].setChecked(False)
            self.delete_buttons[channel_index].setEnabled(False)
            self.channel_visible[channel_index] = False
            
            # If this was the active channel, switch to the first available channel
            if self.active_channel == channel_index:
                for i in range(4):
                    if self.channel_data[i] is not None:
                        self.set_active_channel(i)
                        break
                else:
                    # If no channels are available, disable active channel selector
                    self.active_channel_combo.setEnabled(False)
            
            # Update display
            self.update_display()


    def save_network_3d(self, asbool = True):

        try:
            if asbool:  # Save As
                # First let user select parent directory
                parent_dir = QFileDialog.getExistingDirectory(
                    self,
                    "Select Location for Network3D Object Outputs",
                    "",
                    QFileDialog.Option.ShowDirsOnly
                )

                if parent_dir:  # If user didn't cancel
                    # Prompt user for new folder name
                    new_folder_name, ok = QInputDialog.getText(
                        self,
                        "New Folder",
                        "Enter name for new output folder:"
                    )
                
            else:  # Save
                parent_dir = None  # Let the backend handle default save location
            
            # Call appropriate save method
            if parent_dir is not None or not asbool:  # Proceed if we have a filename OR if it's a regular save
                if asbool:
                    my_network.dump(parent_dir = parent_dir, name = new_folder_name)
                else:
                    my_network.dump(name = 'my_network')
                
                
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error Saving File",
                f"Failed to save file: {str(e)}"
            )


    def save(self, ch_index, asbool=True):
        """Handle both Save and Save As operations."""
        try:
            if asbool:  # Save As
                # Open file dialog for saving
                filename, _ = QFileDialog.getSaveFileName(
                    self,
                    f"Save Image As",
                    "",  # Default directory
                    "TIFF Files (*.tif *.tiff);;All Files (*)"  # File type filter
                )
                
                if filename:  # Only proceed if user didn't cancel
                    # If user didn't type an extension, add .tif
                    if not filename.endswith(('.tif', '.tiff')):
                        filename += '.tif'
            else:  # Save
                filename = None  # Let the backend handle default save location
            
            # Call appropriate save method
            if filename is not None or not asbool:  # Proceed if we have a filename OR if it's a regular save
                if ch_index == 0:
                    my_network.save_nodes(filename=filename)
                elif ch_index == 1:
                    my_network.save_edges(filename=filename)
                elif ch_index == 2:
                    my_network.save_network_overlay(filename=filename)
                elif ch_index == 3:
                    my_network.save_id_overlay(filename=filename)
                elif ch_index == 4:
                    if filename == None:
                        filename = "Highlighted_Element.tif"
                    tifffile.imwrite(f"{filename}", self.highlight_overlay)
                
                #print(f"Saved {self.channel_names[ch_index]}" + (f" to: {filename}" if filename else ""))  # Debug print
                
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error Saving File",
                f"Failed to save file: {str(e)}"
            )

    def toggle_channel(self, channel_index):
        """Toggle visibility of a channel."""
        # Store current zoom settings before toggling
        current_xlim = self.ax.get_xlim() if hasattr(self, 'ax') and self.ax.get_xlim() != (0, 1) else None
        current_ylim = self.ax.get_ylim() if hasattr(self, 'ax') and self.ax.get_ylim() != (0, 1) else None
        
        self.channel_visible[channel_index] = self.channel_buttons[channel_index].isChecked()
        self.update_display(preserve_zoom=(current_xlim, current_ylim))

    
    def update_slice(self):
        """Queue a slice update when slider moves."""
        # Store current view settings
        current_xlim = self.ax.get_xlim() if hasattr(self, 'ax') and self.ax.get_xlim() != (0, 1) else None
        current_ylim = self.ax.get_ylim() if hasattr(self, 'ax') and self.ax.get_ylim() != (0, 1) else None
        
        # Store the pending slice and view settings
        self.pending_slice = (self.slice_slider.value(), (current_xlim, current_ylim))
        
        # Reset and restart timer
        self._slice_update_timer.start(20)  # 20ms delay
        
    def _do_slice_update(self):
        """Actually perform the slice update after debounce delay."""
        if self.pending_slice is not None:
            slice_value, view_settings = self.pending_slice
            self.current_slice = slice_value
            self.update_display(preserve_zoom=view_settings)
            self.pending_slice = None

    def update_brightness(self, channel_index, values):
        """Update brightness/contrast settings for a channel."""

        # Store current zoom settings before toggling
        current_xlim = self.ax.get_xlim() if hasattr(self, 'ax') and self.ax.get_xlim() != (0, 1) else None
        current_ylim = self.ax.get_ylim() if hasattr(self, 'ax') and self.ax.get_ylim() != (0, 1) else None
        # Convert slider values (0-100) to data values (0-1)
        min_val, max_val = values
        self.channel_brightness[channel_index]['min'] = min_val / 100
        self.channel_brightness[channel_index]['max'] = max_val / 100
        self.update_display(preserve_zoom = (current_xlim, current_ylim))
    
    def update_display(self, preserve_zoom=None):
        """Update the display with currently visible channels and highlight overlay."""
        self.figure.clear()
        
        # Create subplot with tight layout and white figure background
        self.figure.patch.set_facecolor('white')
        self.ax = self.figure.add_subplot(111)
        
        # Store current zoom limits if they exist and weren't provided
        if preserve_zoom is None and hasattr(self, 'ax'):
            current_xlim = self.ax.get_xlim() if self.ax.get_xlim() != (0, 1) else None
            current_ylim = self.ax.get_ylim() if self.ax.get_ylim() != (0, 1) else None
        else:
            current_xlim, current_ylim = preserve_zoom if preserve_zoom else (None, None)
        
        # Define base colors for each channel with increased intensity
        base_colors = [
            (1, 0.3, 0.3),    # Lighter red
            (0.3, 1, 0.3),    # Lighter green
            (1, 1, 1),        # White
            (1, 1, 1)         # White
        ]
        
        # Set only the axes (image area) background to black
        self.ax.set_facecolor('black')
        
        # Display each visible channel
        for channel in range(4):
            if (self.channel_visible[channel] and 
                self.channel_data[channel] is not None):
                current_image = self.channel_data[channel][self.current_slice, :, :]
                
                # Calculate brightness/contrast limits
                img_min = np.min(current_image)
                img_max = np.max(current_image)
                
                # Calculate vmin and vmax, ensuring we don't get a zero range
                if img_min == img_max:
                    vmin = img_min
                    vmax = img_min + 1
                else:
                    vmin = img_min + (img_max - img_min) * self.channel_brightness[channel]['min']
                    vmax = img_min + (img_max - img_min) * self.channel_brightness[channel]['max']
                
                # Normalize the image safely
                if vmin == vmax:
                    normalized_image = np.zeros_like(current_image)
                else:
                    normalized_image = np.clip((current_image - vmin) / (vmax - vmin), 0, 1)
                
                # Create custom colormap with higher intensity
                color = base_colors[channel]
                custom_cmap = LinearSegmentedColormap.from_list(
                    f'custom_{channel}',
                    [(0,0,0,0), (*color,1)]
                )
                
                # Display the image with slightly higher alpha
                self.ax.imshow(normalized_image,
                             alpha=0.7,
                             cmap=custom_cmap,
                             vmin=0,
                             vmax=1)

        # Add highlight overlay if it exists
        if self.highlight_overlay is not None:
            highlight_slice = self.highlight_overlay[self.current_slice]
            highlight_cmap = LinearSegmentedColormap.from_list(
                'highlight',
                [(0, 0, 0, 0), (1, 1, 0, 0.7)]
            )
            self.ax.imshow(highlight_slice,
                         cmap=highlight_cmap,
                         alpha=0.5)
        
        # Restore zoom limits if they existed
        if current_xlim is not None and current_ylim is not None:
            self.ax.set_xlim(current_xlim)
            self.ax.set_ylim(current_ylim)
        
        # Style the axes
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title(f'Slice {self.current_slice}')

        # Make axis labels and ticks black for visibility against white background
        self.ax.xaxis.label.set_color('black')
        self.ax.yaxis.label.set_color('black')
        self.ax.title.set_color('black')
        self.ax.tick_params(colors='black')
        for spine in self.ax.spines.values():
            spine.set_color('black')

        # Adjust the layout to ensure the plot fits well in the figure
        self.figure.tight_layout()

        # Redraw measurement points and their labels
        for point in self.measurement_points:
            x1, y1, z1 = point['point1']
            x2, y2, z2 = point['point2']
            pair_idx = point['pair_index']
            
            # Draw points and labels if they're on current slice
            if z1 == self.current_slice:
                self.ax.plot(x1, y1, 'yo', markersize=8)
                self.ax.text(x1, y1+5, str(pair_idx), 
                            color='white', ha='center', va='bottom')
            if z2 == self.current_slice:
                self.ax.plot(x2, y2, 'yo', markersize=8)
                self.ax.text(x2, y2+5, str(pair_idx), 
                            color='white', ha='center', va='bottom')
                
            # Draw line if both points are on current slice
            if z1 == z2 == self.current_slice:
                self.ax.plot([x1, x2], [y1, y2], 'r--', alpha=0.5)
    
        
        self.canvas.draw()

    def show_netshow_dialog(self):
        dialog = NetShowDialog(self)
        dialog.exec()

    def show_partition_dialog(self):
        dialog = PartitionDialog(self)
        dialog.exec()




#TABLE RELATED: 
class SearchWidget(QWidget):
    """For using ctrl + F within a table"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.Popup)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search...")
        self.search_input.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.search_input)
        
        close_button = QPushButton("×")
        close_button.setFixedSize(20, 20)
        close_button.clicked.connect(self.hide)
        layout.addWidget(close_button)
        
        # Store the last searched value
        self.last_search = None
        
    def on_text_changed(self, text):
        if self.parent():
            try:
                value = int(text)
                self.last_search = value
            except ValueError:
                self.last_search = None
            
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.hide()
        elif event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            if self.last_search is not None:
                # Get the parent table view and main window
                table_view = self.parent()
                main_window = table_view.parent
                
                # Only search in the currently active table
                if table_view == main_window.active_table:
                    main_window.highlight_value_in_tables(self.last_search)
        else:
            super().keyPressEvent(event)

class CustomTableView(QTableView):
    """Modified pandas table that allows bolding and other fun stuff"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.search_widget = SearchWidget(self)
        self.search_widget.hide()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        self.parent = parent  # Store reference to parent window

    def keyPressEvent(self, event):
        # Check for Ctrl+F
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_F:
            # Position the search widget at the top-right corner of the table
            pos = self.rect().topRight()
            self.search_widget.move(self.mapToGlobal(pos) - QPoint(self.search_widget.width(), 0))
            self.search_widget.show()
            self.search_widget.search_input.setFocus()
        # If Enter is pressed and search widget is visible
        elif (event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter) and self.search_widget.isVisible():
            # Forward the enter key press to the search widget
            self.search_widget.keyPressEvent(event)
        else:
            super().keyPressEvent(event)

    def show_context_menu(self, position):
        # Get the index at the clicked position
        index = self.indexAt(position)
        
        if index.isValid():  # Only show menu if we clicked on a valid cell
            # Create context menu
            context_menu = QMenu(self)
            
            # Add Sort submenu for all tables
            if self.model() and hasattr(self.model(), '_data'):
                sort_menu = context_menu.addMenu("Sort")
                
                # Get column names from the DataFrame
                columns = self.model()._data.columns.tolist()
                
                # Create submenus for each column
                for col in columns:
                    col_menu = sort_menu.addMenu("Sort by: " + str(col))
                    
                    # Add sorting options
                    asc_action = col_menu.addAction("Low to High")
                    desc_action = col_menu.addAction("High to Low")
                    
                    # Connect actions
                    asc_action.triggered.connect(lambda checked, c=col: self.sort_table(c, ascending=True))
                    desc_action.triggered.connect(lambda checked, c=col: self.sort_table(c, ascending=False))
            
            # Different menus for top and bottom tables
            if self == self.parent.data_table:  # Top table
                save_menu = context_menu.addMenu("Save As")
                save_csv = save_menu.addAction("CSV")
                save_excel = save_menu.addAction("Excel")
                
                # Connect the actions
                save_csv.triggered.connect(lambda: self.save_table_as('csv'))
                save_excel.triggered.connect(lambda: self.save_table_as('xlsx'))
            else:  # Bottom tables
                # Add Find action
                find_menu = context_menu.addMenu("Find")
                find_action = find_menu.addAction("Find Node/Edge")
                find_pair_action = find_menu.addAction("Find Pair")
                find_action.triggered.connect(lambda: self.handle_find_action(
                    index.row(), index.column(), 
                    self.model()._data.iloc[index.row(), index.column()]
                ))
                find_pair_action.triggered.connect(lambda: self.handle_find_action(
                    [index.row()], [0,1,2],
                    [self.model()._data.iloc[index.row(), 0], self.model()._data.iloc[index.row(), 1], self.model()._data.iloc[index.row(), 2]]
                    ))
                
                # Add separator
                context_menu.addSeparator()
                
                # Add Save As menu
                save_menu = context_menu.addMenu("Save As")
                save_csv = save_menu.addAction("CSV")
                save_excel = save_menu.addAction("Excel")
                
                # Connect the actions - ensure we're saving the active table
                save_csv.triggered.connect(lambda: self.parent.active_table.save_table_as('csv'))
                save_excel.triggered.connect(lambda: self.parent.active_table.save_table_as('xlsx'))
            
            # Show the menu at cursor position
            cursor_pos = QCursor.pos()
            context_menu.exec(cursor_pos)

    def sort_table(self, column, ascending=True):
        """Sort the table by the specified column."""
        try:
            # Get the current DataFrame
            df = self.model()._data
            
            # Sort the DataFrame
            sorted_df = df.sort_values(by=column, ascending=ascending, na_position='last')
            
            # Create new model with sorted DataFrame
            new_model = PandasModel(sorted_df)
            
            # Preserve any bold formatting from the old model
            if hasattr(self.model(), 'bold_cells'):
                new_model.bold_cells = self.model().bold_cells
            
            # Set the new model
            self.setModel(new_model)
            
            # Adjust column widths
            for col in range(new_model.columnCount(None)):
                self.resizeColumnToContents(col)
                
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error sorting table: {str(e)}"
            )

    def save_table_as(self, file_type):
        """Save the table data as either CSV or Excel file."""
        if not self.model():
            return
            
        df = self.model()._data
        
        # Get table name for the file dialog title
        if self == self.parent.data_table:
            table_name = "Statistics"
        elif self == self.parent.network_table:
            table_name = "Network"
        else:
            table_name = "Selection"
        
        # Get save file name
        file_filter = "CSV Files (*.csv)" if file_type == 'csv' else "Excel Files (*.xlsx)"
        filename, _ = QFileDialog.getSaveFileName(
            self,
            f"Save {table_name} Table As",
            "",
            file_filter
        )
        
        if filename:
            try:
                if file_type == 'csv':
                    # If user didn't type extension, add .csv
                    if not filename.endswith('.csv'):
                        filename += '.csv'
                    df.to_csv(filename, index=False)
                else:
                    # If user didn't type extension, add .xlsx
                    if not filename.endswith('.xlsx'):
                        filename += '.xlsx'
                    df.to_excel(filename, index=False)
                    
                QMessageBox.information(
                    self,
                    "Success",
                    f"{table_name} table successfully saved to {filename}"
                )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Failed to save file: {str(e)}"
                )

    def handle_find_action(self, row, column, value):
        """Handle the Find action for bottom tables."""
        try:
            if type(column) is not list: #If highlighting one element
                value = int(value)
                
                # Get the currently active table
                active_table = self.parent.active_table
                
                # Determine if we're looking for a node or edge based on column
                if column < 2:  # First two columns are nodes
                    if value in my_network.node_centroids:
                        # Get centroid coordinates (Z, Y, X)
                        centroid = my_network.node_centroids[value]
                        # Set the active channel to nodes (0)
                        self.parent.set_active_channel(0)
                        # Toggle on the nodes channel if it's not already visible
                        if not self.parent.channel_visible[0]:
                            self.parent.channel_buttons[0].setChecked(True)
                            self.parent.toggle_channel(0)
                        # Navigate to the Z-slice
                        self.parent.slice_slider.setValue(int(centroid[0]))
                        print(f"Found node {value} at Z-slice {centroid[0]}")
                        self.parent.create_highlight_overlay(node_indices=[value])
                        self.parent.clicked_values['nodes'].append(value)
                        
                        # Highlight the value in both tables if it exists
                        self.highlight_value_in_table(self.parent.network_table, value, column)
                        self.highlight_value_in_table(self.parent.selection_table, value, column)
                    else:
                        print(f"Node {value} not found in centroids dictionary")
                        
                elif column == 2:  # Third column is edges
                    if value in my_network.edge_centroids:
                        # Get centroid coordinates (Z, Y, X)
                        centroid = my_network.edge_centroids[value]
                        # Set the active channel to edges (1)
                        self.parent.set_active_channel(1)
                        # Toggle on the edges channel if it's not already visible
                        if not self.parent.channel_visible[1]:
                            self.parent.channel_buttons[1].setChecked(True)
                            self.parent.toggle_channel(1)
                        # Navigate to the Z-slice
                        self.parent.slice_slider.setValue(int(centroid[0]))
                        print(f"Found edge {value} at Z-slice {centroid[0]}")
                        self.parent.create_highlight_overlay(edge_indices=[value])
                        self.parent.clicked_values['edges'].append(value)

                        # Highlight the value in both tables if it exists
                        self.highlight_value_in_table(self.parent.network_table, value, column)
                        self.highlight_value_in_table(self.parent.selection_table, value, column)
                    else:
                        print(f"Edge {value} not found in centroids dictionary")
            else: #If highlighting paired elements
                centroid1 = my_network.node_centroids[int(value[0])]
                centroid2 = my_network.node_centroids[int(value[1])]
                try:
                    centroid3 = my_network.edge_centroids[int(value[3])]
                except:
                    pass

                # Set the active channel to nodes (0)
                self.parent.set_active_channel(0)
                # Toggle on the nodes channel if it's not already visible
                if not self.parent.channel_visible[0]:
                    self.parent.channel_buttons[0].setChecked(True)
                    self.parent.toggle_channel(0)
                # Navigate to the Z-slice
                self.parent.slice_slider.setValue(int(centroid1[0]))
                print(f"Found node {value} at Z-slice {centroid1[0]}")
                try:
                    self.parent.create_highlight_overlay(node_indices=[int(value[0]), int(value[1])], edge_indices = int(value[2]))
                    self.parent.clicked_values['edges'].append(value[2])
                    self.parent.clicked_values['nodes'].append(value[0])
                    self.parent.clicked_values['nodes'].append(value[1])
                except:
                    self.parent.create_highlight_overlay(node_indices=[int(value[0]), int(value[1])])
                    self.parent.clicked_values['nodes'].append(value[0])
                    self.parent.clicked_values['nodes'].append(value[1])

        except (ValueError, TypeError) as e:
            print(f"Error processing value: {str(e)}")
            return
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return

    def highlight_value_in_table(self, table, value, column):
        """Helper method to find and highlight a value in a specific table."""
        if table.model() is None:
            return
            
        df = table.model()._data
        
        if column < 2:  # Node
            col1_matches = df[df.columns[0]] == value
            col2_matches = df[df.columns[1]] == value
            all_matches = col1_matches | col2_matches
        else:  # Edge
            all_matches = df[df.columns[2]] == value
        
        if all_matches.any():
            match_indices = all_matches[all_matches].index.tolist()
            row_idx = match_indices[0]
            
            # Only scroll and select if this is the active table
            if table == self.parent.active_table:
                # Create index and scroll to it
                model_index = table.model().index(row_idx, 0)
                table.scrollTo(model_index)
                
                # Select the row
                table.clearSelection()
                table.selectRow(row_idx)
                table.setCurrentIndex(model_index)
            
            # Update bold formatting
            table.model().set_bold_value(value, column < 2 and 0 or 1)


class PandasModel(QAbstractTableModel):
    """A pandas df table that can be displayed in the gui"""
    def __init__(self, data):
        super().__init__()
        if type(data) == list:
            data = self.lists_to_dataframe(data[0], data[1], data[2], column_names=['Node 1A', 'Node 1B', 'Edge 1C'])
        self._data = data
        self.bold_cells = set()  # Store (index, col) pairs that should be bold

    @staticmethod
    def lists_to_dataframe(list1, list2, list3, column_names=['Column1', 'Column2', 'Column3']):
        """
        Convert three lists into a pandas DataFrame with specified column names.
        
        Parameters:
        list1, list2, list3: Lists of equal length
        column_names: List of column names (default provided)
        
        Returns:
        pandas.DataFrame: DataFrame with three columns
        """
        df = pd.DataFrame({
            column_names[0]: list1,
            column_names[1]: list2,
            column_names[2]: list3
        })
        return df

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])
        return None

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        elif role == Qt.ItemDataRole.FontRole:
            # Get the actual index from the DataFrame for this row
            df_index = self._data.index[index.row()]
            if (df_index, index.column()) in self.bold_cells:
                font = QFont()
                font.setBold(True)
                return font
        return None
    
    def set_bold_value(self, value, active_channel=0):
        """Set bold formatting for cells containing this value in relevant columns based on active channel"""
        # Clear previous bold cells
        self.bold_cells.clear()
        
        if active_channel == 0:
            # For nodes, search first two columns
            for col in [0, 1]:
                matches = self._data.iloc[:, col] == value
                for idx in matches[matches].index:
                    self.bold_cells.add((idx, col))
        elif active_channel == 1:
            # For edges, only search third column
            matches = self._data.iloc[:, 2] == value
            for idx in matches[matches].index:
                self.bold_cells.add((idx, 2))
        
        # Emit signal to refresh the view
        self.layoutChanged.emit()

# Tables related for the data tables:

class TabCornerWidget(QWidget):
    """Widget for the corner of the tab widget, can be used to add controls"""
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)

class TabButton(QPushButton):
    """Custom close button for tabs"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(16, 16)
        self.setText("×")
        self.setStyleSheet("""
            QPushButton {
                border: none;
                color: gray;
                font-weight: bold;
                padding: 0px;
            }
            QPushButton:hover {
                color: red;
            }
        """)

class TabbedDataWidget(QTabWidget):
    """Widget that manages multiple data tables in tabs"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setElideMode(Qt.TextElideMode.ElideRight)
        
        # Store tables with their associated names
        self.tables = {}
        self.tabCloseRequested.connect(self.close_tab)
        
        # Set corner widget
        self.setCornerWidget(TabCornerWidget(self))
        
    def add_table(self, name, table_widget, switch_to=True):
        """Add a new table with the given name"""
        if name in self.tables:
            # If tab already exists, update its content
            idx = self.indexOf(self.tables[name])
            self.removeTab(idx)
            
        self.tables[name] = table_widget
        idx = self.addTab(table_widget, name)
        
        if switch_to:
            self.setCurrentIndex(idx)
            
        # Update parent's data_table reference
        if self.parent_window:
            self.parent_window.data_table = table_widget
            
    def close_tab(self, index):
        """Close the tab at the given index"""
        widget = self.widget(index)
        # Find and remove the table name from our dictionary
        name_to_remove = None
        for name, table in self.tables.items():
            if table == widget:
                name_to_remove = name
                break
                
        if name_to_remove:
            del self.tables[name_to_remove]
            
        self.removeTab(index)
        
        # Update parent's data_table reference to current table
        if self.parent_window and self.count() > 0:
            self.parent_window.data_table = self.currentWidget()
            
    def clear_all_tabs(self):
        """Remove all tabs"""
        while self.count() > 0:
            self.close_tab(0)
            
    def get_current_table(self):
        """Get the currently active table"""
        return self.currentWidget()


# IMAGE MENU RELATED

class BrightnessContrastDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Brightness/Contrast Controls")
        self.setModal(False)  # Allows interaction with main window while open
        
        layout = QVBoxLayout(self)
        
        # Create range sliders for each channel
        self.brightness_sliders = []
        for i in range(4):
            channel_widget = QWidget()
            channel_layout = QVBoxLayout(channel_widget)
            
            # Add label
            label = QLabel(f"Channel {i+1} Brightness/Contrast")
            channel_layout.addWidget(label)
            
            # Create range slider
            slider = QRangeSlider(Qt.Orientation.Horizontal)
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setValue((0, 100))
            slider.valueChanged.connect(lambda values, ch=i: self.parent().update_brightness(ch, values))
            self.brightness_sliders.append(slider)
            channel_layout.addWidget(slider)
            
            layout.addWidget(channel_widget)


    #def show_network(self, geometric = False, directory = None):

class Show3dDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Display Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)

        self.downsample = QLineEdit("1")
        layout.addRow("Downsample Factor (Expect Slowness on Large Images):", self.downsample)

        # Network Overlay checkbox (default True)
        self.overlay = QPushButton("Network Overlay")
        self.overlay.setCheckable(True)
        self.overlay.setChecked(True)
        layout.addRow("Include Network Overlay", self.overlay)
        
        # Add Run button
        run_button = QPushButton("Show 3D")
        run_button.clicked.connect(self.show_3d)
        layout.addWidget(run_button)


    def show_3d(self):

        try:
            
            # Get amount
            try:
                downsample = float(self.downsample.text()) if self.downsample.text() else 1
            except ValueError:
                downsample = 1

            overlay = self.overlay.isChecked()
            if overlay:
        
                # Example analysis plot
                my_network.show_3D(my_network.network_overlay, downsample)
            else:
                my_network.show_3D(down_factor = downsample)
            
            self.accept()

        except Exception as e:
            print(f"Error: {e}")


# ANALYZE MENU RELATED

class NetShowDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Display Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)
        
        # geo checkbox (default True)
        self.geo_layout = QPushButton("geo_layout")
        self.geo_layout.setCheckable(True)
        self.geo_layout.setChecked(False)
        layout.addRow("Use Geometric Layout:", self.geo_layout)
        
        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Default", "Community Coded (Uses current communities or label propogation by default if no communities have been found)", "Community Coded (Redo Label Propogation Algorithm)", "Community Coded (Redo Louvain Algorithm)", "Node ID Coded"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

        # weighted checkbox (default True)
        self.weighted = QPushButton("weighted")
        self.weighted.setCheckable(True)
        self.weighted.setChecked(True)
        layout.addRow("Use Weighted Network (Only for community graphs):", self.weighted)

        # Optional saving:
        self.directory = QLineEdit()
        self.directory.setPlaceholderText("Does not save when empty")
        layout.addRow("Output Directory:", self.directory)
        
        # Add Run button
        run_button = QPushButton("Show Network")
        run_button.clicked.connect(self.show_network)
        layout.addWidget(run_button)
    
    def show_network(self):
        # Get parameters and run analysis
        geo = self.geo_layout.isChecked()
        accepted_mode = self.mode_selector.currentIndex()  # Convert to 1-based index
        # Get directory (None if empty)
        directory = self.directory.text() if self.directory.text() else None

        weighted = self.weighted.isChecked()

        try:
            if accepted_mode == 0:
                my_network.show_network(geometric=geo, directory = directory)
            elif accepted_mode == 1:
                my_network.show_communities_flex(geometric=geo, directory = directory, weighted = weighted, partition = my_network.communities)
                self.parent().format_for_upperright_table(my_network.communities, 'NodeID', 'CommunityID')
            elif accepted_mode == 2:
                my_network.show_communities_flex(geometric=geo, directory = directory, weighted = weighted, partition = my_network.communities, style = 0)
                self.parent().format_for_upperright_table(my_network.communities, 'NodeID', 'CommunityID')
            elif accepted_mode ==3:
                my_network.show_communities_flex(geometric=geo, directory = directory, weighted = weighted, partition = my_network.communities, style = 1)
                self.parent().format_for_upperright_table(my_network.communities, 'NodeID', 'CommunityID')
            elif accepted_mode == 4:
                my_network.show_identity_network(geometric=geo, directory = directory)
            
            self.accept()
        except Exception as e:
            print(f"Error showing network: {e}")

class PartitionDialog(QDialog):
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Partition Parameters")
        self.setModal(True)

        layout = QFormLayout(self)

        # weighted checkbox (default True)
        self.weighted = QPushButton("weighted")
        self.weighted.setCheckable(True)
        self.weighted.setChecked(True)
        layout.addRow("Use Weighted Network:", self.weighted)

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Label Propogation", "Louvain"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

        # Add Run button
        run_button = QPushButton("Partition")
        run_button.clicked.connect(self.partition)
        layout.addWidget(run_button)

    def partition(self):

        accepted_mode = self.mode_selector.currentIndex()
        weighted = self.weighted.isChecked()

        try:
            my_network.community_partition(weighted = weighted, style = accepted_mode)
            print(f"Discovered communities: {my_network.communities}")

            self.parent().format_for_upperright_table(my_network.communities, 'NodeID', 'CommunityID')

            self.accept()

        except Exception as e:
            print(f"Error creating communities: {e}")





# PROCESS MENU RELATED:


class ResizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Resize Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)
        self.resize = QLineEdit()
        self.resize.setPlaceholderText("Will Override Below")
        layout.addRow("Resize Factor (All Dimensions):", self.resize)
        self.zsize = QLineEdit("1")
        layout.addRow("Resize Z Factor:", self.zsize)
        self.ysize = QLineEdit("1")
        layout.addRow("Resize Y Factor:", self.ysize)
        self.xsize = QLineEdit("1")
        layout.addRow("Resize X Factor:", self.xsize)


        # cubic checkbox (default False)
        self.cubic = QPushButton("Use Cubic Resize? (Will alter labels and require re-binarization -> labelling, but preserves shape better)")
        self.cubic.setCheckable(True)
        self.cubic.setChecked(False)
        layout.addRow("Use cubic algorithm:", self.cubic)
        
        
        run_button = QPushButton("Run Resize")
        run_button.clicked.connect(self.run_resize)
        layout.addRow(run_button)

    def reset_fields(self):
        """Reset all input fields to default values"""
        self.resize.clear()
        self.zsize.setText("1")
        self.xsize.setText("1")
        self.ysize.setText("1")

    def run_resize(self):
        try:
            # Get amount
            try:
                resize = float(self.resize.text()) if self.resize.text() else None
                zsize = float(self.zsize.text()) if self.zsize.text() else 1
                ysize = float(self.ysize.text()) if self.ysize.text() else 1
                xsize = float(self.xsize.text()) if self.xsize.text() else 1
            except ValueError as e:
                print(f"Invalid input value: {e}")
                self.reset_fields()
                return
            
            resize = resize if resize is not None else (zsize, ysize, xsize)
            
            # Get the shape from whichever array exists
            array_shape = None
            if my_network.nodes is not None:
                array_shape = my_network.nodes.shape
            elif my_network.edges is not None:
                array_shape = my_network.edges.shape
            elif my_network.network_overlay is not None:
                array_shape = my_network.network_overlay.shape
            elif my_network.id_overlay is not None:
                array_shape = my_network.id_overlay.shape
                
            if array_shape is None:
                QMessageBox.critical(self, "Error", "No valid array found to resize")
                self.reset_fields()
                return
                
            # Check if resize would result in valid dimensions
            if isinstance(resize, (int, float)):
                new_shape = tuple(int(dim * resize) for dim in array_shape)
            else:
                new_shape = tuple(int(dim * factor) for dim, factor in zip(array_shape, resize))
                
            if any(dim < 1 for dim in new_shape):
                QMessageBox.critical(self, "Error", f"Resize would result in invalid dimensions: {new_shape}")
                self.reset_fields()
                return

            cubic = self.cubic.isChecked()
            if cubic:
                order = 3
            else:
                order = 0
                
            # If checks pass, proceed with resize
            if my_network.nodes is not None:
                my_network.nodes = n3d.resize(my_network.nodes, resize, order)
            if my_network.edges is not None:
                my_network.edges = n3d.resize(my_network.edges, resize, order)
            if my_network.network_overlay is not None:
                my_network.network_overlay = n3d.resize(my_network.network_overlay, resize, order)
            if my_network.id_overlay is not None:
                my_network.id_overlay = n3d.resize(my_network.id_overlay, resize, order)
                
            # Resize highlight overlay if it exists
            parent_window = self.parent()
            if parent_window is not None and parent_window.highlight_overlay is not None:
                parent_window.highlight_overlay = n3d.resize(parent_window.highlight_overlay, resize, order)
                    
            self.parent().channel_data[0] = my_network.nodes
            self.parent().channel_data[1] = my_network.edges
            self.parent().channel_data[2] = my_network.network_overlay
            self.parent().channel_data[3] = my_network.id_overlay
            self.parent().update_display()
            self.reset_fields()
            self.accept()
            
        except Exception as e:
            print(f"Error during resize operation: {e}")
            self.reset_fields()
            QMessageBox.critical(self, "Error", f"Failed to resize: {str(e)}")


class BinarizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Binarize Active Channel?")
        self.setModal(True)
        
        layout = QFormLayout(self)

       # Add Run button
        run_button = QPushButton("Run Binarize")
        run_button.clicked.connect(self.run_binarize)
        layout.addRow(run_button)

    def run_binarize(self):

        # Get the active channel data from parent
        active_data = self.parent().channel_data[self.parent().active_channel]
        if active_data is None:
            raise ValueError("No active image selected")

        try:
            # Call watershed method with parameters
            result = n3d.binarize(
                active_data
                )

            # Update both the display data and the network object
            self.parent().channel_data[self.parent().active_channel] = result


            # Update the corresponding property in my_network
            setattr(my_network, network_properties[self.parent().active_channel], result)

            self.parent().update_display()
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running binarize: {str(e)}"
            )

class LabelDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Label Active Channel?")
        self.setModal(True)
        
        layout = QFormLayout(self)

       # Add Run button
        run_button = QPushButton("Run Label")
        run_button.clicked.connect(self.run_label)
        layout.addRow(run_button)

    def run_label(self):

        # Get the active channel data from parent
        active_data = self.parent().channel_data[self.parent().active_channel]
        if active_data is None:
            raise ValueError("No active image selected")

        try:
            # Call watershed method with parameters
            result, _ = n3d.label_objects(
                active_data
                )

            # Update both the display data and the network object
            self.parent().channel_data[self.parent().active_channel] = result


            # Update the corresponding property in my_network
            setattr(my_network, network_properties[self.parent().active_channel], result)

            self.parent().update_display()
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running label: {str(e)}"
            )




class DilateDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dilate Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)

        self.amount = QLineEdit("1")
        layout.addRow("Dilation Radius:", self.amount)

        if my_network.xy_scale is not None:
            xy_scale = f"{my_network.xy_scale}"
        else:
            xy_scale = "1"

        self.xy_scale = QLineEdit(xy_scale)
        layout.addRow("xy_scale:", self.xy_scale)

        if my_network.z_scale is not None:
            z_scale = f"{my_network.z_scale}"
        else:
            z_scale = "1"

        self.z_scale = QLineEdit(z_scale)
        layout.addRow("z_scale:", self.z_scale)

       # Add Run button
        run_button = QPushButton("Run Dilate")
        run_button.clicked.connect(self.run_dilate)
        layout.addRow(run_button)

    def run_dilate(self):
        try:
            
            # Get amount
            try:
                amount = float(self.amount.text()) if self.amount.text() else 1
            except ValueError:
                amount = 1

            try:
                xy_scale = float(self.xy_scale.text()) if self.xy_scale.text() else 1
            except ValueError:
                xy_scale = 1

            try:
                z_scale = float(self.z_scale.text()) if self.z_scale.text() else 1
            except ValueError:
                z_scale = 1
            
            # Get the active channel data from parent
            active_data = self.parent().channel_data[self.parent().active_channel]
            if active_data is None:
                raise ValueError("No active image selected")
            
            # Call dilate method with parameters
            result = n3d.dilate(
                active_data,
                amount,
                xy_scale = xy_scale,
                z_scale = z_scale,
            )

            # Update both the display data and the network object
            self.parent().channel_data[self.parent().active_channel] = result


            # Update the corresponding property in my_network
            setattr(my_network, network_properties[self.parent().active_channel], result)

            self.parent().update_display()
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running dilate: {str(e)}"
            )


class SkeletonizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Skeletonize Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)

        self.remove = QLineEdit("0")
        layout.addRow("Remove Branches Pixel Length (int):", self.remove)

       # Add Run button
        run_button = QPushButton("Run Skeletonize")
        run_button.clicked.connect(self.run_skeletonize)
        layout.addRow(run_button)

    def run_skeletonize(self):
        try:
            
            # Get branch removal
            try:
                remove = int(self.remove.text()) if self.remove.text() else 0
            except ValueError:
                remove = 0
            
            # Get the active channel data from parent
            active_data = self.parent().channel_data[self.parent().active_channel]
            if active_data is None:
                raise ValueError("No active image selected")
            
            # Call dilate method with parameters
            result = n3d.skeletonize(
                active_data
            )

            if remove > 0:
                result = n3d.remove_branches(result, remove)


            # Update both the display data and the network object
            self.parent().channel_data[self.parent().active_channel] = result


            # Update the corresponding property in my_network
            setattr(my_network, network_properties[self.parent().active_channel], result)

            self.parent().update_display()
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running skeletonize: {str(e)}"
            )   


class WatershedDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Watershed Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)
        
        # Directory (empty by default)
        self.directory = QLineEdit()
        self.directory.setPlaceholderText("Leave empty for None")
        layout.addRow("Output Directory:", self.directory)
        
        # Proportion (default 0.1)
        self.proportion = QLineEdit("0.1")
        layout.addRow("Proportion:", self.proportion)
        
        # GPU checkbox (default True)
        self.gpu = QPushButton("GPU")
        self.gpu.setCheckable(True)
        self.gpu.setChecked(True)
        layout.addRow("Use GPU:", self.gpu)
        
        # Smallest radius (empty by default)
        self.smallest_rad = QLineEdit()
        self.smallest_rad.setPlaceholderText("Leave empty for None")
        layout.addRow("Smallest Radius:", self.smallest_rad)
        
        # Predownsample (empty by default)
        self.predownsample = QLineEdit()
        self.predownsample.setPlaceholderText("Leave empty for None")
        layout.addRow("Smart Dilate GPU Downsample:", self.predownsample)
        
        # Predownsample2 (empty by default)
        self.predownsample2 = QLineEdit()
        self.predownsample2.setPlaceholderText("Leave empty for None")
        layout.addRow("Smart Label GPU Downsample:", self.predownsample2)
        
        # Add Run button
        run_button = QPushButton("Run Watershed")
        run_button.clicked.connect(self.run_watershed)
        layout.addRow(run_button)

    def run_watershed(self):
        try:
            # Get directory (None if empty)
            directory = self.directory.text() if self.directory.text() else None
            
            # Get proportion (0.1 if empty or invalid)
            try:
                proportion = float(self.proportion.text()) if self.proportion.text() else 0.1
            except ValueError:
                proportion = 0.1
            
            # Get GPU state
            gpu = self.gpu.isChecked()
            
            # Get smallest_rad (None if empty)
            try:
                smallest_rad = float(self.smallest_rad.text()) if self.smallest_rad.text() else None
            except ValueError:
                smallest_rad = None
            
            # Get predownsample (None if empty)
            try:
                predownsample = float(self.predownsample.text()) if self.predownsample.text() else None
            except ValueError:
                predownsample = None
            
            # Get predownsample2 (None if empty)
            try:
                predownsample2 = float(self.predownsample2.text()) if self.predownsample2.text() else None
            except ValueError:
                predownsample2 = None
            
            # Get the active channel data from parent
            active_data = self.parent().channel_data[self.parent().active_channel]
            if active_data is None:
                raise ValueError("No active image selected")
            
            # Call watershed method with parameters
            result = n3d.watershed(
                active_data,
                directory=directory,
                proportion=proportion,
                GPU=gpu,
                smallest_rad=smallest_rad,
                predownsample=predownsample,
                predownsample2=predownsample2
            )

            # Update both the display data and the network object
            self.parent().channel_data[self.parent().active_channel] = result


            # Update the corresponding property in my_network
            setattr(my_network, network_properties[self.parent().active_channel], result)

            self.parent().update_display()
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running watershed: {str(e)}"
            )




class GenNodesDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Nodes from Edge Vertices")
        self.setModal(True)

        layout = QFormLayout(self)

        self.branch_removal = QLineEdit("0")
        layout.addRow("Skeleton Voxel Branch Length to Remove (int) (Compensates for spines off medial axis):", self.branch_removal)

        self.max_vol = QLineEdit("0")
        layout.addRow("Maximum Voxel Volume of Vertices to Retain (int - Compensates for skeleton looping):", self.max_vol)

        self.comp_dil = QLineEdit("0")
        layout.addRow("Voxel distance to merge nearby nodes (Int - compensates for multi-branch identification along thick branch regions):", self.comp_dil)

        self.down_factor = QLineEdit("0")
        layout.addRow("Downsample Factor (Speeds up calculation at the cost of fidelity):", self.down_factor)

        self.directory = QLineEdit()
        self.directory.setPlaceholderText("Leave empty to save in active dir")
        layout.addRow("Output Directory:", self.directory)

        # Add Run button
        run_button = QPushButton("Run Node Generation")
        run_button.clicked.connect(self.run_gennodes)
        layout.addRow(run_button)

    def run_gennodes(self):

        try:
            # Get directory (None if empty)
            directory = self.directory.text() if self.directory.text() else None
            
            # Get branch_removal
            try:
                branch_removal = int(self.branch_removal.text()) if self.branch_removal.text() else 0
            except ValueError:
                branch_removal = 0
                
            # Get max_vol
            try:
                max_vol = int(self.max_vol.text()) if self.max_vol.text() else 0
            except ValueError:
                max_vol = 0
            
            # Get comp_dil
            try:
                comp_dil = int(self.comp_dil.text()) if self.comp_dil.text() else 0
            except ValueError:
                comp_dil = 0
                
            # Get down_factor
            try:
                down_factor = int(self.down_factor.text()) if self.down_factor.text() else 0
            except ValueError:
                down_factor = 0
                
            # Get down_factor value (None if empty)
            try:
                down_factor = int(self.down_factor.text()) if self.down_factor.text() else None
            except ValueError:
                down_factor = None

            
            result = n3d.label_vertices(
                my_network.edges,
                max_vol=max_vol,
                branch_removal=branch_removal,
                comp_dil=comp_dil,
                down_factor=down_factor,

            )

            if directory is None:
                filename = f'labelled_vertices.tif'
            else:
                filename = f'{directory}/labelled_vertices.tif'

            import tifffile     
            tifffile.imwrite(filename, result, photometric='minisblack')
            print(f"Broken skeleton saved to {filename}")


            print(self.parent().channel_data[0])
            # Update both the display data and the network object

            # Update the corresponding property in my_network
            setattr(my_network, network_properties[0], result)

            self.parent().channel_data[0] = my_network.nodes

            # Enable the channel button
            self.parent().channel_buttons[0].setEnabled(True)
            self.parent().delete_buttons[0].setEnabled(True) 

            self.parent().update_display()
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running watershed: {str(e)}"
            )


class CentroidDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculate Centroids")
        self.setModal(True)

        layout = QFormLayout(self)

        self.directory = QLineEdit()
        self.directory.setPlaceholderText("Leave empty for active directory")
        layout.addRow("Output Directory:", self.directory)

        self.downsample = QLineEdit("1")
        layout.addRow("Downsample Factor:", self.downsample)

        # Add Run button
        run_button = QPushButton("Run Calculate Centroids")
        run_button.clicked.connect(self.run_centroids)
        layout.addRow(run_button)

    def run_centroids(self):

        try:
            # Get directory (None if empty)
            directory = self.directory.text() if self.directory.text() else None
            
            # Get downsample
            try:
                downsample = float(self.downsample.text()) if self.downsample.text() else 1
            except ValueError:
                downsample = 1

            # Get the active channel data from parent
            chan = self.parent().active_channel

            if chan == 0:
                my_network.calculate_node_centroids(
                    down_factor = downsample
                )
                my_network.save_node_centroids(directory = directory)

            elif chan == 1:
                my_network.calculate_edge_centroids(
                    down_factor = downsample
                )
                my_network.save_edge_centroids(directory = directory)


            self.parent().update_display()
            self.accept()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error finding centroids: {str(e)}"
            )





class CalcAllDialog(QDialog):
    # Class variables to store previous settings
    prev_directory = ""
    prev_xy_scale = "1"
    prev_z_scale = "1"
    prev_search = ""
    prev_diledge = ""
    prev_down_factor = ""
    prev_GPU_downsample = ""
    prev_other_nodes = ""
    prev_remove_trunk = ""
    prev_gpu = True
    prev_label_nodes = True
    prev_inners = True
    prev_skeletonize = False
    prev_overlays = True
    prev_updates = True

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculate All Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)
        
        # Directory (empty by default)
        self.directory = QLineEdit(self.prev_directory)
        self.directory.setPlaceholderText("Leave empty for 'my_network'")
        layout.addRow("Output Directory:", self.directory)
        
        # Load previous values for all inputs
        self.xy_scale = QLineEdit(self.prev_xy_scale)
        layout.addRow("xy_scale:", self.xy_scale)
        
        self.z_scale = QLineEdit(self.prev_z_scale)
        layout.addRow("z_scale:", self.z_scale)

        self.search = QLineEdit(self.prev_search)
        self.search.setPlaceholderText("Leave empty for None")
        layout.addRow("Node Search (float):", self.search)

        self.diledge = QLineEdit(self.prev_diledge)
        self.diledge.setPlaceholderText("Leave empty for None")
        layout.addRow("Edge Reconnection Distance (int):", self.diledge)

        self.down_factor = QLineEdit(self.prev_down_factor)
        self.down_factor.setPlaceholderText("Leave empty for None")
        layout.addRow("Downsample for Centroids (int):", self.down_factor)

        self.GPU_downsample = QLineEdit(self.prev_GPU_downsample)
        self.GPU_downsample.setPlaceholderText("Leave empty for None")
        layout.addRow("Downsample for Distance Transform (GPU) (int):", self.GPU_downsample)

        self.other_nodes = QLineEdit(self.prev_other_nodes)
        self.other_nodes.setPlaceholderText("Leave empty for None")
        layout.addRow("Filepath or directory containing additional node images:", self.other_nodes)

        self.remove_trunk = QLineEdit(self.prev_remove_trunk)
        self.remove_trunk.setPlaceholderText("Leave empty for 0")
        layout.addRow("Times to remove edge trunks (int): ", self.remove_trunk)

        # Load previous button states
        self.gpu = QPushButton("GPU")
        self.gpu.setCheckable(True)
        self.gpu.setChecked(self.prev_gpu)
        layout.addRow("Use GPU:", self.gpu)

        self.label_nodes = QPushButton("Label")
        self.label_nodes.setCheckable(True)
        self.label_nodes.setChecked(self.prev_label_nodes)
        layout.addRow("Label Nodes:", self.label_nodes)

        self.inners = QPushButton("Inner Edges")
        self.inners.setCheckable(True)
        self.inners.setChecked(self.prev_inners)
        layout.addRow("Use Inner Edges:", self.inners)

        self.skeletonize = QPushButton("Skeletonize")
        self.skeletonize.setCheckable(True)
        self.skeletonize.setChecked(self.prev_skeletonize)
        layout.addRow("Skeletonize Edges:", self.skeletonize)

        self.overlays = QPushButton("Overlays")
        self.overlays.setCheckable(True)
        self.overlays.setChecked(self.prev_overlays)
        layout.addRow("Generate Overlays:", self.overlays)

        self.update = QPushButton("Update")
        self.update.setCheckable(True)
        self.update.setChecked(self.prev_updates)
        layout.addRow("Update Node/Edge in NetTracer3D:", self.update)
        
        # Add Run button
        run_button = QPushButton("Run Calculate All")
        run_button.clicked.connect(self.run_calc_all)
        layout.addRow(run_button)

    def run_calc_all(self):

        try:
            # Get directory (None if empty)
            directory = self.directory.text() if self.directory.text() else None
            
            # Get xy_scale and z_scale (1 if empty or invalid)
            try:
                xy_scale = float(self.xy_scale.text()) if self.xy_scale.text() else 1
            except ValueError:
                xy_scale = 1
                
            try:
                z_scale = float(self.z_scale.text()) if self.z_scale.text() else 1
            except ValueError:
                z_scale = 1
            
            # Get search value (None if empty)
            try:
                search = float(self.search.text()) if self.search.text() else None
            except ValueError:
                search = None
                
            # Get diledge value (None if empty)
            try:
                diledge = int(self.diledge.text()) if self.diledge.text() else None
            except ValueError:
                diledge = None
                
            # Get down_factor value (None if empty)
            try:
                down_factor = int(self.down_factor.text()) if self.down_factor.text() else None
            except ValueError:
                down_factor = None
                
            # Get GPU_downsample value (None if empty)
            try:
                GPU_downsample = int(self.GPU_downsample.text()) if self.GPU_downsample.text() else None
            except ValueError:
                GPU_downsample = None
                
            # Get other_nodes path (None if empty)
            other_nodes = self.other_nodes.text() if self.other_nodes.text() else None
            
            # Get remove_trunk value (0 if empty)
            try:
                remove_trunk = int(self.remove_trunk.text()) if self.remove_trunk.text() else 0
            except ValueError:
                remove_trunk = 0
                
            # Get button states
            gpu = self.gpu.isChecked()
            label_nodes = self.label_nodes.isChecked()
            inners = self.inners.isChecked()
            skeletonize = self.skeletonize.isChecked()
            overlays = self.overlays.isChecked()
            update = self.update.isChecked()

            if not update:
                temp_nodes = my_network.nodes.copy()
                temp_edges = my_network.edges.copy()
            
            my_network.calculate_all(
                my_network.nodes,
                my_network.edges,
                directory=directory,
                xy_scale=xy_scale,
                z_scale=z_scale,
                search=search,
                diledge=diledge,
                down_factor=down_factor,
                GPU_downsample=GPU_downsample,
                other_nodes=other_nodes,
                remove_trunk=remove_trunk,
                GPU=gpu,
                label_nodes=label_nodes,
                inners=inners,
                skeletonize=skeletonize
            )

            # Store current values as previous values
            CalcAllDialog.prev_directory = self.directory.text()
            CalcAllDialog.prev_xy_scale = self.xy_scale.text()
            CalcAllDialog.prev_z_scale = self.z_scale.text()
            CalcAllDialog.prev_search = self.search.text()
            CalcAllDialog.prev_diledge = self.diledge.text()
            CalcAllDialog.prev_down_factor = self.down_factor.text()
            CalcAllDialog.prev_GPU_downsample = self.GPU_downsample.text()
            CalcAllDialog.prev_other_nodes = self.other_nodes.text()
            CalcAllDialog.prev_remove_trunk = self.remove_trunk.text()
            CalcAllDialog.prev_gpu = self.gpu.isChecked()
            CalcAllDialog.prev_label_nodes = self.label_nodes.isChecked()
            CalcAllDialog.prev_inners = self.inners.isChecked()
            CalcAllDialog.prev_skeletonize = self.skeletonize.isChecked()
            CalcAllDialog.prev_overlays = self.overlays.isChecked()
            CalcAllDialog.prev_updates = self.update.isChecked()


            # Update both the display data and the network object
            if update:
                self.parent().channel_data[0] = my_network.nodes
                self.parent().channel_data[1] = my_network.edges
            else:
                my_network.nodes = temp_nodes.copy()
                del temp_nodes
                my_network.edges = temp_edges.copy()
                del temp_edges
                self.parent().channel_data[0] = my_network.nodes
                self.parent().channel_data[1] = my_network.edges


            # Then handle overlays
            if overlays:
                if directory is None:
                    directory = 'my_network'
                
                # Generate and update overlays
                my_network.network_overlay = my_network.draw_network(directory=directory)
                my_network.id_overlay = my_network.draw_node_indices(directory=directory)
                
                # Update channel data
                self.parent().channel_data[2] = my_network.network_overlay
                self.parent().channel_data[3] = my_network.id_overlay
                
                # Enable the overlay channel buttons
                self.parent().channel_buttons[2].setEnabled(True)
                self.parent().channel_buttons[3].setEnabled(True)


            self.parent().update_display()
            self.accept()

            # Display network_lists in the network table
            try:
                if hasattr(my_network, 'network_lists'):
                    model = PandasModel(my_network.network_lists)
                    self.parent().network_table.setModel(model)
                    # Adjust column widths to content
                    for column in range(model.columnCount(None)):
                        self.parent().network_table.resizeColumnToContents(column)
            except Exception as e:
                print(f"Error loading network_lists: {e}")

            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running calculate all: {str(e)}"
            )







if __name__ == '__main__':
    global my_network
    my_network = n3d.Network_3D()
    global network_properties
    # Update the corresponding network property based on active channel
    network_properties = {
        0: 'nodes',
        1: 'edges',
        2: 'network_overlay',
        3: 'id_overlay'
    }

    app = QApplication(sys.argv)
    window = ImageViewerWindow()
    window.show()
    sys.exit(app.exec())