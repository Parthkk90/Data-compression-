import json, struct, os
MAGIC = b'PPC1'
def create_ppc(out_path: str, payload: bytes, metadata: dict):
    meta_json = json.dumps(metadata).encode('utf-8')
    with open(out_path, 'wb') as f:
        f.write(MAGIC)
        f.write(struct.pack('>I', len(meta_json)))
        f.write(meta_json)
        f.write(payload)
def extract_ppc(ppc_path: str, out_dir: str) -> str:
    with open(ppc_path, 'rb') as f:
        magic = f.read(4)
        if magic != MAGIC:
            raise ValueError("Not a PPC file")
        meta_len = struct.unpack('>I', f.read(4))[0]
        metadata = json.loads(f.read(meta_len).decode('utf-8'))
        payload = f.read()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, metadata.get('original_name', 'restored.bin'))
    with open(out_path, 'wb') as g:
        g.write(payload)
    return out_path
