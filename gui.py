import sys
import main
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

MAX_X = 700
MAX_Y = 700
RADIUS = 4


class Circle:

    def __init__(self, x, y, color, radius=RADIUS):
        """Circle class"""
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def if_clicked(self, pos_x, pos_y):
        """Returns True if circle was clicked, False otherwise"""
        if (pos_x - self.x) ** 2 + (pos_y - self.y) ** 2 <= self.radius ** 2:
            return True
        return False


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.c1 = False
        self.c2 = False
        self.add = False
        self.x_training_sample = []
        self.y_training_sample = []
        self.circles = []

        self.setWindowTitle('Binary classification')
        self.mousePressEvent = self.mouseMoveEvent
        self.setObjectName("main_window")
        self.resize(958, 811)
        self.setStyleSheet("background-color: rgb(0, 123, 180);")

        self.title_frame = QFrame(self)
        self.title_frame.setGeometry(QRect(740, 10, 191, 51))
        self.title_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.title_frame.setObjectName("title_frame")

        self.title_label = QLabel(self.title_frame)
        self.title_label.setGeometry(QRect(10, 10, 181, 31))
        self.title_label.setStyleSheet("font: 13pt \"Sitka Text\";\n"
                                       "text-align: center;")
        self.title_label.setObjectName("title_label")

        self.c1_add_button = QPushButton(self)
        self.c1_add_button.setGeometry(QRect(760, 120, 151, 41))
        self.c1_add_button.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                         "font: 11pt \"Sitka Text\";\n"
                                         "text-align: center;\n"
                                         "border-radius: 10;\n"
                                         "border: 2px solid black;")
        self.c1_add_button.setObjectName("c1_add_button")
        self.c1_add_button.clicked.connect(self.add_c1)

        self.c2_add_button = QPushButton(self)
        self.c2_add_button.setGeometry(QRect(760, 190, 151, 41))
        self.c2_add_button.setStyleSheet("background-color: rgb(125, 255, 212);\n"
                                         "font: 11pt \"Sitka Text\";\n"
                                         "text-align: center;\n"
                                         "border-radius: 10;\n"
                                         "border: 2px solid black;")
        self.c2_add_button.setObjectName("c2_add_button")
        self.c2_add_button.clicked.connect(self.add_c2)

        self.result_frame = QFrame(self)
        self.result_frame.setGeometry(QRect(10, 730, 271, 61))
        self.result_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.result_frame.setFrameShape(QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QFrame.Raised)
        self.result_frame.setObjectName("result_frame")

        self.result_label = QLabel(self.result_frame)
        self.result_label.setGeometry(QRect(10, 10, 251, 31))
        self.result_label.setStyleSheet("font: 13pt \"Sitka Text\";\n"
                                        "text-align: center;")
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")

        self.classify_point_button = QPushButton(self)
        self.classify_point_button.setGeometry(QRect(740, 480, 191, 61))
        self.classify_point_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 11pt \"Sitka Text\";\n"
                                                 "text-align: center;\n"
                                                 "border-radius: 10;\n"
                                                 "border: 2px solid black;")
        self.classify_point_button.setObjectName("classify_point_button")
        self.classify_point_button.clicked.connect(self.set_classify)

        self.clear_scene_button = QPushButton(self)
        self.clear_scene_button.setGeometry(QRect(760, 260, 151, 41))
        self.clear_scene_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "font: 11pt \"Sitka Text\";\n"
                                              "text-align: center;\n"
                                              "border-radius: 10;\n"
                                              "border: 2px solid black;")
        self.clear_scene_button.setObjectName("clear_scene_button")
        self.clear_scene_button.clicked.connect(self.clear_scene)

        self.import_button = QPushButton(self)
        self.import_button.setGeometry(QRect(310, 740, 151, 41))
        self.import_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "font: 11pt \"Sitka Text\";\n"
                                         "text-align: center;\n"
                                         "border-radius: 10;\n"
                                         "border: 2px solid black;")
        self.import_button.setObjectName("import_button")
        self.import_button.clicked.connect(self.import_scene)

        self.export_button = QPushButton(self)
        self.export_button.setGeometry(QRect(490, 740, 151, 41))
        self.export_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "font: 11pt \"Sitka Text\";\n"
                                         "text-align: center;\n"
                                         "border-radius: 10;\n"
                                         "border: 2px solid black;")
        self.export_button.setObjectName("export_button")
        self.export_button.clicked.connect(self.export_scene)

        self.exit_button = QPushButton(self)
        self.exit_button.setGeometry(QRect(760, 740, 151, 41))
        self.exit_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 11pt \"Sitka Text\";\n"
                                       "text-align: center;\n"
                                       "border-radius: 10;\n"
                                       "border: 2px solid black;")
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.stop_alg)

        self.title_label.setText("Binary Classification")
        self.c1_add_button.setText("C1 type point")
        self.c2_add_button.setText("C2 type point")
        self.classify_point_button.setText("Classify Point")
        self.clear_scene_button.setText("Clear Scene")
        self.import_button.setText("Import Scene")
        self.export_button.setText("Export Scene")
        self.exit_button.setText("Exit")
        self.show()

    def add_c1(self):
        self.c1 = True
        self.c2 = False
        self.add = False

    def add_c2(self):
        self.c1 = False
        self.c2 = True
        self.add = False

    def set_classify(self):
        self.c1 = False
        self.c2 = False
        self.add = True

    def clear_scene(self):
        self.x_training_sample = []
        self.y_training_sample = []
        self.circles = []

    def stop_alg(self):
        exit(0)

    def import_scene(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt);;JPEG Files(*.jpeg);;\
                                                         PNG Files(*.png);;GIF File(*.gif);;All Files(*)")
        with open(f'{filename}', 'r') as F:
            for line in F.readlines():
                tup = tuple(map(int, line.split(', ')))
                self.x_training_sample.append((tup[0], tup[1]))
                self.y_training_sample.append(tup[2])
                if tup[2] == 1:
                    self.circles.append(Circle(tup[0], tup[1], "magenta"))
                if tup[2] == -1:
                    self.circles.append(Circle(tup[0], tup[1], "cyan"))

    def export_scene(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt);;JPEG Files(*.jpeg);;\
                                                         PNG Files(*.png);;GIF File(*.gif);;All Files(*)")
        with open(f'{filename}', 'w') as F:
            for i in range(len(self.x_training_sample)):
                F.write(f'{self.x_training_sample[i]}'[1:-1] + ', ' + f'{self.y_training_sample[i]}\n')

    def mouseMoveEvent(self, event):
        if (10 <= event.x() <= 710) and (10 <= event.y() <= 710):
            if self.c1:
                if event.button() == Qt.LeftButton:
                    self.x_training_sample.append((event.x() - 10, MAX_Y - event.y() + 10))
                    self.y_training_sample.append(1)
                    self.circles.append(Circle(event.x() - 10, MAX_Y - event.y() + 10, "magenta"))
            if self.c2:
                if event.button() == Qt.LeftButton:
                    self.x_training_sample.append((event.x() - 10, MAX_Y - event.y() + 10))
                    self.y_training_sample.append(-1)
                    self.circles.append(Circle(event.x() - 10, MAX_Y - event.y() + 10, "cyan"))
            if self.add:
                if event.button() == Qt.LeftButton:
                    vector = main.binary_classify(self.x_training_sample, self.y_training_sample)
                    d = (event.x() - 10 - 10) * (700 * vector[0]) - (MAX_Y - event.y() - 10) * (710 - 10)
                    if d > 0:
                        self.result_label.setText("C1")
                    if d < 0:
                        self.result_label.setText("C2")
                    if d == 0:
                        self.result_label.setText("Classification denied")

            if event.button() == Qt.RightButton:
                for circle in self.circles:
                    if circle.if_clicked(event.x() - 10, MAX_Y - event.y() + 10):
                        self.circles.remove(circle)
                        ind = self.x_training_sample.index((circle.x, circle.y))
                        self.x_training_sample.pop(ind)
                        self.y_training_sample.pop(ind)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QPen(Qt.white, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        painter.drawRect(10, 10, 700, 700)
        for circle in self.circles:
            if circle.color == "magenta":
                painter.setPen(QPen(Qt.magenta, 5, Qt.SolidLine))
                painter.setBrush(QBrush(Qt.magenta, Qt.SolidPattern))
                painter.drawEllipse(10 + circle.x - 2, 10 + MAX_Y - circle.y - 2, 4, 4)
            if circle.color == "cyan":
                painter.setPen(QPen(Qt.cyan, 5, Qt.SolidLine))
                painter.setBrush(QBrush(Qt.cyan, Qt.SolidPattern))
                painter.drawEllipse(10 + circle.x - 2, 10 + MAX_Y - circle.y - 2, 4, 4)
        painter.setPen(QPen(Qt.green, 5, Qt.SolidLine))
        vect = main.binary_classify(self.x_training_sample, self.y_training_sample)
        painter.drawLine(10, MAX_Y + 10, 710, MAX_Y - 700 * vect[0])
        self.update()
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
