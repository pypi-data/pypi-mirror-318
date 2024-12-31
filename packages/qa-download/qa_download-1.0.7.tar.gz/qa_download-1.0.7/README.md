# Music Downloader 🎶

**Music Downloader** is a Python-based tool that allows you to effortlessly download music from YouTube, automatically embedding rich metadata, album artwork, and lyrics sourced from Genius. Whether you're building an offline music library or organizing your favorite tracks, **Music Downloader** ensures your music files are well-tagged and enriched with essential information.

## Features

- **Download Audio**: Extracts the best quality audio from YouTube videos and saves them as MP3 files.
- **Download Video**: Fetches high-quality video and audio streams from YouTube and merges them into MP4 files.
- **Embed Metadata**: Automatically embeds metadata such as title, artist, album, and release date into your music files.
- **Fetch Album Artwork**: Retrieves and embeds album artwork from Genius into your MP3 files.
- **Add Lyrics**: Scrapes and embeds lyrics from Genius or a custom lyrics URL into your MP3 files.
- **Colored Logs**: Provides color-coded terminal logs for better readability and status tracking.
- **Minimal and Informative Logging**: Displays essential information and progress updates without overwhelming the terminal.
- **Graceful Error Handling**: Handles interruptions and errors gracefully, ensuring a smooth user experience.

## Installation

You can install **Music Downloader** via `pip`. Ensure you have Python 3.7 or higher installed on your system.

```bash
pip install qa-download
```

## Requirements

- **Python 3.7+**
- **Dependencies**: The required Python packages are automatically installed with the `qa-download` package.

## Usage

Once installed, you can use `music-downloader` directly from the command line. Below are detailed instructions and examples to help you get started.

> **Recommended**: Using the song name (instead of a YouTube URL) yields more accurate metadata from Genius.

### Basic Command Structure

```bash
music-downloader "input" [--output_dir "/path/to/save"] [--lyr "lyrics_url_or_search_term"] [--video]
```

### Downloading by Song Name

Using a song title allows **Music Downloader** to fetch accurate metadata, album artwork, and lyrics from Genius.

```bash
music-downloader "Let Me Down Slowly Alec Benjamin"
```

**Example with Custom Output Directory:**

```bash
music-downloader "Let Me Down Slowly Alec Benjamin" --output_dir "/path/to/save/music"
```

### Downloading by YouTube URL

If you have a specific YouTube URL, you can use it directly. However, using the song title is recommended for richer metadata.

```bash
music-downloader "https://www.youtube.com/watch?v=T3OyeBuD1h0"
```

**Example with Custom Output Directory:**

```bash
music-downloader "https://www.youtube.com/watch?v=T3OyeBuD1h0" --output_dir "/path/to/save/music"
```

### Downloading by YouTube Playlist

To download an entire YouTube playlist, simply provide the playlist URL. **Music Downloader** will download each video in the playlist and attempt to match metadata from Genius for each song.

```bash
music-downloader "https://www.youtube.com/playlist?list=PL3oW2tjiIxvQjL36vHTlFlX-1KeaJKTzC"
```

### Using the `--lyr` Option

The `--lyr` option allows you to specify either a URL to scrape lyrics from or a direct search term for Genius metadata.

#### 1. Providing a Lyrics URL

When you provide a URL (e.g., a Genius lyrics page), **Music Downloader** will scrape the lyrics from that page and embed them into the MP3 file. It will still fetch other metadata like title, artist, and artwork from Genius based on the YouTube video's title.

```bash
music-downloader "https://www.youtube.com/watch?v=T3OyeBuD1h0" --lyr "https://genius.com/Alec-benjamin-let-me-down-slowly-lyrics"
```

#### 2. Providing a Genius Search Term

If `--lyr` is not a URL, **Music Downloader** treats it as a search term to fetch metadata from Genius. This allows you to specify an exact search string for better metadata matching.

