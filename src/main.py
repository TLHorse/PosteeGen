import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

from PosterArrangement import *
from WindowManager import *

posterArngModel = PosterArrangement()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindowUI()
    aboutWindow = AboutWindowUI()
    textEditWindow = TextEditWindowUI()
    chooseTemplateWindow = ChooseTemplateWindowUI()
    checkArgsWindow = CheckArgsWindowUI()

    mainWindow.show()

    ##### Main window method #####

    mainWindow.aboutButton.clicked.connect(aboutWindow.show)
    mainWindow.newButton.clicked.connect(textEditWindow.show)

    ##### textEditWindow method #####

    def setTextEditInfo():
        global posterArngModel, textEditWindow, chooseTemplateWindow
        posterArngModel.posterTitle = textEditWindow.titleInput.text()
        for i in range(4): exec(f"posterArngModel.part{i + 1}Text = textEditWindow.textEdit_{i + 1}.toPlainText()")
        posterArngModel.posterTitleFont = textEditWindow.titleFontBox.currentText()
        posterArngModel.posterTextFont = textEditWindow.textFontBox.currentText()
        posterArngModel.posterTitleSize = textEditWindow.titlePointsSpinBox.value()
        posterArngModel.posterTextSize = textEditWindow.textPointsSpinBox.value()
        # chooseTemplateWindow.show()

    textEditWindow.continueButton.clicked.connect(lambda: chooseTemplateWindow.showWith(setTextEditInfo))
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

    def setTemplateInfo():
        global checkArgsWindow, chooseTemplateWindow, posterArngModel
        posterArngModel.template = list(chooseTemplateWindow.currentChooseLabel.text())[5]

    for i in [1, 2, 3, 4]:
        exec(f"""
chooseTemplateWindow.temp{i}Button.toggled.connect(
    lambda tempChoosed: chooseTemplateWindow.currentChooseLabel.setText("当前选择：{i}")
)
""")
    chooseTemplateWindow.continueButton.clicked.connect(lambda: checkArgsWindow.showWith(setTemplateInfo))

    sys.exit(app.exec_())
