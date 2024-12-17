# Data-Preparation-And-Cleaning

# Image Downloader

## Description
This Python script downloads images from a list of URLs stored in either an Excel (.xlsx) file or a plain text file. The script uses the `requests` library to fetch the images, `pandas` to handle the Excel file, and `tqdm` to show a progress bar while downloading. The downloaded images are saved in a specified folder on your local machine.

## Features
- Download images from URLs listed in an Excel or text file.
- Supports both `.xlsx` (Excel) and `.txt` (text) input files.
- Creates an output folder if it doesn't exist.
- Provides a progress bar during the download process.
- Handles errors gracefully, skipping faulty URLs.

## Requirements
Before running the script, make sure you have the following libraries installed:

- `requests`
- `pandas`
- `tqdm`
- `pyfiglet`

You can install these dependencies using the following pip command:

```bash
pip install requests pandas tqdm pyfiglet openpyxl
