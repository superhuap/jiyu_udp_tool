import PyQt5.QtCore as qc
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFileDialog
from qfluentwidgets import setTheme, setThemeColor, Theme, isDarkTheme, \
    ColorDialog

from view.ui.setting_ui import Ui_Form_Setting
from utils.utils import utils


class setting(QWidget, Ui_Form_Setting, utils):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.infoBar = super().infoBar
        self.LineEdit_path.setPlaceholderText("ip列表路径：")

        self.Button_get_path.clicked.connect(self.set_path)
        self.Button_submit.clicked.connect(self.submit)
        self.Button_setTheme.clicked.connect(self.setTheme)
        self.Button_setThemeColor.clicked.connect(self.setThemeColor)

        self.settings = qc.QSettings("./config/config.ini", qc.QSettings.IniFormat)
        self.LineEdit_path.setText(self.settings.value("CONFIG/ip_list"))

        self.ComboBox_run_type.addItems(["cmd.exe", "powershell.exe"])
        if self.settings.value("CONFIG/run_type") is None:
            self.ComboBox_run_type.setCurrentText("cmd.exe")
        else:
            data = str(self.settings.value("CONFIG/run_type"))
            self.ComboBox_run_type.setCurrentText(data)

        if self.settings.value("CONFIG/time") is None:
            self.SpinBox_time.setValue(1)
        else:
            self.SpinBox_time.setValue(int(self.settings.value("CONFIG/time")))

    # 设置ip_list文件路径
    def set_path(self):
        file_path = QFileDialog.getOpenFileName(self, "选取文件", "C:/", "Text Files (*.txt)")
        if file_path[0] != '':
            self.LineEdit_path.setText(file_path[0])
            self.settings.setValue("CONFIG/ip_list", file_path[0])
            self.infoBar("success", "设置成功。")

    # 提交按钮
    def submit(self):
        self.settings.setValue("CONFIG/time", self.SpinBox_time.value())
        self.settings.setValue("CONFIG/run_type", self.ComboBox_run_type.currentText())
        self.infoBar("success", "已提交设置。")

    # 设置主题
    def setTheme(self):
        theme = Theme.LIGHT if isDarkTheme() else Theme.DARK
        if theme == Theme.DARK:
            self.settings.setValue("CONFIG/theme", "dark")
        if theme == Theme.LIGHT:
            self.settings.setValue("CONFIG/theme", "light")
        setTheme(theme)

    # 设置主题色
    def setThemeColor(self):
        w = ColorDialog(Qt.cyan, self.tr('Choose color'), self.window())
        w.colorChanged.connect(
            lambda c: (setThemeColor(c.name()), self.settings.setValue("CONFIG/theme_color", c.name())))
        w.exec()
