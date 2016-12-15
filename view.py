import sys, random
import graphics
import model
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 800
        self.height = 600
        self.initUI()
        self.model = model.Model()

    def initUI(self):
        self.setGeometry(800 - self.width // 2, 450 - self.height // 2,
                         self.width, self.height)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_model(qp)
        qp.end()

    def draw_model(self, qp: QPainter):
        qp.setBrush(Qt.black)
        qp.drawRect(0, 0, self.width, self.height)
        qp.setBrush(Qt.red)
        qp.setPen(Qt.red)
        graphics.draw_model(self.model, qp)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Control:
            self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())