import os
import sys
import time
from textwrap import dedent
import moviepy.editor as mp


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = (
    '\33[94m', '\033[91m',
    '\33[97m', '\33[93m',
    '\033[1;35m', '\033[1;32m',
    '\033[0m')

def help():
    """
    1. Enter name of video file together with the extension
    2. begin with location if file is located somewnere
    """
    print(YELLOW + help.__doc__ +  END)
    time.sleep(5)
    close()

def info():
    """
    Coder: Amo James
    Github: amo95
    Twitter: @dummyCod3r_
    """
    print(info.__doc__)

def spin():
    while True:
        for cursor in '|/-\\':
            yield cursor


def start_spin():
    spinner = spin()
    for _ in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def close():
    entry = input("\nDo you want to quit [Yes/No]? ")
    if entry == "Yes":
        sys.exit(1)
    elif entry == "No":
        startHere()
    else:
        print(dedent("""Are you serious right now?
        You entered nothing dude!"""))

def main():
    info()

    print("Enter video name", end=": ")
    vid = input()
    aud = input("Save as: ")


    print("Wait a moment please", end = " ")
    start_spin()
    clip = mp.VideoFileClip(vid).subclip(0,20)
    clip.audio.write_audiofile(aud + ".mp3")
    time.sleep(1)
    close()


if __name__ == '__main__':
    try:
        def startHere():
            os.system("clear")
            start = ["start", "help"]

            for num, begin in enumerate(start, start=1):
                print("[{}] {}".format(num, begin))

            print("\nSelect option:", end=" ")
            entry1 = int(input())

            while True:
                if entry1 == (start.index("start") + 1):
                    os.system("clear")
                    time.sleep(1)
                    main()
                elif entry1 == (start.index("help") + 1):
                    help()
                else:
                    if entry1 == "" or entry1 == " ":
                        print("You entered nothing, reenter: ")
                        time.sleep(1)
                        startHere()
                    else:
                        print("Wrong entry, try again!! ")
                        time.sleep(1)
        startHere()

    except:
        try:
            print("Wrong entry")
            time.sleep(3)
            startHere()
        except:
            close()
