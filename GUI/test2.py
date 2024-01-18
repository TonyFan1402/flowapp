from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget
import sys

class MyTreeWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        
        # Create some items
        item1 = QTreeWidgetItem(self)
        item1.setText(0, "Item 1")

        item2 = QTreeWidgetItem(self)
        item2.setText(0, "Item 2")

        item3 = QTreeWidgetItem(self)
        item3.setText(0, "Item 3")

        # Connect the itemClicked signal to the on_item_clicked method
        self.itemClicked.connect(self.on_item_clicked)

    def on_item_clicked(self, item, column):
        # This method will be called when any item is clicked
        print(f"Item clicked: {item.text(column)}")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout and set it for the main window
        layout = QVBoxLayout(self)

        # Create the custom QTreeWidget
        tree_widget = MyTreeWidget()

        # Add the tree widget to the layout
        layout.addWidget(tree_widget)

        # Set the layout for the main window
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
