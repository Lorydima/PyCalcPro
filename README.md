# PyCalc Pro V1.6
<div align="center">
  <img src="https://github.com/user-attachments/assets/c27c154a-8c2d-4615-9cfb-885b824f65d4" alt="PyCalc_Pro_V1.4_README_Img" width="400" height="900">
</div>

# ℹ️Repository Info 
![GitHub stars](https://img.shields.io/github/stars/Lorydima/NeonNote?color=gold)
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
│   ├── main.py                        # Source Code
│   |── pycalcpro_v1.6_data.json       # Operations history
|   |── pycalcpro_v1.6_logo.ico        # Application icon
│
├── modules/                           # Calculation modules 
│   ├── __init__.py
│   ├── operations.py                  # Calculator math logic
│   ├── state.py                       # State management and history
│   ├── input_validation.py            # Input validation
│   ├── ui.py                          # UI components 
│   └── utils.py                       # Utility functions
│
├── docs/                              # Website source code
│   ├── index.html
│   ├── style.css
│   └── website images
│
├── LICENSE.txt                        # MIT License 
├── README.md                          # This file
├── CHANGELOG.md                       # Version history
├── CONTRIBUTING.md                    # Contributing File                       
├── pyproject.toml                     # Project metadata
└── .gitattributes                     # Git repository
```

**About assets:**  
Assets (`.json` and `.ico`) are stored inside so the application can find them when run from source or packaged.

**About the docs/ folder:**  
The `docs/` folder contains files used for source code of the website. It is **not required to run the application** locally.


# 🌐PyCalc Pro Webiste
<img src="https://github.com/user-attachments/assets/d02caa45-b13e-410c-ab4c-5c8e4d34142e" alt="PyCalc_Pro_V1.1_README_Img" width="1200" height="400">
You can access PyCalc Pro Website from this link: <a href="https://lorydima.github.io/PyCalcPro/" target="_blank">PyCalc Pro Website</a>

# 💾Downolad PyCalc Pro 
For donwload PyCalc Pro V.1.6 follow this link, the software is only for **Windows OS:**
<a href="https://github.com/Lorydima/PyCalcPro/releases/download/PyCalc_Pro_V1.6_Relase/PyCalc_Pro_V1.6_Windows.zip" download>Download PyCalc Pro V1.6</a>

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
Before you use the software please read the **MIT License** license at this link: <a href="https://github.com/Lorydima/PyCalcPro/blob/main/LICENSE.txt">License</a>
