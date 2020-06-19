from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import AboutWindow
import CheckArgsWindow
import ChooseTemplateWindow
import MainWindow
import TextEditWindow
import PosterArrangement
from PosterResultWindow import *


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
    def __init__(self, parent=None, model=PosterArrangement.PosterArrangement()):
        """The UI window use to check poster arguments (allocs).

        Keyword Arguments:
            parent {QMainWindow} -- [Parent window of CheckArgsWindow.] (default: {None})
            model {PosterArrangement} -- [Poster allocation model.] (default: {PosterArrangement()})
        """        
        super(CheckArgsWindowUI, self).__init__(parent)
        self.model = model
        self.setupUi(self)
    def showWith(self, do):
        do(); super(CheckArgsWindowUI, self).show()
        _translate = QtCore.QCoreApplication.translate
        self.titleDesLabel.setText(_translate("Dialog", self.model.posterTitle))
        self.part1Label.setText(_translate("Dialog", self.model.part1Text))
        self.part2Label.setText(_translate("Dialog", self.model.part2Text))
        self.part3Label.setText(_translate("Dialog", self.model.part3Text))
        self.part4Label.setText(_translate("Dialog", self.model.part4Text))
        self.titleFontDesLabel.setText(_translate("Dialog", self.model.posterTitleFont))
        self.textFontDesLabel.setText(_translate("Dialog", self.model.posterTextFont))

class PosterResultWindowUI(PosterResultWindow):
    def __init__(self, model=PosterArrangement.PosterArrangement()):
        super(PosterResultWindowUI, self).__init__(model=model)
    def show(self):
        super(PosterResultWindowUI, self).appear()
