# Changelog — PyCalc Pro

All notable changes to this project will be documented in this file.  
This project uses semantic versioning.

## [1.6] - 2025-12-29
### Added
- Modular project structure (src/modules/)
- Separate module files: operations, state, ui, input_validation, utils
- Assets folder for icons and data files
- Pathlib support for cross-platform compatibility

### Fixed
- Calculator C/CE button behavior (C clears all, CE clears last entry)
- Input validation to prevent free-form text entry
- Float precision issues using Decimal arithmetic
- NoneType crashes after invalid input
- User-friendly error messages instead of raw Python exceptions
- License handling (MIT license only)

### Changed
- Project structure reorganized to follow Python best practices
- MIT License simplified (removed EULA requirement)
- Improved documentation and clarity

### Improved
- Repository structure and file organization
- Code readability and modularity
- Error recovery and state management
- Asset loading with pathlib

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