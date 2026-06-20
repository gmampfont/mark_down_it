"""
MarkItDown Converter — a tiny web app.

Upload any file, it gets converted to Markdown with Microsoft's markitdown,
and you can download the result.

Run:  python app.py
Then open http://127.0.0.1:5000 in your browser.
"""

import io
import os
import tempfile
import traceback

from flask import (
    Flask,
    render_template,
    request,
    send_file,
    jsonify,
)
from markitdown import MarkItDown

app = Flask(__name__)

# Max upload size: 100 MB. Bump this if you need to convert larger files.
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024

# One shared converter instance is fine and avoids reloading models per request.
_converter = MarkItDown()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    if "file" not in request.files:
        return jsonify(error="No file was uploaded."), 400

    upload = request.files["file"]
    if not upload.filename:
        return jsonify(error="No file was selected."), 400

    # markitdown picks the right converter from the file extension / content,
    # so we keep the original suffix on the temp file.
    suffix = os.path.splitext(upload.filename)[1]
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            upload.save(tmp.name)
            tmp_path = tmp.name

        result = _converter.convert(tmp_path)
        markdown = result.text_content or ""
    except Exception as exc:  # surface a readable error to the browser
        traceback.print_exc()
        return jsonify(error=f"Could not convert this file: {exc}"), 422
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)

    download_name = os.path.splitext(upload.filename)[0] + ".md"

    # If the client asked for a download, stream the .md back as an attachment.
    if request.form.get("download") == "1":
        buffer = io.BytesIO(markdown.encode("utf-8"))
        return send_file(
            buffer,
            mimetype="text/markdown",
            as_attachment=True,
            download_name=download_name,
        )

    # Otherwise return JSON so the page can show a preview.
    return jsonify(markdown=markdown, download_name=download_name)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
