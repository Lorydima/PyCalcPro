# PyCalc Pro V1.6
<div align="center">
  <img src="https://github.com/user-attachments/assets/1253decb-4d74-439e-994c-7b1d612871ca" alt="PyCalc_Pro_V1.4_README_Img" width="400" height="900">
</div>

# ℹ️Repository Info 
![GitHub repo size](https://img.shields.io/github/repo-size/Lorydima/PyCalcPro?color=red)
![Platform: Windows](https://img.shields.io/badge/platform-windows-blue)

![GitHub last commit](https://img.shields.io/github/last-commit/Lorydima/PyCalcPro?color=lightblue)
![GitHub version](https://img.shields.io/github/v/release/Lorydima/PyCalcPro?color=blueviolet)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Lorydima/PyCalcPro?color=purple)
![GitHub Issues](https://img.shields.io/github/issues/Lorydima/PyCalcPro?color=purple)

![Contributions welcome](https://img.shields.io/badge/contributions-welcome-green)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)

# 🎲Features

PyCalc Pro includes:
- Basic math operations (+, -, *, /, %)
- Advanced math operations (sqrt, sin, cos, tan, log, abs)
- Unit converter (mass, length)
- Operations memory (last 10 operations)


# 📁Project Structure

```
PyCalc Pro V1.6/
├── src/                               # Application source code + assets
│   ├── main.py                        # Entry point
│   |── pycalcpro_v1.6_data.json       # Operations history
|   |── pycalcpro_v1.6_logo.ico        # Application icon
│
├── modules/                           # Calculation modules (kept at repo root)
│   ├── __init__.py
│   ├── operations.py                  # Calculator math logic
│   ├── state.py                       # State management and history
│   ├── input_validation.py            # Input validation
│   ├── ui.py                          # UI components (Tkinter)
│   └── utils.py                       # Utility functions
│
├── docs/                              # Website documentation
│   ├── index.html
│   ├── style.css
│   └── website images/
│
├── LICENSE.txt                        # MIT License 
├── README.md                          # This file
├── CHANGELOG.md                       # Version history
├── CONTRIBUTING.md                    # Contributing File
├── TESTS.md                           # Manual test documentation
├── pyproject.toml                     # Project metadata
└── .gitattributes                     # Git repository
```

**About assets:**  
Assets (icons and data files) are stored inside so the application can find them when run from source or packaged.

**About the docs/ folder:**  
The `docs/` folder contains files used for the project website and documentation pages. It is **not required to run the application** locally.


# 🌐PyCalc Pro Webiste
<img src="https://github.com/user-attachments/assets/278be1fc-b2ff-4aeb-94f3-32ec7c7856b7" alt="PyCalc_Pro_V1.1_README_Img" width="1200" height="400">
You can access PyCalc Pro Website from this link: <a href="https://lorydima.github.io/PyCalcPro/" target="_blank">PyCalc Pro Website</a>

# 💾Downolad PyCalc Pro 
For donwload PyCalc Pro V.1.5 follow this link, the software is only for **Windows OS:**
<a href="https://github.com/Lorydima/PyCalcPro/releases/download/Relases_PyCalc_Pro_V1.5/PyCalcPro_V1.5_Windows.zip" download>Download PyCalc Pro V1.5</a>

> [!WARNING]
> **For proper program execution, please read the notes below**
> - **AV Alert**  
>   This application is distributed as a standalone .exe built with PyInstaller.
>   Some antivirus software may occasionally flag unsigned PyInstaller executables as false positives.
>  **NOT disable your antivirus.**
>  If your antivirus blocks the file, you can:
>    verify the source code in this repository
>    build the executable yourself from source
>    or add the executable to your antivirus allow-list, if you trust the source
>  No network access, telemetry, or background processes are used by this application.
> - **Important:**  
>   **Do not delete the `.json` or `.ico` or `.txt` other file types** in the download folder they are required for the program to function correctly.

# 🔗Clone Repository
```bash
git clone https://github.com/Lorydima/PyCalcPro.git
```
# 🛠️Bug reports and issue
I do my best to keep this project stable and reliable, but bugs can still happen.
If you spot any issues or errors, feel free to open a GitHub issue.
Your feedback really helps me improve the project.

Thanks for contributing and helping make this project better from *LDM Dev*❤️ 

# 📄License 
Before you use the software please read the **MIT License** license at this link: <a href="https://github.com/Lorydima/PyCalcPro?tab=License-1-ov-file#">License</a>
