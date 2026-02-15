# video2text

Small framework to download YouTube videos and transcribe speech to text (e.g. for turning lectures into notes).

<hr>

## Planned functionality

- [x] Download video
- [x] Extracting an audio track from a video
- [x] Recognizing sentences from audio (Whisper)

<hr>

## Getting started from scratch

### Prerequisites

- **Python 3.9+**
- **Poetry** (dependency and environment manager)
- **ffmpeg** (required by Whisper for reading audio/video)

### 1. Install Python

Ensure Python 3.9 or newer is installed:

```bash
python3 --version
```

On macOS you can use [Homebrew](https://brew.sh/): `brew install python`. On Windows use the [official installer](https://www.python.org/downloads/) or [winget](https://winget.run/pkg/Python.Python.3.12).

### 2. Install Poetry

Install Poetry using the official installer:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Add Poetry to your `PATH` if needed (the installer usually prints instructions). Verify:

```bash
poetry --version
```

### 3. Clone the repository and enter the project

```bash
git clone https://github.com/<your-username>/video2text.git
cd video2text
```

Replace `<your-username>` with the actual repo owner, or use your fork URL.

### 4. Install ffmpeg

- **macOS:** `brew install ffmpeg`
- **Ubuntu/Debian:** `sudo apt update && sudo apt install ffmpeg`
- **Windows:** `choco install ffmpeg` or [download from ffmpeg.org](https://ffmpeg.org/download.html)

### 5. Install project dependencies

From the project root:

```bash
poetry install
```

This creates a virtual environment and installs all dependencies (yt-dlp, openai-whisper, etc.). To run commands use `poetry run python ...` or activate the shell with `poetry shell` and then run `python ...` directly.

### 6. Run the scripts

Use the commands below (see [Usage](#usage) for more options).

<hr>

## Usage

**1. Download video or audio from YouTube:**

```bash
poetry run python scripts/download.py -u "https://youtube.com/..." -f mp3
```

Files are saved to the `example/` directory.

**2. Transcribe to text:**

```bash
poetry run python scripts/transcribe.py example/your_file.mp3 -o transcript.txt
```

Options: `-m base` (or `tiny` / `small` / `medium` / `large`), `-l ru` for Russian (or omit for auto-detect).

<hr>

## Note

The project uses third-party libraries (yt-dlp, Whisper) rather than reimplementing download and transcription.

## Discussion

If you are interested in the project, feel free to open an issue to discuss :smile:
