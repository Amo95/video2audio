import os
import sys
import time
import subprocess
import imageio
import moviepy.editor
from textwrap import dedent

imageio.plugins.ffmpeg.download()

def video():
    vid = input("Enter filename: ")
    video = moviepy.editor.VideoFileClip(r"{}".format(vid))
    aud = input("Save file as: ")
    print("Your file is: {}, Press enter to continue".format(aud))
    input()
    conversion(video, audio)
    
def conversion(video, aud):
    audio = video.audio
    audio.write_audiofile(r"{}".format(aud + ".mp3"))
    print("converted successfully")

def readMe():
    """
    Note: in the input prompt, enter filename or location then name file if
    file exists outside a common folder. i.e ~/Desktop/james.mkv

    Note: Also, you can add location then mp3 name to the new file (mp3 format). ie.
    ~/Downloads/james.mp3

    Press Ctrl ^C to cancel
    """
    print(readMe.__doc__)
    time.sleep(10)
    quit()

def quit():
    print("\nDo you want to quit? [Y/n] ", end=" ")
    stop = input()

    if (stop == "" 
            or stop == "Y" 
            or stop == "y"):
        sys.stdout.write("\nThank you for using this script\n")
        exit(1)
    elif stop == "n" or stop == "N":
        main()

def main():
    try:
        location = ["File", "ReadMe"]
        for num, loc in enumerate(location, start=1):
            print(f"[{num}] {loc}")

        entry = int(input("Select option: "))
        if entry == (location.index("File") + 1):
            video()

        elif entry == (location.index("ReadMe") + 1):
            readMe()
        else:
            print("\nInput not found!!\n")
            time.sleep(1)
            main()
    
    except ValueError:
        print(dedent("""
            You enter wrong values
            Please enter number in the select option\n
        """))
        time.sleep(3)
        main()
    except KeyboardInterrupt:
        quit()
    except EOFError:
        quit()

if __name__ == "__main__":
    if (sys.platform == "linux" or
            sys.platform == "linux2"):
        subprocess.call("clear", shell=True)
    else:
        subprocess.call("cls", shell=True)
 
    time.sleep(1)
    with open("./header.txt", "r") as text:
        print(text.read())
    main()

