import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QLineEdit, QPushButton, QGraphicsTextItem, QGraphicsEllipseItem, QGraphicsLineItem, QVBoxLayout, QWidget
from PyQt5.QtGui import QBrush, QColor

class MindMapApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mind Map Creator")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.view.setSceneRect(0, 0, 800, 600)

        self.node_text = QLineEdit(self)
        self.add_node_button = QPushButton("Add Node", self)
        self.add_node_button.clicked.connect(self.add_node)

        self.add_line_button = QPushButton("Add Line", self)
        self.add_line_button.clicked.connect(self.add_line)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.view)
        self.layout.addWidget(self.node_text)
        self.layout.addWidget(self.add_node_button)
        self.layout.addWidget(self.add_line_button)

        self.nodes = []  # Store created nodes

        # Store the currently selected nodes for adding lines
        self.selected_nodes = []

    def add_node(self):
        node_text = self.node_text.text()
        if node_text:
            node = QGraphicsEllipseItem(0, 0, 100, 50)
            node.setFlag(QGraphicsEllipseItem.ItemIsMovable)
            text_item = QGraphicsTextItem(node_text, node)
            text_item.setPos(25, 15)

            node.setAcceptHoverEvents(True)
            node.hoverEnterEvent = lambda event, node=node: self.node_hover_enter(node)
            node.hoverLeaveEvent = lambda event, node=node: self.node_hover_leave(node)

            self.scene.addItem(node)
            self.nodes.append(node)
            self.node_text.clear()

    def node_hover_enter(self, node):
        if node not in self.selected_nodes:
            node.setBrush(QBrush(QColor("orange")))

    def node_hover_leave(self, node):
        if node not in self.selected_nodes:
            node.setBrush(QBrush(QColor("white")))

    def add_line(self):
        if len(self.selected_nodes) == 2:
            # If exactly two nodes are selected, draw a line between them
            node1, node2 = self.selected_nodes
            line = QGraphicsLineItem(node1.pos().x() + 50, node1.pos().y() + 50,
                                     node2.pos().x() + 50, node2.pos().y())
            self.scene.addItem(line)

            # Clear selection and reset node colors
            for node in self.selected_nodes:
                node.setBrush(QBrush(QColor("white")))
            self.selected_nodes = []

    def mousePressEvent(self, event):
        item = self.scene.itemAt(event.pos(), self.view.transform())
        if isinstance(item, QGraphicsEllipseItem):
            if item not in self.selected_nodes:
                self.selected_nodes.append(item)
                item.setBrush(QBrush(QColor("yellow")))
            if len(self.selected_nodes) > 2:
                # If more than two nodes are selected, reset selection
                for node in self.selected_nodes:
                    node.setBrush(QBrush(QColor("white")))
                self.selected_nodes = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mind_map_app = MindMapApp()
    mind_map_app.show()
    sys.exit(app.exec_())
