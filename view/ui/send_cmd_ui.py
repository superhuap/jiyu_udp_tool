# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_cmd.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_send_cmd(object):
    def setupUi(self, Form_send_cmd):
        Form_send_cmd.setObjectName("Form_send_cmd")
        Form_send_cmd.resize(597, 481)
        self.BodyLabel_ip = BodyLabel(Form_send_cmd)
        self.BodyLabel_ip.setGeometry(QtCore.QRect(25, 79, 65, 19))
        self.BodyLabel_ip.setObjectName("BodyLabel_ip")
        self.BodyLabel_port = BodyLabel(Form_send_cmd)
        self.BodyLabel_port.setGeometry(QtCore.QRect(240, 70, 65, 19))
        self.BodyLabel_port.setObjectName("BodyLabel_port")
        self.LineEdit_port = LineEdit(Form_send_cmd)
        self.LineEdit_port.setGeometry(QtCore.QRect(290, 60, 151, 33))
        self.LineEdit_port.setInputMask("")
        self.LineEdit_port.setText("")
        self.LineEdit_port.setObjectName("LineEdit_port")
        self.bodyLabel_cmd = BodyLabel(Form_send_cmd)
        self.bodyLabel_cmd.setGeometry(QtCore.QRect(320, 120, 101, 20))
        self.bodyLabel_cmd.setObjectName("bodyLabel_cmd")
        self.LineEdit_cmd = LineEdit(Form_send_cmd)
        self.LineEdit_cmd.setGeometry(QtCore.QRect(270, 150, 191, 33))
        self.LineEdit_cmd.setObjectName("LineEdit_cmd")
        self.Button_Send = PrimaryPushButton(Form_send_cmd)
        self.Button_Send.setGeometry(QtCore.QRect(290, 200, 153, 32))
        self.Button_Send.setObjectName("Button_Send")
        self.ListWidget = ListWidget(Form_send_cmd)
        self.ListWidget.setGeometry(QtCore.QRect(60, 50, 171, 401))
        self.ListWidget.setObjectName("ListWidget")
        self.ProgressBar = ProgressBar(Form_send_cmd)
        self.ProgressBar.setGeometry(QtCore.QRect(240, 260, 231, 4))
        self.ProgressBar.setMaximum(15)
        self.ProgressBar.setProperty("value", 15)
        self.ProgressBar.setObjectName("ProgressBar")
        self.ProgressRing = ProgressRing(Form_send_cmd)
        self.ProgressRing.setGeometry(QtCore.QRect(240, 320, 100, 100))
        self.ProgressRing.setTextVisible(True)
        self.ProgressRing.setObjectName("ProgressRing")
        self.Button_Shutdown = PrimaryPushButton(Form_send_cmd)
        self.Button_Shutdown.setGeometry(QtCore.QRect(380, 310, 153, 32))
        self.Button_Shutdown.setObjectName("Button_Shutdown")
        self.Button_Reboot = PrimaryPushButton(Form_send_cmd)
        self.Button_Reboot.setGeometry(QtCore.QRect(380, 360, 153, 32))
        self.Button_Reboot.setObjectName("Button_Reboot")
        self.Button_OpenSMB = PrimaryPushButton(Form_send_cmd)
        self.Button_OpenSMB.setGeometry(QtCore.QRect(380, 410, 153, 32))
        self.Button_OpenSMB.setObjectName("Button_OpenSMB")
        self.PillPushButton_selectAll = PillPushButton(Form_send_cmd)
        self.PillPushButton_selectAll.setGeometry(QtCore.QRect(110, 10, 121, 30))
        self.PillPushButton_selectAll.setObjectName("PillPushButton_selectAll")
        self.PrimaryPushButton_load_ip = PrimaryPushButton(Form_send_cmd)
        self.PrimaryPushButton_load_ip.setGeometry(QtCore.QRect(20, 10, 71, 32))
        self.PrimaryPushButton_load_ip.setObjectName("PrimaryPushButton_load_ip")

        self.retranslateUi(Form_send_cmd)
        QtCore.QMetaObject.connectSlotsByName(Form_send_cmd)

    def retranslateUi(self, Form_send_cmd):
        _translate = QtCore.QCoreApplication.translate
        Form_send_cmd.setWindowTitle(_translate("Form_send_cmd", "Form"))
        self.BodyLabel_ip.setText(_translate("Form_send_cmd", "IP："))
        self.BodyLabel_port.setText(_translate("Form_send_cmd", "端口："))
        self.bodyLabel_cmd.setText(_translate("Form_send_cmd", "想发送的命令:"))
        self.Button_Send.setText(_translate("Form_send_cmd", "发送"))
        self.Button_Shutdown.setText(_translate("Form_send_cmd", "关机"))
        self.Button_Reboot.setText(_translate("Form_send_cmd", "重启"))
        self.Button_OpenSMB.setText(_translate("Form_send_cmd", "打开共享文件夹"))
        self.PillPushButton_selectAll.setText(_translate("Form_send_cmd", "全选"))
        self.PrimaryPushButton_load_ip.setText(_translate("Form_send_cmd", "加载ip"))
from qfluentwidgets import BodyLabel, LineEdit, ListWidget, PillPushButton, PrimaryPushButton, ProgressBar, ProgressRing
