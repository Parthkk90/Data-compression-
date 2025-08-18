import sys
from core.file_detector import detect_file_type
from core.ppc_wrapper import wrap_ppc, unwrap_ppc
from models import text_compressor, image_compressor, audio_compressor
from storage.ipfs_handler import store_file, retrieve_file


def compress(input_path):
    ftype = detect_file_type(input_path)
    print(f"[INFO] Detected file type: {ftype}")

    if ftype == "text":
        compressed = text_compressor.compress(input_path)
    elif ftype == "image":
        compressed = image_compressor.compress(input_path)
    elif ftype == "audio":
        compressed = audio_compressor.compress(input_path)
    else:
        print("[ERROR] Unsupported file type")
        return

    output_path = input_path.rsplit(".", 1)[0] + ".ppc"
    wrap_ppc(compressed, output_path)
    print(f"[SUCCESS] Compressed to {output_path}")

    cid = store_file(output_path)
    print(f"[INFO] Stored on IPFS with CID: {cid}")


def decompress(ppc_path):
    data = unwrap_ppc(ppc_path)
    ftype = data.get("type")

    if ftype == "text":
        text_compressor.decompress(data["content"], ppc_path.replace(".ppc", ".txt"))
    elif ftype == "image":
        image_compressor.decompress(data["content"], ppc_path.replace(".ppc", ".png"))
    elif ftype == "audio":
        audio_compressor.decompress(data["content"], ppc_path.replace(".ppc", ".wav"))
    else:
        print("[ERROR] Unknown file type in PPC package")
        return

    print(f"[SUCCESS] Decompressed {ppc_path}")


def main():
    if len(sys.argv) < 3:
        print("Usage: pcc <compress|decompress> <file>")
        sys.exit(1)

    action, path = sys.argv[1], sys.argv[2]
    
    path2 = "F:\Data-compression\universal-compressor\data.csv"

    if action == "compress":
        compress(path)
    elif action == "decompress":
        decompress(path)
    elif action == "univerasal-compressor":
        compress(path)
        
    else:
        print(f"[ERROR] Unknown action: {action}")
        sys.exit(1)
        
    
        
    


if __name__ == "__main__":
    main()
