# MarkItDown Converter

A tiny local web app that converts any file you upload into Markdown using
Microsoft's [markitdown](https://github.com/microsoft/markitdown), then lets you
download the result.

Supports PDF, Word (.docx), PowerPoint (.pptx), Excel (.xlsx/.xls), HTML, CSV,
JSON, XML, images, audio (with ffmpeg), ZIP, EPUB, and more.

## Run it

```powershell
python app.py
```

Then open <http://127.0.0.1:5000> in your browser.

- **Drag & drop** a file (or click to browse).
- **Preview Markdown** shows the result inline.
- **Convert & Download .md** saves the converted file.

## Install (if starting fresh)

```powershell
pip install -r requirements.txt
```

## Notes

- Max upload size is 100 MB (change `MAX_CONTENT_LENGTH` in `app.py`).
- Audio transcription needs `ffmpeg` on your PATH: `winget install Gyan.FFmpeg`.
- Runs locally only (`127.0.0.1`). Files are converted in a temp file that is
  deleted right after conversion.
