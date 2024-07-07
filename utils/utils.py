from PyQt5.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarPosition



class utils:
    def __init__(self):
        pass

    def infoBar(self, type: str, content: str) -> None:
        if type == "warning":
            w = InfoBar.warning(
                title='警告：',
                content=content,
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.BOTTOM_RIGHT,
                duration=5000,
                parent=self
            )
        elif type == "success":
            w = InfoBar.success(
                title='',
                content=content,
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.BOTTOM_RIGHT,
                duration=5000,
                parent=self
            )
        elif type == "error":
            w = InfoBar.error(
                title='错误：',
                content=content,
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.TOP_RIGHT,
                duration=5000,
                parent=self
            )
        w.show()
