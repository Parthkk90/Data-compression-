import argparse
import os
import sys
from pathlib import Path

# Import modules (you'll create these later)
# from modules import image_compressor, text_compressor, audio_compressor

def detect_file_type(file_path: Path) -> str:
    ext = file_path.suffix.lower()
    if ext in ['.png', '.jpg', '.jpeg']:
        return "image"
    elif ext in ['.txt', '.csv', '.json']:
        return "text"
    elif ext in ['.wav']:
        return "audio"
    elif ext == '.ppc':
        return "ppc"
    else:
        return "unknown"

def compress(file_path: Path):
    file_type = detect_file_type(file_path)
    print(f"[INFO] Detected file type: {file_type}")
    # Placeholder — later call the AI compression model
    output_file = file_path.with_suffix('.ppc')
    with open(file_path, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.write(f_in.read())  # Temporary: just copies
    print(f"[SUCCESS] Compressed to {output_file}")

def decompress(file_path: Path):
    if file_path.suffix != '.ppc':
        print("[ERROR] File is not a .ppc file.")
        sys.exit(1)
    # Placeholder — later call the AI decompression model
    output_file = file_path.with_suffix('.decompressed')
    with open(file_path, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.write(f_in.read())  # Temporary: just copies
    print(f"[SUCCESS] Decompressed to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Pied Piper Universal Compressor CLI")
    parser.add_argument("command", choices=["compress", "decompress"], help="Action to perform")
    parser.add_argument("file", type=str, help="Path to file")
    args = parser.parse_args()

    file_path = Path(args.file)

    if not file_path.exists():
        print(f"[ERROR] File not found: {file_path}")
        sys.exit(1)

    if args.command == "compress":
        compress(file_path)
    elif args.command == "decompress":
        decompress(file_path)

if __name__ == "__main__":
    main()
