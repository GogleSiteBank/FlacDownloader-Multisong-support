import yt_dlp
from youtube_search import YoutubeSearch as search
import os
config = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'flac',
    }]
}

os.system("") ## Windows is stupid and requires us to run a command to allow ansi codes.

def useterminal(): ## function for not using the file 'songs.txt'
    songs = []
    get = input("\u001b[36mMultiple songs?(y/n) \u001b[33m").lower()
    if get == "y":
        num = input("\u001b[34mNumber of songs to download: ")
        isnum = num.isnumeric()
        inum = int(num)
        if isnum == True:
            for i in range(inum):
                song = (f"https://youtube.com/watch?v=" +
                        str(search(input(f"\u001b[35mInput song ({i + 1}): \u001b[33m"),
                                   max_results=10).to_dict()).replace("[{'id': '", "").split("', 't", 1)[0])
                songs.append(song)
            for song in songs:
                try:
                    with yt_dlp.YoutubeDL(config) as down:
                        down.download([song])
                except yt_dlp.utils.DownloadError as e:
                    print(f"\x1b[31mffmpeg is not installed, please install here: https://ffmpeg.org/")
                except Exception as e:
                    if input("Unkown error, would you like to print it?(y/n): ").lower() == "y":
                        print(f"\x1b[31mERROR BELOW: \n{e}")
    elif get == "n":
        song = (f"https://youtube.com/watch?v=" +
                str(search(input(f"\u001b[35mInput song: \u001b[33m"), max_results=10).to_dict()).replace("[{'id': '",
                                                                                                          "").split(
                    "', 't", 1)[0])
        print("\x1b[32m")
        try:
            with yt_dlp.YoutubeDL(config) as down:
                down.download([song])
        except yt_dlp.utils.DownloadError as e:
            print(f"\x1b[31mffmpeg is not installed, please install here: https://ffmpeg.org/")
        except Exception as e:
            if input("Unkown error, would you like to print it?(y/n): ").lower() == "y":
                print(f"\x1b[31mERROR BELOW: \n{e}")
    else:
        print("\u001b[31mInput y or n.")
        useterminal()

def main():
    usefile = input("\u001b[36mRead from file (songs.txt)?(y/n) \u001b[33m").lower()
    if usefile == "n":
        useterminal()
    elif usefile == "y":
        x = 0
        songs = []
        try:
            file = open("songs.txt")
            lines = file.readlines()
            for s in lines:
                x += 1
                print(f"\u001b[35mSong {x}: {s}")
                song = (f"https://youtube.com/watch?v=" + str(search(s).to_dict()).replace("[{'id': '", "").split("', 't", 1)[0])
                songs.append(f"{song}")
            if input("\u001b[36mThese songs will be downloaded (as FLACs) is this correct(y/n) \u001b[33m").lower() == "y":
                for song in songs:
                    try:
                        with yt_dlp.YoutubeDL(config) as down:
                            down.download([song])
                    except yt_dlp.utils.DownloadError as e:
                        print(f"\x1b[31mffmpeg is not installed, please install here: https://ffmpeg.org/")
                    except Exception as e:
                        if input("Unkown error, would you like to print it?(y/n): ").lower() == "y":
                            print(f"\x1b[31mERROR BELOW: \n{e}")
        except FileNotFoundError:
            print("\x1b[31mThe file 'songs.txt' doesn't exist. Please create it.")
        except Exception as e:
            if input("Unkown error, would you like to print it?(y/n): ").lower() == "y":
                print(f"\x1b[31mERROR BELOW: \n{e}")
    else:
        print("\u001b[31mInput y or n.")
        main()
    os.system("color")
    print("")

if __name__ == '__main__':
    main()
