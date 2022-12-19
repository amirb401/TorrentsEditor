# Torrent URL Changer

This app is a simple command line tool that allows you to change the announce URL of all torrent files in a directory.

## Requirements
- Python 3.11

## Usage
1. Clone or download the repository.
2. Navigate to the directory where the app sits.
3. Run the command `python torrentEditor.py`.
4. Make sure your ".torrent" files are located in the same folder as the `torrentEditor.py` is.
4. Follow the prompts to enter the announce URL to be replaced and the **new** announce URL.

## How It Looks:

![Preview](https://i.imgur.com/eI35IXv.gif)

## Notes
- The app will only modify torrent files. (Files with the .torrent extension).
- The app will modify files strictly based on the input given, so make sure you provide the correct URL.
- This app will not modify your private key, it will only change the base url you provide it with.
- 

## Disclaimer
**Use at your own risk!**

The author is not responsible for any damages or loss of data that may occur as a result of using this app.
