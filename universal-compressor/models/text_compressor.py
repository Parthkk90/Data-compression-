# import os
# def compress_text(path: str):
#     with open(path, 'rb') as f:
#         raw = f.read()
#     payload = raw[:max(1, len(raw)//2)]
#     meta = {
#         "original_name": os.path.basename(path),
#         "original_size": len(raw),
#         "compressed_size": len(payload),
#         "model": "text_stub_v0"
#     }
#     return payload, meta
import zlib

def compress(path):
    with open(path, "rb") as f:
        data = f.read()
    return zlib.compress(data)

def decompress(data, output_path):
    with open(output_path, "wb") as f:
        f.write(zlib.decompress(data))
