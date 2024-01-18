import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QTreeWidgetItem
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QColor

class CustumTree(QtWidgets.QTreeWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setDragEnabled(True)  # Added missing parentheses
        self.setHeaderHidden(True)  # Optional: Hide the header for simplicity
        self.setColumnCount(1)  # Optional: Set the number of columns
        self.itemClicked.connect(self.create)
    
    def create(self,item,collumn):
        print("ok123")

class Item(QtWidgets.QGraphicsItem):
    def __init__(self,parent,name):
        
        text_item = QtWidgets.QGraphicsTextItem(name, self)
        text_item.setPos(25, 15)

class GraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(GraphicsView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.image_path = None  # to save the path of the image


class GraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self,parent):
        super(GraphicsScene, self).__init__(parent)

        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("flowAPP")
        self.resize(1000, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.lib_list = CustumTree(self)    
        self.func_group = QtWidgets.QGroupBox(self)


        self.scene = GraphicsScene(self)
        self.view = GraphicsView(self.scene)

        self.layout = QtWidgets.QGridLayout(self.central_widget)
        self.layout.addWidget(self.lib_list,0,0,5,2)
        self.layout.addWidget(self.func_group,5,0,5,2)
        self.layout.addWidget(self.view,0,3,10,7)

        self.compoent = []
    

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
