import json

def wrap_ppc(data_bytes, output_path, ftype="text"):
    payload = {
        "type": ftype,
        "content": data_bytes.hex()
    }
    with open(output_path, "w") as f:
        json.dump(payload, f)

def unwrap_ppc(input_path):
    with open(input_path, "r") as f:
        payload = json.load(f)
    payload["content"] = bytes.fromhex(payload["content"])
    return payload
