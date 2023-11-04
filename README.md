# Prototype Game CPU Limiter

## Introduction

This script allows you to run a prototype game that may not be compatible with Windows 10 and Windows 11. By limiting
the CPU affinity of the game, you can potentially make it work on these newer versions of Windows.

## How to Use (Simple)

1. Download
   the [executable file](https://github.com/Ahmadrezadl/prototype-game-runner/releases/download/v1.0.0/prototype-launcher.exe)
   from releases section.

2. Run downloaded file which named: `prototype-launcher.exe`

3. In the GUI window, use the following steps to run the game:

    - Click the "Browse" button to select the prototype game's `.exe` file.
    - Once selected, the file path will appear in the text entry field.
    - Click the "Run Game" button to start the game with limited CPU affinity.

4. Enjoy playing your prototype game on your new windows.

## How to Use (Programmers)

To run the script using Python, follow these steps:

1. Clone or download this repository to your local machine.

2. Make sure you have Python installed on your system. If not, you can download it
   from [Python's official website](https://www.python.org/downloads/).


3. Navigate to the directory where you have the repository cloned or extracted.


4. Install the required Python libraries using the following command in your terminal or command prompt:

   ```
   pip install -r requirements.txt
   ```


5. Run the `main.py` script using the following command:

   ```
   python main.py
   ```
   
6. The graphical user interface (GUI) window will appear, and you can follow the same steps as mentioned in the "How to
   Use (Simple)" section to run the game.

## Troubleshooting

- If you encounter any issues or the game still doesn't work correctly, please note that this script may not work for
  all games. Some games may have compatibility issues that cannot be resolved by limiting CPU affinity.


