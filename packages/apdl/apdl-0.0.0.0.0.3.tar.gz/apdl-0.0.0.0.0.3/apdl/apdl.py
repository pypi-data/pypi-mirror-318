import argparse
import requests
import re
import json
import time
import itertools
from fake_useragent import UserAgent
from colorama import init, Fore
import threading

# Initialize colorama
init(autoreset=True)

ua = UserAgent().chrome
request = requests.Session()


def display_animation(message, done_event):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done_event.is_set():
            break
        print(f"\r{Fore.CYAN}{message} {c}", end='', flush=True)
        time.sleep(0.1)
    print("\r", end='')  # Clear the line after the animation stops


def fetch_video_info(url):
    vid = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url).group(1) if re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url) else None
    if not vid:
        raise ValueError(f"{Fore.RED}Invalid YouTube URL.")

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

    print(f"{Fore.GREEN}Initiating conversion for {selected_quality}: ID {x2}")
    
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
            print(f"{Fore.GREEN}Conversion completed: {Fore.CYAN}Download link - {download_link}")
            break
        else:
            time.sleep(1)  # Add delay to reduce status check frequency


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
            print(f"{Fore.RED}Invalid MP3 quality. Available: {', '.join(qualities.keys())}")
    else:
        print(f"{Fore.GREEN}Available MP3 Qualities: {', '.join(qualities.keys())}")


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
            print(f"{Fore.RED}Invalid MP4 quality. Available: {', '.join(qualities.keys())}")
    else:
        print(f"{Fore.GREEN}Available MP4 Qualities: {', '.join(qualities.keys())}")


def main():
    parser = argparse.ArgumentParser(description="YouTube Downloader CLI")
    parser.add_argument('-url', type=str, required=True, help='YouTube video URL')
    parser.add_argument('-mp3', nargs='?', const=True, default=False, help='Download audio (MP3). Optionally specify quality (64/128/192/256/320)')
    parser.add_argument('-mp4', nargs='?', const=True, default=False, help='Download video (MP4). Optionally specify quality (1080/720/480/360)')

    args = parser.parse_args()

    try:
        video_info, auth = fetch_video_info(args.url)

        if args.mp3:
            if args.mp3 is True:
                mp3_mode(video_info, auth)
            else:
                mp3_mode(video_info, auth, args.mp3)
        elif args.mp4:
            if args.mp4 is True:
                mp4_mode(video_info, auth)
            else:
                mp4_mode(video_info, auth, args.mp4)
        else:
            print(f"{Fore.RED}Please specify either -mp3 or -mp4 option.")

    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED}Network unavailable, please check your connection.")
    except ValueError as e:
        print(e)
    except KeyError as e:
        print(f"{Fore.RED}Missing expected data: {e}")


if __name__ == "__main__":
    main()
