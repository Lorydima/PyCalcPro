# Changelog — PyCalc Pro

All notable changes to this project will be documented in this file.  
This project uses semantic versioning.

## [1.7] - 2026-01-2026
### Added
- Decimal precision arithmetic to eliminate floating-point errors
- Input validation for free-form text prevention
- Error handling for NoneType exceptions

### Fixed
- Fixed C/CE button functions (swapped functionality)
  - C now clears last entry (removes one character)
  - CE now clears entire entry (resets calculator)
- Fixed floating-point calculation errors (e.g., 5.5-1.2-1.2 now returns 3.1 instead of 3.09999999999999996)
- Fixed Operations Memory display showing internal Decimal conversion syntax
- Fixed macOS white text visibility on red buttons
- Fixed input validation to reject free-form text like "HELLO WORLD" with proper error messages
- Fixed calculator recovery after division by zero and other errors

### Changed
- Updated all version references from v1.6 to v1.7
- Changed icon filename from PyCalc_Pro_V1.6_Logo.ico to PyCalc_Pro_Logo.ico
- Changed data file from PyCalcPro_V1.6_DATA.json to DATA.json
- Reorganized project structure for better maintainability
- Improved code documentation with docstrings

## [1.6] - 2025-12-29
### Changed
- Project structure reorganized to follow Python best practices
- MIT License simplified (removed EULA requirement)
- Improved documentation and clarity

### Improved
- Repository structure and file organization
- Code readability and modularity

## [1.5] - 2025-11-15
### Fixed
- Bug fixes


## [1.4] - 2025-06-23
### Added
- License check function on program

### Fixed
- Bug fixes


## [1.3] - 2025-04-18
### Added
- "Read License" button on credit window  
- "PyCalc Pro Website" button on credit window  


## [1.2] - 2025-04-02
### Added
- Operations Memory Function

### Fixed
- Bug fixes  


## [1.1] - 2025-03-29
### Added
- Terms of use on a `.txt` file

### Fixed
- Bug fixes


## [1.0] - 2025-02-22
### Added
- Math basic operations  
- Math advanced operations  
- Unit converter  
