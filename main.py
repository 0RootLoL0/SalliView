import json
import mydesign
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
Wroot = 0
Wschena = 0
textMess = []

class ExampleApp(QtWidgets.QMainWindow, mydesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.otvet)
        self.pushButton_2.clicked.connect(self.pereit)
        self.spinBox.setMaximum(len(textMess))
        self.spinBox.setMinimum(0)
        self.printText()
        self.show()

    def printText(self):
        self.listWidget.addItem(textMess[Wroot][Wschena]["text"])
        self.listWidget.addItem("<---------------------------------------------------------->")
        self.comboBox.clear()
        for textOtveta in textMess[Wroot][Wschena]["otvet"]:
            self.comboBox.addItem(textOtveta["text"])

    def otvet(self):
        print(Wschena)
        print(textMess[Wroot][Wschena]["otvet"][self.comboBox.currentIndex()]["schena"])
        self.sss(textMess[Wroot][Wschena]["otvet"][self.comboBox.currentIndex()]["schena"], textMess[Wroot][Wschena]["root"])
        self.printText()

    def sss(self, schenas, roots):
        global Wschena, Wroot
        Wroot = roots
        Wschena = schenas

    def pereit(self):
        self.sss(self.spinBox_2.value(),self.spinBox.value())
        self.printText()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    try:
        with open('script/script.json') as f:
            textMess = json.load(f)  # TODO засунуть в try и выкидовать ошибку
            f.close()
            main()
    except FileNotFoundError:
        print("error 1")
