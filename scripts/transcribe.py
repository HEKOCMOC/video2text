"""
Transcribe audio/video to text using Whisper.
Suited for lectures: one file → full text transcript.
"""
from argparse import ArgumentParser
from pathlib import Path

import whisper


def main():
    parser = ArgumentParser(description="Transcribe audio or video to text")
    parser.add_argument(
        "path",
        type=Path,
        help="Path to .mp3, .mp4, .wav, etc.",
    )
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        default="base",
        choices=["tiny", "base", "small", "medium", "large", "large-v2", "large-v3"],
        help="Whisper model size: tiny is faster, large is more accurate (default: base)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output .txt file. If omitted, text is printed to stdout",
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        default=None,
        help="Audio language (e.g. ru, en). Omit for auto-detect",
    )
    args = parser.parse_args()

    path = args.path.resolve()
    if not path.exists():
        parser.error(f"File not found: {path}")

    print(f"Loading Whisper model '{args.model}'...")
    model = whisper.load_model(args.model)

    print(f"Transcribing: {path}")
    result = model.transcribe(
        str(path),
        language=args.language,
        fp16=False,  # more stable on CPU
    )

    text = result["text"].strip()
    if args.output:
        out = args.output.resolve()
        out.write_text(text, encoding="utf-8")
        print(f"Saved to: {out}")
    else:
        print("\n--- Transcript ---\n")
        print(text)


if __name__ == "__main__":
    main()
