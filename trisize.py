from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from confirmation import Ui_confirmation
import variables


class Ui_TriSize(object):
    def setupUi(self, TriSize):
        TriSize.setObjectName("Carry")
        TriSize.resize(640, 480)

        #moving position of window to center of screen
        frame = TriSize.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        TriSize.move(frame.topLeft())

        self.pushButton = QtWidgets.QPushButton(TriSize)
        self.pushButton.setStyleSheet("background-color:black; color: red; font-size: 32px")
        self.pushButton.setGeometry(QtCore.QRect(25, 100, 250, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(TriSize)
        self.pushButton_2.setStyleSheet("background-color:black; color: red; font-size: 32px")
        self.pushButton_2.setGeometry(QtCore.QRect(350, 100, 250, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(TriSize)
        self.pushButton_3.setStyleSheet("background-color:black; color: red; font-size: 32px")
        self.pushButton_3.setGeometry(QtCore.QRect(200, 250, 250, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_4 = QtWidgets.QPushButton(TriSize)
        # self.pushButton_4.setStyleSheet("background-color: red;" "color: white")
        # self.pushButton_4.setGeometry(QtCore.QRect(300, 185, 80, 40))
        # self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(TriSize)
        QtCore.QMetaObject.connectSlotsByName(TriSize)

        #Connecting Clicked Buttons
        self.pushButton.clicked.connect(self.Small)
        self.pushButton_2.clicked.connect(self.Medium)
        self.pushButton_3.clicked.connect(self.Large)
        # self.pushButton_4.clicked.connect(self.Back)

    def Small(self):
        variables.command = variables.command + 0.2
        Ui_confirmation.ConfirmationShow(self)


    def Medium(self):
        variables.command = variables.command + 0.4
        Ui_confirmation.ConfirmationShow(self)


    def Large(self):
        variables.command = variables.command + 0.6
        Ui_confirmation.ConfirmationShow(self)


    # def Back(self):
    #     print("return to Main")
    #     variables.command = 0

    def retranslateUi(self, TriSize):
        _translate = QtCore.QCoreApplication.translate
        TriSize.setWindowTitle(_translate("TriSize", "Form"))
        self.pushButton.setText(_translate("TriSize", "Acute"))
        self.pushButton_2.setText(_translate("TriSize", "Iso"))
        self.pushButton_3.setText(_translate("TriSize", "Obtuse"))
        # self.pushButton_4.setText(_translate("TriSize", "Back"))

