import zlib

def compress(path):
    with open(path, "rb") as f:
        data = f.read()
    return zlib.compress(data)

def decompress(data, output_path):
    with open(output_path, "wb") as f:
        f.write(zlib.decompress(data))
