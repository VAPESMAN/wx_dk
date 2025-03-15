# 微信多开助手 (WeChat Multi-Instance Launcher)

一个简单的微信多开工具，可以帮助你在Windows系统上同时运行多个微信实例。

[English](README_EN.md) | 简体中文

## 功能特点

- 自动检测微信安装路径
- 可选择启动的实例数量（1-10个）
- 显示当前运行的微信实例数量
- 简洁的图形用户界面
- 一键启动多个实例

## 截图

![image](https://github.com/user-attachments/assets/44d93c11-ed97-4f3a-b47e-f93b3c91a51e)


## 安装方法

### 方法1：直接使用

1. 从 [Releases](../../releases) 页面下载最新的可执行文件
2. 双击运行 `WeChatLauncher.exe`

### 方法2：从源码运行

1. 克隆仓库：
```bash
git clone https://github.com/[your-username]/wechat-multi-launcher.git
cd wechat-multi-launcher
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行程序：
```bash
python wechat_multi_launcher.py
```

### 方法3：自行打包

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 使用PyInstaller打包：
```bash
pyinstaller --onefile --windowed --name "WeChatLauncher" wechat_multi_launcher.py
```

## 系统要求

- Windows 7/8/10/11
- 已安装微信客户端
- Python 3.7+ (如果从源码运行)

## 注意事项

- 请确保您的电脑性能足够运行多个微信实例
- 建议不要同时运行过多实例，以免影响系统性能
- 如果找不到微信安装路径，请确认微信是否正确安装
- 本程序仅供学习交流使用，请遵守相关法律法规

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。 
