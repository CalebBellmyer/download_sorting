# File Sorting Script

## Table of Contents

-   [Description](#description)
-   [Features](#features)
-   [Requirements](#requirements)
-   [Installation and Setup](#installation-and-setup)
-   [Usage](#usage)
-   [How It Works](#how-it-works)
-   [Supported File Extensions](#supported-file-extensions)
-   [Customization](#customization)

## Description

This Python script **automatically organizes files** in the Downloads folder into categorized subfolders based on their file types.

## Features

-   **Automatic Detection**: Sorts files into designated subfolders.
-   **Error Handling**: Manages file access issues gracefully.
-   **Supported Types**: Images, Videos, Documents.

## Requirements

-   Python 3.x
-   PyInstaller (optional for executable)

## Installation and Setup

1. Install Python 3.x.
2. Clone the repo: `git clone https://your-repo-link`.
3. (Optional) Create an executable:
    ```bash
    pip install pyinstaller
    pyinstaller --onefile --icon=sort_icon.ico sort.py
    ```

## Usage

Run the script using Python

```
  python sort.py
```

or, double click the executable

## How it works

The script categorizes files into 'Images', 'Videos', 'Documents', 'Executables', 'Compressed', 'Music', 'Programming', 'Spreadsheats', and 'Presentations' based on file extensions

## Supported File Extensions

-   **Images**: .jpg, .jpeg, .png, .svg .webp .map
-   **Videos**: .mp4, .avi, .mov .flv .mkv .wmv .webm
-   **Documents**: .pdf, .docx, .txt .doc .ppt .xls .xlsx .ovt .ods .dop .odg .odf
-   **Executables**: .exe .msi .apk
-   **Compressed**: .zip .rar .tar .gz
-   **Music**: .mp3 .wav .ogg .flac .alac
-   **Programming**: .py .js .html .css .java .cpp .cs .c .sql
-   **Spreadsheets**: .xlsx, .csv, .ods
-   **Presentations**: .pptx

## Customization

Modify the 'file_type' dictionary in the script to change file categories and extensions.