```bash
music-downloader "https://www.youtube.com/watch?v=T3OyeBuD1h0" --lyr "Alec Benjamin Let Me Down Slowly"
```

### Downloading as Video (MP4)

By default, **Music Downloader** downloads audio as MP3 files. To download the full video in MP4 format, use the `--video` flag.

```bash
music-downloader "Let Me Down Slowly Alec Benjamin" --video
```

**Example with Custom Output Directory:**

```bash
music-downloader "Let Me Down Slowly Alec Benjamin" --output_dir "/path/to/save/videos" --video
```

### Complete Example Commands

```bash
# Recommended method for best metadata
music-downloader "Let Me Down Slowly Alec Benjamin"

# Using a single YouTube video URL
music-downloader "https://www.youtube.com/watch?v=T3OyeBuD1h0"

# Using a YouTube playlist URL
music-downloader "https://www.youtube.com/playlist?list=PL3oW2tjiIxvQjL36vHTlFlX-1KeaJKTzC"

# Downloading with a custom lyrics URL
music-downloader "https://www.youtube.com/watch?v=T3OyeBuD1h0" --lyr "https://genius.com/Alec-benjamin-let-me-down-slowly-lyrics"

# Downloading with a custom Genius search term
music-downloader "https://www.youtube.com/watch?v=T3OyeBuD1h0" --lyr "Alec Benjamin Let Me Down Slowly"

# Downloading as MP4 with custom output directory
music-downloader "Let Me Down Slowly Alec Benjamin" --output_dir "/path/to/save/videos" --video
```

## Command-Line Options

- **`input`**: The YouTube URL, playlist URL, or song title you want to download.
- **`--output_dir`**: Specifies a custom directory to save the downloaded file. Defaults to your system's Music directory.
- **`--lyr`**:
  - **If URL**: Scrapes lyrics from the provided URL and embeds them into the MP3.
  - **If not URL**: Treats the input as a search term to fetch metadata from Genius.
- **`--video`**: Downloads the best quality video (MP4) instead of MP3 audio.

## Development

If you'd like to contribute or experiment with the code, follow these steps:

1. **Fork the Repository**: Click the "Fork" button on the repository's GitHub page to create your own copy.
2. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/music_downloader.git
    cd music_downloader
    ```
3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Downloader Locally**:
    ```bash
    python -m music_downloader.downloader "Song Title"
    ```

### Contributing

We welcome contributions to enhance **Music Downloader**! To contribute:

1. **Fork the Repository**.
2. **Create a New Branch** for your feature or bugfix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Make Your Changes**: Ensure all code is properly documented and tested.
4. **Commit Your Changes**:
    ```bash
    git commit -m "Add feature: Your Feature Description"
    ```
5. **Push to Your Fork**:
    ```bash
    git push origin feature/your-feature-name
    ```
6. **Submit a Pull Request**: Provide a detailed explanation of your changes.

Please ensure your contributions align with the project’s code style and conventions. Feel free to open an issue if you'd like to discuss your contribution before starting.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Utilizes [yt-dlp](https://github.com/yt-dlp/yt-dlp) for downloading YouTube audio and video.
- Metadata and lyrics sourced from [Genius](https://genius.com/).
- Colored terminal outputs powered by [colorama](https://pypi.org/project/colorama/).

## Support

For issues or feature requests, please open an issue on [GitHub](https://github.com/yourusername/music_downloader/issues).

---

## Additional Notes

- **Dependencies**: Ensure all required Python packages are installed. They are typically handled automatically when installing via `pip`, but you can manually install them if needed:
    ```bash
    pip install yt-dlp mutagen requests beautifulsoup4 colorama
    ```

- **MP4 Metadata**: Currently, embedding metadata into MP4 files is not handled. If you need this feature, consider integrating libraries like `mutagen.mp4` or other specialized tools.

- **Network Reliability**: Ensure you have a stable internet connection while using **Music Downloader** to prevent interruptions during downloads.
