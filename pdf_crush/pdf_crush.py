import argparse
import subprocess
import os
import sys

def compress_pdf(input_path, output_path, quality='screen'):
    """
    Compress a PDF using Ghostscript.
    quality options: 'screen', 'ebook', 'printer', 'prepress', 'default'
    'screen' gives the highest compression, 'prepress' the least.
    """
    # Ghostscript command for PDF compression
    gs_command = [
        'gs',
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        f'-dPDFSETTINGS=/{quality}',
        '-dNOPAUSE',
        '-dQUIET',
        '-dBATCH',
        f'-sOutputFile={output_path}',
        input_path
    ]
    try:
        subprocess.run(gs_command, check=True)
    except FileNotFoundError:
        print("Error: Ghostscript (gs) is not installed or not in PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Ghostscript failed: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Compress PDF files for easy sharing via email, preserving image display quality.')
    parser.add_argument('input_pdf', help='Path to the input PDF file')
    parser.add_argument('output_pdf', help='Path to save the compressed PDF')
    parser.add_argument('--quality', choices=['screen', 'ebook', 'printer', 'prepress', 'default'], default='screen',
                        help='Compression quality (default: screen, best for smallest size)')
    args = parser.parse_args()

    if not os.path.isfile(args.input_pdf):
        print(f"Input file {args.input_pdf} does not exist.")
        sys.exit(1)

    compress_pdf(args.input_pdf, args.output_pdf, args.quality)
    print(f"Compressed PDF saved to {args.output_pdf}")

if __name__ == '__main__':
    main()
