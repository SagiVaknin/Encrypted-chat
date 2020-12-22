from PyQt5 import QtCore, QtGui, QtWidgets
import time
import socket
from threading import Thread
from socketserver import ThreadingMixIn
import aesN
import os
conn = None
random_key = os.urandom(16)
ptrIp = None
ptrStatus = None
ptrChat = None

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 382)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 111, 16))
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
        self.label_5.setGeometry(QtCore.QRect(390, 30, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(120, 30, 141, 16))
        self.label_6.setObjectName("label_6")
        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(self.sendMessageBtn)
        self.pushButton.clicked.connect(self.closeIt)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        global ptrChat
        ptrChat = self.chat

        def changeIp(self, host, port):
            self.label_6.setText("<font color='green'>" + host + ":" + port + "</font>");
        global ptrIp
        ptrIp = self.label_6
        def changeStatus(self):
            self.label_5.setText("<font color='green'>"+"Connected"+"</font>");
        global ptrStatus
        ptrStatus = self.label_5
    def closeIt(self):
        self.close()
    def sendMessageBtn(self):
        sh = self.textEdit.toPlainText()
        self.textEdit.setPlainText("")
        self.chat.appendPlainText("Me:" + sh)
        global conn
        temp = aesN.aesCbcEncrypt(sh,random_key)
        conn.send(temp)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Server window"))
        self.label.setText(_translate("Dialog", "Chatting with:"))
        self.label_2.setText(_translate("Dialog", "Connection status:"))
        self.label_3.setText(_translate("Dialog", "Chat log:"))
        self.label_4.setText(_translate("Dialog", "Enter message"))
        self.pushButton.setText(_translate("Dialog", "Close"))
        self.pushButton_2.setText(_translate("Dialog", "Send message"))
        self.label_5.setText("<font color='Red'>" + "Waiting" + "</font>")
        self.label_6.setText("<font color='Red'>" + "No Connection" + "</font>");


class ServerThread(Thread):
    def __init__(self,window):
        Thread.__init__(self)
        self.window=window

    def run(self):
        TCP_IP = '0.0.0.0'
        TCP_PORT = 80
        BUFFER_SIZE = 20
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.bind((TCP_IP, TCP_PORT))
        threads = []

        tcpServer.listen(4)
        while True:
            print("Multithreaded Python server : Waiting for connections from TCP clients...")
            global conn
            (conn, (ip, port)) = tcpServer.accept()
            newthread = ClientThread(ip, port, self.window)
            newthread.start()
            threads.append(newthread)

        for t in threads:
            t.join()


class ClientThread(Thread):

    def __init__(self, ip, port, window):
        Thread.__init__(self)
        self.window = window
        self.ip = ip
        self.port = port
        print("[+] New server socket thread started for " + ip + ":" + str(port))
        global ptrIp
        ptrIp.setText("<font color='green'>" + ip + ":" + str(port) + "</font>");
        global ptrStatus
        ptrStatus.setText("<font color='green'>" + "Connected" + "</font>")


    def run(self):
        global conn
        print(random_key)
        conn.send(random_key)
        while True:
            data = conn.recv(2048)
            data = aesN.aesCbcDecrypt(data,random_key)
            temp = str(data)
            #temp = temp[2:-1]
            ptrChat.appendPlainText("Guest:"+str(temp))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    import socket
    serverThread=ServerThread(Dialog)
    serverThread.start()
    sys.exit(app.exec_())
