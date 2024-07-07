import sys

import PyQt5.QtCore as qc
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentIcon as FIF, setTheme, setThemeColor
from qfluentwidgets import FluentWindow, NavigationItemPosition, Theme

from view.widget.send_cmd_widget import send_cmd
from view.widget.send_message_widget import send_message
from view.widget.setting_widget import setting
from utils.utils import utils

class MainWindows(FluentWindow):
    def __init__(self):
        super().__init__()
        self.settings = qc.QSettings("./config/config.ini", qc.QSettings.IniFormat)
        self.send_message = send_message()
        self.setting = setting()
        self.send_cmd = send_cmd()

        self.add_interface()
        self.setFixedSize(600, 500)

        if self.settings.value("CONFIG/theme") == "light":
            setTheme(Theme.LIGHT)
        if self.settings.value("CONFIG/theme") == "dark":
            setTheme(Theme.DARK)

        if self.settings.value("CONFIG/theme_color") is None:
            pass
        else:
            setThemeColor(self.settings.value("CONFIG/theme_color"))

    def add_interface(self):
        pos = NavigationItemPosition.SCROLL
        self.addSubInterface(self.send_message, FIF.CHAT, self.tr("消息发送"), pos)
        self.addSubInterface(self.send_cmd, FIF.DEVELOPER_TOOLS, self.tr("命令发送"), pos)
        self.addSubInterface(self.setting, FIF.SETTING, self.tr("设置"), pos)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindows()
    window.setWindowTitle("极域udp重放工具")
    window.show()
    app.exec_()
