import sys
import os
import psutil
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLabel, QSpinBox, QPushButton, QMessageBox)
from PySide6.QtCore import Qt

class WeChatLauncher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wechat_path = self.find_wechat_path()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('微信多开助手')
        self.setFixedSize(400, 200)

        # 创建主窗口部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 显示微信路径
        path_layout = QHBoxLayout()
        path_label = QLabel('微信路径:', self)
        path_value = QLabel(self.wechat_path if self.wechat_path else '未找到微信安装路径', self)
        path_layout.addWidget(path_label)
        path_layout.addWidget(path_value)
        layout.addLayout(path_layout)

        # 实例数量选择
        count_layout = QHBoxLayout()
        count_label = QLabel('启动实例数量:', self)
        self.count_spin = QSpinBox(self)
        self.count_spin.setRange(1, 10)
        self.count_spin.setValue(2)
        count_layout.addWidget(count_label)
        count_layout.addWidget(self.count_spin)
        layout.addLayout(count_layout)

        # 启动按钮
        launch_button = QPushButton('一键启动', self)
        launch_button.clicked.connect(self.launch_wechat)
        layout.addWidget(launch_button)

    def find_wechat_path(self):
        """查找微信安装路径"""
        possible_paths = [
            os.path.expandvars(r'%ProgramFiles(x86)%\Tencent\WeChat\WeChat.exe'),
            os.path.expandvars(r'%ProgramFiles%\Tencent\WeChat\WeChat.exe'),
            os.path.expandvars(r'%UserProfile%\AppData\Local\Tencent\WeChat\WeChat.exe')
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None

    def launch_wechat(self):
        """启动多个微信实例"""
        if not self.wechat_path:
            QMessageBox.critical(self, '错误', '未找到微信安装路径！')
            return

        count = self.count_spin.value()
        launched = 0

        # 检查现有的微信进程
        existing_instances = len([p for p in psutil.process_iter(['name']) 
                                if p.info['name'] == 'WeChat.exe'])

        for i in range(count):
            try:
                # 使用命令行参数来实现多开
                os.startfile(self.wechat_path)
                launched += 1
            except Exception as e:
                QMessageBox.warning(self, '警告', f'启动第{i+1}个实例时出错：{str(e)}')
                break

        QMessageBox.information(self, '成功', 
            f'成功启动{launched}个微信实例\n当前共有{existing_instances + launched}个实例在运行')

def main():
    app = QApplication(sys.argv)
    launcher = WeChatLauncher()
    launcher.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main() 