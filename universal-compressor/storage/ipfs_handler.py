# try:
#     import ipfshttpclient
# except:
#     ipfshttpclient = None
# def upload_file(path: str):
#     if ipfshttpclient is None:
#         raise RuntimeError('ipfshttpclient not installed')
#     return ipfshttpclient.connect().add(path)
# def download_cid(cid: str, out_path: str):
#     if ipfshttpclient is None:
#         raise RuntimeError('ipfshttpclient not installed')
#     ipfshttpclient.connect().get(cid, target=out_path)
#     return out_path


import ipfshttpclient

def store_file(path):
    try:
        client = ipfshttpclient.connect()
        res = client.add(path)
        return res["Hash"]
    except Exception as e:
        print(f"[ERROR] IPFS store failed: {e}")
        return None

def retrieve_file(cid, output_path):
    try:
        client = ipfshttpclient.connect()
        client.get(cid, target=output_path)
        return True
    except Exception as e:
        print(f"[ERROR] IPFS retrieve failed: {e}")
        return False
