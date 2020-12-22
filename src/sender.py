from PyQt5 import QtCore, QtGui, QtWidgets
import socket
from threading import Thread
from socketserver import ThreadingMixIn
import aesN
tcpClientA=None
myClient = None
password = None
click = 0
ptrChat = None
class Ui_Dialog(object):


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 382)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.chat = QtWidgets.QPlainTextEdit(Dialog)
        self.chat.setGeometry(QtCore.QRect(10, 100, 281, 101))
        self.chat.setObjectName("plainTextEdit")
        self.chat.setReadOnly(True)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 260, 281, 71))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 81, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 350, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 350, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 60, 101, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 30, 81, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.getMsgFromEdit)
        self.pushButton_2.clicked.connect(self.sendMessageBtn)
        self.pushButton.clicked.connect(self.closeIt)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        global ptrChat
        ptrChat = self.chat
        global ptrStatus
        ptrStatus = self.label_5
    def closeIt(self):
        self.close()
    def getMsgFromEdit(self):
        try:
            sh = self.lineEdit.text().split(':')
            print(sh[0]+' ' + sh[1])
            global myClient
            clientThread = ClientThread()
            myClient = clientThread
            myClient.ra(sh[0],sh[1])
            myClient.start()
        except:
            self.label_5.setText("<font color='Red'>" + "Error" + "</font>");

    def sendMessageBtn(self):
        sh = self.textEdit.toPlainText()
        print(sh)
        self.textEdit.setPlainText("")
        self.chat.appendPlainText("Me:"+sh)
        global tcpClientA

        temp = aesN.aesCbcEncrypt(sh,password)
        tcpClientA.send(temp)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Client window"))
        self.label.setText(_translate("Dialog", "Enter reciver ip:"))
        self.label_2.setText(_translate("Dialog", "Connection status:"))
        self.label_3.setText(_translate("Dialog", "Chat log:"))
        self.label_4.setText(_translate("Dialog", "Enter message"))
        self.pushButton.setText(_translate("Dialog", "Close"))
        self.pushButton_2.setText(_translate("Dialog", "Send message"))
        self.label_5.setText("<font color='Red'>" + "Disconnected" + "</font>");
        self.pushButton_3.setText(_translate("Dialog", "Connect"))

class ClientThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.host = socket.gethostname()
        self.port = 80
    def ra(self,host,port):
        self.host = host
        self.port = port

    def run(self):
        try:
            BUFFER_SIZE = 2000
            global tcpClientA
            tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            tcpClientA.connect((self.host, int(self.port)))
            global ptrStatus
            ptrStatus.setText("<font color='green'>" + "Connected" + "</font>");
            data = tcpClientA.recv(BUFFER_SIZE)
            global password
            password = data
            print(password)
            while True:
                data = tcpClientA.recv(BUFFER_SIZE)
                decdata = aesN.aesCbcDecrypt(data,password)
                temp = str(decdata)
                ptrChat.appendPlainText("Guest:"+str(temp))

            tcpClientA.close()
        except:
            self.label_5.setText("<font color='Red'>" + "Error" + "</font>");


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    Dialog.show()
    sys.exit(app.exec_())
