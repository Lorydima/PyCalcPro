<div align="center">
  <h1>PyCalc Pro</h1>
  <img src="docs/PyCalc_Pro_Logo.png" alt="PyCalc Pro Logo" width="200">
  <br>
  <img src="https://img.shields.io/github/stars/Lorydima/PyCalcPro?color=gold" alt="GitHub stars">
  <img src="https://img.shields.io/badge/platforms-Windows%20%7C%20Linux%20via%20Wine or main.py%20%7C%20macOS%20via%20main.py-red" alt="Platforms">
  <img src="https://img.shields.io/badge/contributions-welcome-green" alt="Contributions welcome">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="License: MIT">
  <br>
</div>

<div align="center">
  <a href="https://lorydima.github.io/PyCalcPro/" target="_blank" style="font-size: 30px; font-weight: bold;">Website</a>
</div>

<br>
<p align="center"><strong>Professional and easy to use calculator developed in Python</strong></p>

# 🎲 Features

| Images | Feature Description |
| ------------ | ------------------- |
| ![PyCalc Pro GUI](https://github.com/user-attachments/assets/44b319b5-1a12-4d44-94be-c4f50ba28488) | **GUI screenshot** |
| ![PyCalc Pro 1](https://lorydima.github.io/PyCalcPro/PyCalc_Pro_README_02.png) | **Advanced math operations:** sqrt, sin, cos, tan, log, abs |
| ![PyCalc Pro 2](https://lorydima.github.io/PyCalcPro/PyCalc_Pro_README_03.png) | **Unit converter:** mass, length; |
| ![PyCalc Pro 3](https://lorydima.github.io/PyCalcPro/PyCalc_Pro_README_04.png) | **Operations memory:** last 10 operations |

# 📁Project Structure

```
PyCalcPro/
├── src/                               # Application source code
│   └── pycalcpro/                     # Main application package
│       ├── __init__.py                # Package initializer
│       ├── main.py                    # Application entry point
│       ├── calculator.py              # Main GUI and calculator logic
│       ├── operations.py              # Calculator math operations
│       ├── storage.py                 # Operations history management
│       ├── ui.py                      # UI windows and components
│       ├── assets.py                  # Asset paths management
│       │
│       └── Assests/                   # Application assets
│           ├── PyCalc_Pro_Logo.ico    # Application icon
│           └── DATA.json              # Operations history storage
│
├── docs/                              # Website Source Code
│   ├── index.html
│   ├── style.css
│   └── images                         # Website images and ico
│
├── LICENSE.txt                        # MIT License
├── README.md                          # Project overview 
├── CHANGELOG.md                       # Version history
├── CONTRIBUTING.md                    # Contribution guidelines
├── pyproject.toml                     # Project metadata and build config
├── SECURITY.md                        # Security Policy
└── .gitattributes                     # Git repository settings
```

**About assets:**  
Assets (icons and data files) are stored inside so the application can find them when run from source or packaged.

**About the docs/ folder:**  
The `docs/` folder contains files used for the source code of website. It is **not required to run the application** locally.

# 💾Downolad PyCalc Pro

To donwload PyCalc Pro V.1.7 follow this link, the software is for **Windows OS, for linux use Wine:**
<a href="https://github.com/Lorydima/PyCalcPro/releases/download/PyCalc_Pro_V1.7_Relase/PyCalc_Pro_V1.7.zip" download>Download PyCalc Pro V1.7</a>

**For macOS**  
The `.app` file is not available.

However, the application can be run from source by executing the `main.py` file,
provided that Python and the required dependencies are installed.

# 🔗Clone Repository

Follow this steps:

```bash
git clone https://github.com/Lorydima/PyCalcPro.git
```

```bash
run main.py
```

All libraries used in this project are part of **Python's standard library**. No external libraries are required

# 🛠️Bug reports and issue

I do my best to keep this project stable and reliable, but bugs can still happen.
If you spot any issues or errors, feel free to open a GitHub issue.
Your feedback really helps me improve the project.

Thanks for contributing and helping make this project better from *LDM Dev*❤️

# 📄License

Before you use the software please read the **MIT License** license at this link: <a href="https://github.com/Lorydima/PyCalcPro?tab=License-1-ov-file#">License</a>
