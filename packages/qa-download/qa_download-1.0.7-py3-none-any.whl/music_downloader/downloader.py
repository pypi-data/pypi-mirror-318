import argparse
import os
import re
import shutil
import tempfile
import requests
import yt_dlp
from bs4 import BeautifulSoup
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, USLT, APIC
import platform
from urllib.parse import urlparse
import sys
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Replace with your actual Genius API key
GENIUS_API_KEY = 'L0BY-i4ZVi0wQ53vlvm2zucqjHTuLbHv--YgjxJoN0spnEIhb5swTr_mWlQ6Ye-F'

def is_url(string):
    """Check if the provided string is a valid URL."""
    try:
        parsed = urlparse(string)
        return bool(parsed.scheme and parsed.netloc)
    except:
        return False

def sanitize_filename(filename):
    """Sanitize filename to avoid issues with special characters."""
    return re.sub(r'[\\/:"*?<>|]+', "_", filename)

def is_youtube_url(input_string):
    """Check if the input string is a YouTube URL."""
    return "youtube.com" in input_string or "youtu.be" in input_string

def scrape_lyrics_from_url(url):
    """Scrape lyrics directly from the provided page (e.g., Genius or any custom URL)."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Genius.com approach: data-lyrics-container
        containers = soup.find_all("div", attrs={"data-lyrics-container": "true"})
        if containers:
            return "\n".join(div.get_text(separator="\n") for div in containers)
        return soup.get_text(separator="\n")
    except:
        return None

def fetch_genius_metadata(search_term):
    """
    Fetch song metadata (title, artist, album, release_date, artwork, lyrics) from Genius
    using 'search_term'. Returns the first match if available, or None if no hits.
    """
    try:
        headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}
        params = {"q": search_term}
        response = requests.get("https://api.genius.com/search", headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data['response']['hits']:
                hit = data['response']['hits'][0]['result']
                song_url = hit['url']
                art_url = hit['song_art_image_url']
                artist = hit['primary_artist']['name']
                title = hit.get('title_with_featured') or hit.get('title')
                # Scrape official Genius lyrics
                lyrics = scrape_lyrics_from_url(song_url)
                return {
                    "title": title or "Unknown Title",
                    "artist": artist or "Unknown Artist",
                    "album": "Single",
                    "release_date": hit.get('release_date_for_display'),
                    "song_art_url": art_url,
                    "lyrics": lyrics,
                }
    except:
        pass
    return None

def embed_metadata_mp3(file_path, metadata):
    """Embed metadata into MP3 files (ID3 tags)."""
    if not metadata:
        return
    try:
        audio = EasyID3(file_path)
        audio['title'] = metadata.get('title', 'Unknown Title')
        audio['artist'] = metadata.get('artist', 'Unknown Artist')
        audio['album'] = metadata.get('album', 'Unknown Album')
        audio.save()

        audio_id3 = ID3(file_path)
        # Embed lyrics
        if metadata.get('lyrics'):
            audio_id3["USLT"] = USLT(encoding=3, lang='eng', desc='Lyrics', text=metadata['lyrics'])
        # Embed artwork
        if metadata.get('song_art_url'):
            art_resp = requests.get(metadata['song_art_url'], timeout=10)
            art_resp.raise_for_status()
            audio_id3["APIC"] = APIC(
                encoding=3,
                mime='image/jpeg',
                type=3,  # Front cover
                desc='Cover',
                data=art_resp.content
            )
        audio_id3.save()
    except:
        print(Fore.RED + "[ERROR] Failed to embed metadata.")

def download_audio(video_url, output_dir, metadata):
    """Download audio from YouTube, convert to MP3, embed metadata, then move file."""
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            title = sanitize_filename(metadata.get('title', 'audio'))
            output_template = os.path.join(temp_dir, f"{title}.%(ext)s")

            # Define a simple progress hook
            def progress_hook(d):
                if d['status'] == 'downloading':
                    percent = d.get('_percent_str', '0.0%').strip()
                    eta = d.get('eta', 0)
                    sys.stdout.write(f"\r{Fore.BLUE}Downloading audio: {percent} ETA: {eta}s")
                    sys.stdout.flush()
                elif d['status'] == 'finished':
                    sys.stdout.write(f"\r{Fore.GREEN}Downloading audio: 100.0% Completed.\n")
                    sys.stdout.flush()

            ydl_opts = {
                'quiet': True,
                'no_warnings': True,  # Suppress warnings
                'format': 'bestaudio/best',
                'outtmpl': output_template,
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }
                ],
                'progress_hooks': [progress_hook],
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            downloaded_file = os.path.join(temp_dir, f"{title}.mp3")
            if os.path.exists(downloaded_file):
                embed_metadata_mp3(downloaded_file, metadata)
                final_file = os.path.join(output_dir, f"{title}.mp3")
                shutil.move(downloaded_file, final_file)
                print(Fore.GREEN + f"[SUCCESS] Saved MP3 to: {final_file}")
            else:
                print(Fore.RED + "\n[ERROR] Downloaded MP3 file not found.")
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[INFO] Download interrupted by user.")
    except:
        print(Fore.RED + "\n[ERROR] Something went wrong during audio download.")

def download_video(video_url, output_dir, metadata):
    """Download the video at best quality (video + audio) and merge to MP4."""
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            title = sanitize_filename(metadata.get('title', 'video'))
            output_template = os.path.join(temp_dir, f"{title}.%(ext)s")

            # Define a simple progress hook
            def progress_hook(d):
                if d['status'] == 'downloading':
                    percent = d.get('_percent_str', '0.0%').strip()
                    eta = d.get('eta', 0)
                    sys.stdout.write(f"\r{Fore.BLUE}Downloading video: {percent} ETA: {eta}s")
                    sys.stdout.flush()
                elif d['status'] == 'finished':
                    sys.stdout.write(f"\r{Fore.GREEN}Downloading video: 100.0% Completed.\n")
                    sys.stdout.flush()

            ydl_opts = {
                'quiet': True,
                'no_warnings': True,  # Suppress warnings
                'format': 'bv*+ba/b',  # bestvideo + bestaudio fallback
                'outtmpl': output_template,
                'merge_output_format': 'mp4',
                'progress_hooks': [progress_hook],
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            merged_file = os.path.join(temp_dir, f"{title}.mp4")
            if os.path.exists(merged_file):
                final_file = os.path.join(output_dir, f"{title}.mp4")
                shutil.move(merged_file, final_file)
                print(Fore.GREEN + f"[SUCCESS] Saved MP4 to: {final_file}")
            else:
                print(Fore.RED + "\n[ERROR] Downloaded MP4 file not found.")
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[INFO] Download interrupted by user.")
    except:
        print(Fore.RED + "\n[ERROR] Something went wrong during video download.")


def search_youtube(query):
    """Search on YouTube for 'query' and return first match (URL, metadata)."""
    try:
        ydl_opts = {'quiet': True, 'format': 'bestaudio/best', 'noplaylist': True}
        search_url = f"ytsearch:{query}"
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            results = ydl.extract_info(search_url, download=False)
            if 'entries' in results and len(results['entries']) > 0:
                entry = results['entries'][0]
                return entry['webpage_url'], entry
    except:
        pass
    return None, None

def get_youtube_title(url):
    """Fetch the title of the YouTube video."""
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get('title', 'Unknown Title')
    except:
        return 'Unknown Title'

def main():
    try:
        parser = argparse.ArgumentParser(
            description="Download from YouTube (URL or search term) and optionally embed Genius metadata or custom lyrics."
        )

        # Determine default output directory based on OS
        if platform.system().lower().startswith("win"):
            default_output_dir = os.path.join(os.path.expanduser("~"), "Music")
        elif platform.system().lower().startswith("darwin"):
            default_output_dir = os.path.expanduser("~/Music/Music/Media.localized/Automatically Add to Music.localized")
        else:
            default_output_dir = os.path.expanduser("~/Music")

        parser.add_argument("input", help="YouTube URL, playlist URL, or search term.")
        parser.add_argument("--output_dir", default=default_output_dir, help="Where to save the downloaded file.")
        parser.add_argument(
            "--lyr",
            help=(
                "If it's a URL (http/s), scrape lyrics from that page. "
                "If it's NOT a URL, treat it as a search term for Genius metadata."
            ),
            default=None
        )
        parser.add_argument(
            "--video",
            action="store_true",
            help="Download best quality video (MP4) instead of MP3 audio."
        )

        args = parser.parse_args()
        output_dir = os.path.expanduser(args.output_dir)
        os.makedirs(output_dir, exist_ok=True)

        # Step 1: Determine YouTube URL
        if is_youtube_url(args.input):
            youtube_url = args.input
            print(Fore.BLUE + f"[INFO] YouTube URL detected: {youtube_url}")
        else:
            print(Fore.BLUE + f"[INFO] Searching YouTube for: '{args.input}'")
            youtube_url, yt_metadata = search_youtube(args.input)
            if not youtube_url:
                print(Fore.RED + "[ERROR] No YouTube results found.")
                sys.exit(1)
            print(Fore.BLUE + f"[INFO] Found YouTube URL: {youtube_url}")

        # Step 2: Handle --lyr
        genius_meta = None
        custom_lyrics = None

        if args.lyr:
            if is_url(args.lyr):
                # --lyr is a URL: scrape lyrics from it
                print(Fore.BLUE + f"[INFO] Scraping lyrics from URL: {args.lyr}")
                custom_lyrics = scrape_lyrics_from_url(args.lyr)
                if not custom_lyrics:
                    print(Fore.YELLOW + "[WARNING] Could not extract lyrics from the provided URL.")

                # Fetch Genius metadata using YouTube title
                youtube_title = get_youtube_title(youtube_url)
                print(Fore.BLUE + f"[INFO] Fetching Genius metadata using YouTube title: '{youtube_title}'")
                genius_meta = fetch_genius_metadata(youtube_title)
                if genius_meta:
                    print(Fore.GREEN + "[SUCCESS] Genius metadata fetched successfully.")
                else:
                    print(Fore.YELLOW + "[WARNING] Could not fetch Genius metadata using YouTube title.")
                    # Minimal metadata fallback
                    genius_meta = {
                        "title": youtube_title,
                        "artist": "Unknown Artist",
                        "album": "Single",
                        "song_art_url": None,
                        "lyrics": None,
                    }

                # Override lyrics with custom lyrics
                if custom_lyrics:
                    genius_meta["lyrics"] = custom_lyrics
            else:
                # --lyr is a search term: use it to fetch Genius metadata
                print(Fore.BLUE + f"[INFO] Using '--lyr' as Genius search term: '{args.lyr}'")
                genius_meta = fetch_genius_metadata(args.lyr)
                if genius_meta:
                    print(Fore.GREEN + "[SUCCESS] Genius metadata fetched successfully using '--lyr' search term.")
                else:
                    print(Fore.YELLOW + "[WARNING] Could not fetch Genius metadata using '--lyr' search term.")
                    # Fallback to YouTube title
                    youtube_title = get_youtube_title(youtube_url)
                    print(Fore.BLUE + f"[INFO] Fetching Genius metadata using YouTube title: '{youtube_title}'")
                    genius_meta = fetch_genius_metadata(youtube_title)
                    if genius_meta:
                        print(Fore.GREEN + "[SUCCESS] Genius metadata fetched successfully using YouTube title fallback.")
                    else:
                        print(Fore.YELLOW + "[WARNING] Could not fetch Genius metadata using YouTube title fallback.")
                        # Minimal metadata fallback
                        genius_meta = {
                            "title": youtube_title,
                            "artist": "Unknown Artist",
                            "album": "Single",
                            "song_art_url": None,
                            "lyrics": None,
                        }
        else:
            # No --lyr provided: fetch Genius metadata using YouTube title
            youtube_title = get_youtube_title(youtube_url)
            print(Fore.BLUE + f"[INFO] Fetching Genius metadata using YouTube title: '{youtube_title}'")
            genius_meta = fetch_genius_metadata(youtube_title)
            if genius_meta:
                print(Fore.GREEN + "[SUCCESS] Genius metadata fetched successfully.")
            else:
                print(Fore.YELLOW + "[WARNING] Could not fetch Genius metadata using YouTube title.")
                # Minimal metadata fallback
                genius_meta = {
                    "title": youtube_title,
                    "artist": "Unknown Artist",
                    "album": "Single",
                    "song_art_url": None,
                    "lyrics": None,
                }

        # Step 3: Download media
        if args.video:
            print(Fore.BLUE + "[INFO] Starting video download...")
            download_video(youtube_url, output_dir, genius_meta)
        else:
            print(Fore.BLUE + "[INFO] Starting audio download...")
            download_audio(youtube_url, output_dir, genius_meta)

        print(Fore.GREEN + "\n[INFO] All operations completed successfully.\n")

    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[INFO] Process interrupted by user.")
    except:
        print(Fore.RED + "\n[ERROR] Something went wrong. Please try again.")

if __name__ == "__main__":
    main()
