# Command Line Radio Player

A simple yet powerful command-line interface radio player that lets you stream music from various internet radio stations. Built with Python and VLC.

## Features

- Stream multiple radio stations directly from your terminal
- Easy-to-use command interface
- Volume control
- Support for multiple streaming formats including AAC and MP3
- Automatic handling of PLS playlist files
- Currently supported stations:
  - KEXP (Seattle)
  - WMSE (Milwaukee)
  - XRAY.fm (Portland)
  - KCRW (Los Angeles)

## Requirements

- Python 3.x
- VLC media player installed on your system
- python-vlc package (automatically installed during setup)

## Installation

1. Make sure you have VLC media player installed on your system
2. Clone this repository or download the source code
3. Create and activate a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Unix/MacOS
# or
.\venv\Scripts\activate  # On Windows
```
4. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

There are two ways to run the program:

### Method 1: Direct Run
Navigate to the project directory and run:
```bash
source venv/bin/activate  # Activate virtual environment
python3 radio.py
```

### Method 2: Using an Alias (recommended)
Add this alias to your shell configuration file (e.g., `.zshrc` or `.bashrc`):
```bash
alias radio="cd /path/to/radio/directory && source venv/bin/activate && python3 radio.py"
```
After adding the alias and reloading your shell configuration, simply type:
```bash
radio
```

### Available Commands

- `play`: Start playing a station
  - When prompted, enter the station name or press Enter to play the current station
  - Available stations: KEXP, WMSE, KXRY, KCRW
- `stop`: Stop the current stream
- `volume`: Change the volume
  - Enter a value between 0-100 when prompted
- `stations`: List all available radio stations
- `quit`: Exit the program

## Default Station

The default station is set to KEXP. You can change stations at any time using the `play` command.

## Contributing

Feel free to fork this repository and submit pull requests to add more stations or features.

## License

This project is open source and available under the MIT License. 
