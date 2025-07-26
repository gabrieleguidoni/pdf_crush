# PDF Crush

A simple command-line tool to compress PDF files for easy sharing via email, while preserving image display quality.

## Features
- Compresses large PDF files to make them easily transferable.
- Lets you choose the compression quality (balance size and quality).
- Preserves the display quality of images as much as possible.

## Requirements
- Python 3.x
- [Ghostscript](https://www.ghostscript.com/) (must be installed and accessible as `gs` in your PATH)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/gabrieleguidoni/pdf_crush.git
   cd pdf_crush
   ```

2. **Install Ghostscript:**
   - On macOS (with Homebrew):
     ```sh
     brew install ghostscript
     ```
   - On Ubuntu/Debian:
     ```sh
     sudo apt-get install ghostscript
     ```
   - [Other platforms](https://www.ghostscript.com/download/gsdnld.html)

3. **(Optional) Create a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **No additional Python packages are required for basic functionality.**

## Usage

```sh
python3 pdf_crush.py <input.pdf> <output.pdf> [--quality QUALITY]
```

- `<input.pdf>`: Path to your source PDF file.
- `<output.pdf>`: Path where the compressed PDF will be saved.
- `--quality QUALITY`: Compression quality (optional, default is `screen`). Options are:
  - `screen` (highest compression, smallest size)
  - `ebook`
  - `printer`
  - `prepress` (least compression, best quality)
  - `default`

### Example

```sh
python3 pdf_crush.py /path/to/large.pdf /path/to/compressed.pdf --quality ebook
```

## Notes
- The tool uses Ghostscript under the hood for compression.
- The `screen` setting is usually best for email attachments.
- If you encounter errors about Ghostscript, make sure it is installed and accessible from your terminal as `gs`.

## License
MIT
