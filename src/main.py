import sys

from functools import partial
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

import AboutWindow
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindowUI()
    aboutWindow = AboutWindowUI()
    textEditWindow = TextEditWindowUI()
    chooseTemplateWindow = ChooseTemplateWindowUI()

    mainWindow.show()

    ##### Main window method #####

    mainWindow.aboutButton.clicked.connect(aboutWindow.show)
    mainWindow.newButton.clicked.connect(textEditWindow.show)
    textEditWindow.continueButton.clicked.connect(chooseTemplateWindow.show)

    ##### textEditWindow method #####

    # Font family method
    textEditWindow.titleFontBox.currentFontChanged.connect(textEditWindow.titleInput.setFont)
    for i in [1, 2, 3, 4]:
        exec(f"textEditWindow.textFontBox.currentFontChanged.connect(textEditWindow.textEdit_{i}.setFont)")

    # Font point size method
    textEditWindow.titlePointsSpinBox.valueChanged.connect(
        lambda fontPoint: textEditWindow.titleInput.setFont(QtGui.QFont(str(textEditWindow.titleFontBox.currentFont), pointSize=fontPoint))
    )
    for i in [1, 2, 3, 4]:
        exec(f"""
textEditWindow.textPointsSpinBox.valueChanged.connect(
    lambda fontPoint: textEditWindow.textEdit_{i}.setFont(QtGui.QFont(str(textEditWindow.textFontBox.currentFont), pointSize=fontPoint))
)
""")

    ##### chooseTemplateWindow method #####

    for i in [1, 2, 3, 4]:
        exec(f"""
chooseTemplateWindow.temp{i}Button.toggled.connect(
    lambda tempChoosed: chooseTemplateWindow.currentChooseLabel.setText("当前选择：{i}")
)
""")

    sys.exit(app.exec_())
