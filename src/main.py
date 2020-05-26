import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import *
from AboutWindow import *

class MainWindowUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowUI, self).__init__(parent)
        self.setupUi(self)

class AboutWindowUI(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(AboutWindowUI, self).__init__(parent)
        self.setupUi(self)

    def accept(self): self.hide()
    def reject(self): sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindowUI()
    aboutWindow = AboutWindowUI()

    mainWindow.show()
    mainWindow.aboutButton.clicked.connect(aboutWindow.show)

    sys.exit(app.exec_())