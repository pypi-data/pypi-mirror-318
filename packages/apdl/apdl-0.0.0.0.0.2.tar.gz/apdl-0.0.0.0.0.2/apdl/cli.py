import argparse
import requests
import re
import json
import time
import itertools
from fake_useragent import UserAgent
import threading
import sys

# Colorama-style color definitions
W = '\x1b[1;97m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
Y = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'

ua = UserAgent().chrome
request = requests.Session()


def display_animation(message, done_event):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done_event.is_set():
            break
        print(f"\r{O}{message} {c}{N}", end='', flush=True)
        time.sleep(0.1)
    print("\r", end='')  # Clear the line after the animation stops


def fetch_video_info(url):
    if not url:
        raise ValueError(f"{R}YouTube URL is required. Use -url <YouTube Video URL>{N}")
    
    vid = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    if not vid:
        raise ValueError(f"{R}Invalid YouTube URL format. Please check your input.{N}")
    vid = vid.group(1)
    xx = request.get(f"https://rr-01-bucket.cdn1313.net/api/v4/info/{vid}", headers={
        'User-Agent': ua,
        'origin': "https://apidl.net",
        'referer': "https://apidl.net/",
        'connection': "keep-alive"
    })
    return xx.json(), xx.headers.get('authorization')


def download_format(selected_quality, qualities, auth):
    token = qualities[selected_quality]["token"]
    x2 = request.post("https://rr-01-bucket.cdn1313.net/api/v4/convert", data=json.dumps({"token": token}), headers={
        'User-Agent': ua,
        'Content-Type': "application/json",
        'authorization': auth,
        'origin': "https://apidl.net",
        'referer': "https://apidl.net/",
        'connection': "keep-alive"
    }).json()["id"]

    print(f"{G}Initiating conversion for {selected_quality}: ID {x2}{N}")
    
    done_event = threading.Event()
    animation_thread = threading.Thread(target=display_animation, args=("Converting", done_event))
    animation_thread.start()

    while True:
        get = request.get(f"https://rr-01-bucket.cdn1313.net/api/v4/status/{x2}", headers={
            'User-Agent': ua,
            'authorization': auth,
            'origin': "https://apidl.net",
            'referer': "https://apidl.net/",
            'connection': "keep-alive"
        })
        status = get.json()
        if status.get("status") == "completed" or status.get("progress") == 100:
            done_event.set()
            animation_thread.join()
            download_link = status.get("download")
            if download_link:
                print(f"{G}Conversion completed: {O}Download link - {download_link}{N}")
            else:
                print(f"{R}No download link found. Please try again.{N}")
            break
        else:
            time.sleep(1)


def display_available_qualities(video_info):
    mp3_qualities = [str(q) for q in ["64", "128", "192", "256", "320"]]
    mp4_qualities = [str(q) for q in ["1080", "720", "480", "360"]]

    print(f"{G}Available MP3 Qualities: {', '.join(mp3_qualities)}{N}")
    print(f"{G}Available MP4 Qualities: {', '.join(mp4_qualities)}{N}")



def thumbnail_mode(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    if not match:
        print(f"{R}Invalid YouTube URL.{N}")
        return
    vid = match.group(1)
    thumbnail_url = f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg"
    response = requests.head(thumbnail_url)
    if response.status_code == 200:
        print(f"{G}Thumbnail URL: {thumbnail_url}{N}")
    else:
        print(f"{R}No thumbnail found for the given video.{N}")


def mp3_mode(video_info, auth, quality=None):
    mp3_formats = video_info["formats"]["audio"]["mp3"]
    qualities = {
        "64": mp3_formats[4],
        "128": mp3_formats[3],
        "192": mp3_formats[2],
        "256": mp3_formats[1],
        "320": mp3_formats[0],
    }

    if quality:
        if quality in qualities:
            download_format(quality, qualities, auth)
        else:
            print(f"{R}Invalid MP3 quality. Available: {', '.join(qualities.keys())}{N}")
    else:
        print(f"{G}Available MP3 Qualities: {', '.join(qualities.keys())}{N}")


def mp4_mode(video_info, auth, quality=None):
    mp4_formats = video_info["formats"]["video"]["mp4"]
    qualities = {
        "1080": mp4_formats[0],
        "720": mp4_formats[1],
        "480": mp4_formats[2],
        "360": mp4_formats[3],
    }

    if quality:
        if quality in qualities:
            download_format(quality, qualities, auth)
        else:
            print(f"{R}Invalid MP4 quality. Available: {', '.join(qualities.keys())}{N}")
    else:
        print(f"{G}Available MP4 Qualities: {', '.join(qualities.keys())}{N}")


def main():
    parser = argparse.ArgumentParser(description="apdl - YouTube Downloads & Details")
    parser.add_argument('-url', type=str, help='YouTube video URL')
    parser.add_argument('-mp3', nargs='?', const=True, default=False, help='Download audio (MP3)')
    parser.add_argument('-mp4', nargs='?', const=True, default=False, help='Download video (MP4)')
    parser.add_argument('-title', action='store_true', help='Display video title')
    parser.add_argument('-thumbnail', action='store_true', help='Display video thumbnail URL')
    parser.add_argument('-list', action='store_true', help='List available MP3 and MP4 qualities')

    args = parser.parse_args()

    # Handle cases where no URL is provided
    if not args.url:
        if len(sys.argv) == 1:  # No arguments provided
            parser.print_usage()
            print(f"{R}Error: -url argument is required.{N}")
        elif args.url is None:  # -url argument is provided without value
            print(f"{R}Error: Please provide a valid YouTube URL with -url option.{N}")
        sys.exit(1)

    try:
        video_info, auth = fetch_video_info(args.url)

        if args.list:
            display_available_qualities(video_info)
        elif args.title:
            print(f"{G}Video Title: {video_info.get('title', 'Unknown')}{N}")
        elif args.thumbnail:
            if not args.url:
                print(f"{R}Error: Please provide a URL with -url when using -thumbnail.{N}")
            else:
                thumbnail_mode(args.url)
        elif args.mp3:
            if not args.mp3:
                print(f"{Y}Please specify the MP3 quality. Use -list to view available qualities.{N}")
            mp3_mode(video_info, auth, args.mp3 if args.mp3 is not True else None)
        elif args.mp4:
            if not args.mp4:
                print(f"{Y}Please specify the MP4 quality. Use -list to view available qualities.{N}")
            mp4_mode(video_info, auth, args.mp4 if args.mp4 is not True else None)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"{R}Unexpected error: {e}{N}")
    except KeyboardInterrupt:
        exit()
    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED}Network unavailable, please check your connection.")


if __name__ == "__main__":
    main()
