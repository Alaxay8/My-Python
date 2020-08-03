
from PyQt5 import QtWidgets
from intarface import Ui_Dialog  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



#Digits buttons
        self.ui.pushButton_2.clicked.connect(lambda: self.displayNumber("2"))
        self.ui.pushButton_3.clicked.connect(lambda: self.displayNumber("1"))
        self.ui.pushButton_4.clicked.connect(lambda: self.displayNumber("4"))
        self.ui.pushButton_5.clicked.connect(lambda: self.displayNumber("5"))
        self.ui.pushButton_7.clicked.connect(lambda: self.displayNumber("7"))
        self.ui.pushButton_8.clicked.connect(lambda: self.displayNumber("8"))
        self.ui.pushButton_9.clicked.connect(lambda: self.displayNumber("9"))
        self.ui.pushButton_6.clicked.connect(lambda: self.displayNumber("6"))
        self.ui.pushButton_10.clicked.connect(lambda: self.zero("0"))
        self.ui.pushButton.clicked.connect(lambda: self.displayNumber("3"))


        self.ui.pushButton_12.clicked.connect(self.decimal) #"."

        self.ui.pushButton_11.clicked.connect(self.unaryOperator)

        self.ui.pushButton_14.clicked.connect(self.binary) #+
        self.ui.pushButton_15.clicked.connect(self.binary) #-
        self.ui.pushButton_16.clicked.connect(self.binary) #*
        self.ui.pushButton_20.clicked.connect(self.binary) #/

        self.ui.pushButton_14.setCheckable(True)
        self.ui.pushButton_15.setCheckable(True)
        self.ui.pushButton_16.setCheckable(True)
        self.ui.pushButton_20.setCheckable(True)

        self.ui.pushButton_17.clicked.connect(lambda:self.squere("х²"))
        self.ui.pushButton_18.clicked.connect(lambda:self.squere("√х"))

        self.ui.pushButton_19.clicked.connect(lambda:self.backscpace("Del"))

        self.ui.pushButton_13.clicked.connect(self.equel)

    def displayNumber(self,value):
        text = self.sender()
        newLabel = format(float(self.ui.label.text() + text.text()),".15g")

        self.ui.label.setText(newLabel)


    def zero(self,zero):
        if self.ui.label.text()[0] != "0":
            self.ui.label.setText(self.ui.label.text()+"0")

    def decimal(self,point):
        if not self.ui.label.text().__contains__("."):
            self.ui.label.setText(self.ui.label.text()+".")
    def squere(self,value):
        total = float(self.ui.label.text())

        if value=="х²":
            total=format((total**2),".15g")
            self.ui.label.setText(total)
        if value == "√х":
            total=format((total**0.5),".15g")
            self.ui.label.setText(total)

    def backscpace(self,value):
        if value == "Del":
            txt = self.ui.label.text()
            txt = txt.replace(txt[-1],"")
            if txt=="":
                txt=txt+"0"
            self.ui.label.setText(txt)

    def unaryOperator(self):
        button = self.sender()
        labelNumber = float(self.ui.label.text())
        if button.text() == "+/-":
            labelNumber = labelNumber* -1
        else:
            labelNumber = labelNumber*0.01
        neLabel = format(labelNumber,"15g")
        self.ui.label.setText(neLabel)

    def binary(self):
        button = self.sender()

        button.setChecked(True)

        self.first = float(self.ui.label.text())

        if button.sender():
            self.ui.label.setText("0")

    def equel(self):
        second = float(self.ui.label.text())


        if self.ui.pushButton_14.isChecked():
            total = format((self.first+second),".15g")
            self.ui.label.setText(total)
            self.ui.pushButton_14.setChecked(False)
        if self.ui.pushButton_15.isChecked():
            total = format((self.first-second),".15g")
            self.ui.label.setText(total)
            self.ui.pushButton_15.setChecked(False)
        if self.ui.pushButton_16.isChecked():
            total = format((self.first * second), ".15g")
            self.ui.label.setText(total)
            self.ui.pushButton_16.setChecked(False)
        if self.ui.pushButton_20.isChecked():
            total = format((self.first / second), ".15g")
            self.ui.label.setText(total)
            self.ui.pushButton_20.setChecked(False)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())