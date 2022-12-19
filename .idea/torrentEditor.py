from torrentool.api import Torrent
import pathlib
import os

#Initialize inputs from user
changeFrom = input("Enter the part in the announce URL you would like to change:\n")
changeTo = input("What would you like it to be instead?\n")

directory = os.getcwd()
print("Starting...\n")
for filename in os.listdir(directory):
    fileExtension = pathlib.Path(filename).suffix
    if(fileExtension == ".torrent"):
        #Obtain .torrent file
        currentFile = os.path.basename(filename)
        print("File found: ", currentFile)
        torrent = Torrent.from_file(currentFile)
        path = torrent.announce_urls[0][0]

        #Edit .torrent file
        print("old URL:", path)
        path = path.replace(changeFrom, changeTo)
        print("new URL:", path)
        torrent.announce_urls = path #Modify torrent announce url

        #Save changes
        torrent.to_file() #Save changes to file
    else:
        print("ERROR! File >", filename, "< is not a torrent file. skipping to next file.")


input("\n\nCompleted!\nPress enter to exit the program.")
