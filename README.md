# MarkItDown Converter

A web app that converts any file you upload into Markdown using Microsoft's
[markitdown](https://github.com/microsoft/markitdown), then lets you download the
result.

Supports PDF, Word (.docx), PowerPoint (.pptx), Excel (.xlsx/.xls), HTML, CSV,
JSON, XML, images, audio (with ffmpeg), ZIP, EPUB, and more.

## Live app

Hosted at **<https://markdown.fomatecoslutions.com>** (subdomain of
`fomatecoslutions.com`).

- **Drag & drop** a file (or click to browse).
- **Preview Markdown** shows the result inline.
- **Convert & Download .md** saves the converted file.

## Run it locally

```powershell
pip install -r requirements.txt
python app.py
```

Then open <http://127.0.0.1:5000> in your browser.

## Notes

- Max upload size is 100 MB (change `MAX_CONTENT_LENGTH` in `app.py`).
- Audio transcription needs `ffmpeg` on your PATH: `winget install Gyan.FFmpeg`.
- Files are converted in a temp file that is deleted right after conversion.
