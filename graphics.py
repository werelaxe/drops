from PyQt5.QtGui import QPainter
import model


def draw_circle(circle: model.Circle, qp: QPainter):
    print(circle.coords[0] - circle.radius,
                   circle.coords[1] - circle.radius,
                   circle.radius, circle.radius)
    qp.drawEllipse(circle.coords[0] - circle.radius,
                   circle.coords[1] - circle.radius,
                   circle.radius, circle.radius)


def draw_drop(drop: model.Drop, qp: QPainter):
    for circle in drop.circles:
        draw_circle(circle, qp)


def draw_model(model: model.Model, qp: QPainter):
    model.print_model()
    for drop in model.drops:
        draw_drop(drop, qp)
