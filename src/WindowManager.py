from PyQt5.QtWidgets import QApplication, QMainWindow

import AboutWindow
import CheckArgsWindow
import ChooseTemplateWindow
import MainWindow
import TextEditWindow


class MainWindowUI(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowUI, self).__init__(parent)
        self.setupUi(self)

class AboutWindowUI(QMainWindow, AboutWindow.Ui_Dialog):
    def __init__(self, parent=None):
        super(AboutWindowUI, self).__init__(parent)
        self.setupUi(self)

    def accept(self): self.close()
    def reject(self): sys.exit(0)

class TextEditWindowUI(QMainWindow, TextEditWindow.Ui_Dialog):
    def __init__(self, parent=None):
        super(TextEditWindowUI, self).__init__(parent)
        self.setupUi(self)

class ChooseTemplateWindowUI(QMainWindow, ChooseTemplateWindow.Ui_Dialog):
    def __init__(self, parent=None):
        super(ChooseTemplateWindowUI, self).__init__(parent)
        self.setupUi(self)
    def showWith(self, do):
        do(); super(ChooseTemplateWindowUI, self).show()

class CheckArgsWindowUI(QMainWindow, CheckArgsWindow.Ui_Dialog):
    def __init__(self, parent=None):
        super(CheckArgsWindowUI, self).__init__(parent)
        self.setupUi(self)
    def showWith(self, do):
        do(); super(CheckArgsWindowUI, self).show()

