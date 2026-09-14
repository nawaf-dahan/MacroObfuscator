# MacroObfuscator - Pure Python VBA Obfuscation Tool

A lightweight cybersecurity tool for obfuscating VBA Macros in Office documents, built using **Pure Python (Standard Library only)** for security analysis and pentesting research.

## Features
- **Pure Python**: Built strictly using standard Python libraries (`argparse`, `re`, `json`, `logging`, `os`, `sys`).
- **CLI Standard Support**: Supports `--help`, `--version`, `--config`, and `--log-level`.
- **Obfuscation Techniques**:
  - Strips comments and unnecessary lines.
  - Encodes raw string literals into `Chr()` ASCII concatenations.
  - Renames `Dim` variables into randomized obfuscated identifiers.

## Installation
No third-party packages are required.
```bash
git clone [https://github.com/YourUsername/MacroObfuscator.git](https://github.com/YourUsername/MacroObfuscator.git)
cd MacroObfuscator

# Basic Usage
python macro_obfuscator.py -i sample.vba -o output.vba

# Help & Options
python macro_obfuscator.py --help

# Custom Config & Debug Logging
python macro_obfuscator.py -i sample.vba --config config.json --log-level DEBUG