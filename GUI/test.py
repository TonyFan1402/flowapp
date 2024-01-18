import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsLineItem
from PyQt5.QtCore import Qt, QPointF

class MyView(QGraphicsView):
    def __init__(self, scene):
        super(MyView, self).__init__(scene)
        self.setScene(scene)
        self.line_item = None
        self.start_point = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = self.mapToScene(event.pos())
            self.line_item = QGraphicsLineItem()
            self.line_item.setLine(self.start_point.x(), self.start_point.y(),
                                    self.start_point.x(), self.start_point.y())
            self.scene().addItem(self.line_item)

    def mouseMoveEvent(self, event):
        if self.line_item is not None:
            end_point = self.mapToScene(event.pos())
            
            # Calculate the difference between start and end points
            dx = end_point.x() - self.start_point.x()
            dy = end_point.y() - self.start_point.y()
            
            # Adjust the end point to form a 90-degree angle
            if abs(dx) > abs(dy):
                end_point.setY(self.start_point.y())
            else:
                end_point.setX(self.start_point.x())
            
            self.line_item.setLine(self.start_point.x(), self.start_point.y(),
                                    end_point.x(), end_point.y())

    def mouseReleaseEvent(self, event):
        if self.line_item is not None:
            self.line_item = None

def main():
    app = QApplication(sys.argv)
    scene = QGraphicsScene()
    view = MyView(scene)

    # Show the view
    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
