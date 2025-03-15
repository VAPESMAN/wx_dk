# WeChat Multi-Instance Launcher

Created by Cursor, a simple tool to help you run multiple WeChat instances simultaneously on Windows.

English | [简体中文](README.md)

## Features

- Automatically detect WeChat installation path
- Choose the number of instances to launch (1-10)
- Display current running WeChat instances
- Clean and simple GUI
- One-click launch multiple instances

## Screenshots

![image](https://github.com/user-attachments/assets/2010bdfb-ecd6-4d6b-9895-59e9ef875056)


## Installation

### Method 1: Direct Use

1. Download the latest executable from [Releases](../../releases)
2. Double-click `WeChatLauncher.exe` to run

### Method 2: Run from Source

1. Clone the repository:
```bash
git clone https://github.com/[your-username]/wechat-multi-launcher.git
cd wechat-multi-launcher
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the program:
```bash
python wechat_multi_launcher.py
```

### Method 3: Build from Source

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Build with PyInstaller:
```bash
pyinstaller --onefile --windowed --name "WeChatLauncher" wechat_multi_launcher.py
```

## System Requirements

- Windows 7/8/10/11
- WeChat client installed
- Python 3.7+ (if running from source)

## Notes

- Ensure your computer has sufficient resources to run multiple WeChat instances
- Avoid running too many instances simultaneously to prevent system performance issues
- If WeChat installation path is not found, verify that WeChat is properly installed
- This program is for educational and learning purposes only

## Contributing

Issues and Pull Requests are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
