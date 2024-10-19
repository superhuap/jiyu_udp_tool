from PyQt5.QtCore import QEventLoop
from PyQt5.QtCore import QSettings, QTimer
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from qfluentwidgets import CheckBox

from utils.param_check import check_ip
from view.ui.send_message_ui import Ui_Form_send_message
from utils.tool_api import send
from utils.utils import utils


class send_message(QWidget, Ui_Form_send_message, utils):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.infoBar = super().infoBar
        # 初始化检查
        self.LineEdit_message.setPlaceholderText("输入要发送的消息")
        self.LineEdit_port.setPlaceholderText("端口默认4705")
        self.settings = QSettings("./config/config.ini", QSettings.IniFormat)
        self.Button_Send.clicked.connect(self.send_message)
        self.PillPushButton_selectAll.clicked.connect(self.selectAll)
        self.PrimaryPushButton_load_ip.clicked.connect(self.load_ip)

        self.load_ip()


    def pause(self, seconds: int):
        loop = QEventLoop()
        QTimer.singleShot(seconds * 1000, loop.quit)
        loop.exec_()

    def lock(self) -> None:  # 运行时锁住按钮
        self.Button_Send.setEnabled(False)
        self.ProgressBar.setValue(0)
        for i in range(int(self.settings.value("CONFIG/time"))):
            self.pause(1)
            self.ProgressBar.setValue(i + 1)
        self.ProgressRing.setValue(0)
        self.Button_Send.setEnabled(True)

    def send_message(self) -> None:  # 发送
        if self.LineEdit_port.text() == '':
            self.LineEdit_port.setText("4705")
            self.infoBar("warning", "端口为空，已填写4705")
            return

        try:
            if int(self.LineEdit_port.text()) > 65535:
                self.infoBar("error", "端口错误")
                return
        except ValueError:
            self.infoBar("error", "端口错误")
            return

        if self.LineEdit_message.text() == '':
            self.infoBar("error", "发送消息为空。")
        else:
            # print(type(self.LineEdit_port.text()))
            count = self.ListWidget.count()
            check_box_list = [self.ListWidget.itemWidget(self.ListWidget.item(i)) for i in range(count)]

            chooses = []
            for cb in check_box_list:
                if cb.isChecked():
                    chooses.append(cb.text())
            if not chooses:
                self.infoBar("error", "无IP选择。")
            else:
                self.Button_Send.setEnabled(False)
                self.ProgressRing.setMaximum(len(chooses))
                self.ProgressBar.setMaximum(int(self.settings.value("CONFIG/time")))
                self.ProgressBar_sendProcess.setMaximum(self.sendNum.value())
                for i, choose in enumerate(chooses):
                    for n in range(self.sendNum.value()):
                        send("msg", self.LineEdit_message.text(), choose, int(self.LineEdit_port.text()))
                        self.ProgressBar_sendProcess.setValue(n + 1)
                        self.pause(int(self.settings.value("CONFIG/time")))

                    self.pause(0.125)
                    self.ProgressRing.setValue(i + 1)
                self.infoBar("success", "发送成功")
                self.Button_Send.setEnabled(True)
                self.lock()

    def selectAll(self) -> None:  # 全选
        check_box_list = [self.ListWidget.itemWidget(self.ListWidget.item(i)) for i in range(self.ListWidget.count())]
        if self.PillPushButton_selectAll.isChecked():
            for check in check_box_list:
                check.setChecked(True)
        else:
            for check in check_box_list:
                check.setChecked(False)

    def load_ip(self):
        self.ListWidget.clear()
        if self.settings.value("CONFIG/ip_list") is None:
            self.infoBar("warning", "未找到ip列表，请去设置。")
        else:
            try:
                with open(self.settings.value("CONFIG/ip_list"), "r", encoding="utf-8") as file:
                    num = 0
                    for data in file.read().split("\n"):
                        box = CheckBox(data)
                        item = QListWidgetItem()
                        if num == 5:
                            break
                        if check_ip(data):
                            self.ListWidget.addItem(item)
                            self.ListWidget.setItemWidget(item, box)
                        else:
                            self.infoBar("error", f"{data}不合法")
                            num += 1

            except TypeError as error:
                self.infoBar("warning", "未找到ip列表，请去设置。")

            except FileNotFoundError as error:
                self.infoBar("error", "列表文件没有找到。")

