from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt

class CircleLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = [(100, 100), (200, 150), (300, 200)]  # Kırmızı dairelerin başlangıç konumları
        self.dragging = False
        self.dragged_circle = None

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        pos = event.pos()
        for i, circle_pos in enumerate(self.circles):
            circle_center = self.calculate_circle_center(circle_pos)
            if self.is_point_in_circle(pos, circle_center):
                self.dragging = True
                self.dragged_circle = i
                break

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if self.dragging and self.dragged_circle is not None:
            self.circles[self.dragged_circle] = (event.pos().x(), event.pos().y())
            self.repaint()

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if self.dragging and self.dragged_circle is not None:
            circle_pos = self.circles[self.dragged_circle]
            self.print_circle_coordinates(self.dragged_circle, circle_pos)
        self.dragging = False
        self.dragged_circle = None

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for circle_pos in self.circles:
            circle_center = self.calculate_circle_center(circle_pos)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QColor(255, 0, 0, 100))  # Şeffaflık değeri (100) ekleniyor
            painter.setOpacity(0.5)  # Şeffaflık değeri (0.5) ayarlanıyor
            painter.drawEllipse(circle_center[0] - 20, circle_center[1] - 20, 40, 40)

    def calculate_circle_center(self, pos):
        return (pos[0] + 20, pos[1] + 20)

    def is_point_in_circle(self, point, center):
        distance_squared = (point.x() - center[0]) ** 2 + (point.y() - center[1]) ** 2
        return distance_squared <= 20 ** 2

    def print_circle_coordinates(self, circle_index, circle_pos):
        print(f"Kırmızı daire {circle_index + 1}: Koordinatlar ({circle_pos[0]}, {circle_pos[1]})")

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("STAMPIX")

        self.label = CircleLabel(self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        pixmap = QPixmap("D:/pythonProject/tofas/door-inner-panel.jpg")
        self.label.setPixmap(pixmap)

        self.resize(pixmap.width(), pixmap.height())  # Pencere boyutunu görüntü boyutuna ayarla

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
