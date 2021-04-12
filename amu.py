import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


qss = """
    QLabel {
        color: rgb(100, 100, 100);
    }
    QPushButton {
        color: rgb(100, 0, 0);
    }
    QPushButton:hover {
        color: rgb(255, 255, 255);
        background-color: rgb(0, 0, 0);
    }
    
    QPushButton#Start {
        color: rgb(100, 0, 100);
    }
    QPushButton#Start:hover {
        color: rgb(100, 100, 100);
        background-color: rgb(200, 200, 20);
    }
"""


class MyBtn(QPushButton):
    def __init__(self, parent, x, y, txt_name='', prop=''):
        super(MyBtn, self).__init__(parent=parent)
        self.parent = parent
        self.setGeometry(x, y, 100, 100)
        self.setObjectName(prop)

        self.setText(txt_name)

        self.click_count = 0

    def mousePressEvent(self, e) -> None:
        print(f'{self} Click !! {self.click_count}')
        self.click_count += 1


class MyApp(QWidget):
    def __init__(self, parent=None):
        super(MyApp, self).__init__()

        self.setWindowTitle('My First Application')
        self.setStyleSheet(qss)

        self.move(300, 300)
        self.resize(400, 200)

        _1 = MyBtn(self, 0, 0, txt_name='Call1', prop='Start'),
        _2 = MyBtn(self, 100, 100, txt_name='Call2')


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   ex.show()
   sys.exit(app.exec_())