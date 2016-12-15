from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPainter
import model


def draw_circle(circle: model.Circle, qp: QPainter, alpha: float):
    qp.setBrush(QColor(alpha * 256, 0, 0))
    qp.setPen(QColor(alpha * 256, 0, 0))
    qp.drawEllipse(circle.coords[0] - circle.radius,
                   circle.coords[1] - circle.radius,
                   circle.radius, circle.radius)


def draw_drop(drop: model.Drop, qp: QPainter):
    size = len(drop.circles)
    for index in range(size):
        circle = drop.circles[index]
        draw_circle(circle, qp, index / size)


def draw_model(model: model.Model, qp: QPainter):
    # model.print_model()
    for drop in model.drops:
        draw_drop(drop, qp)
