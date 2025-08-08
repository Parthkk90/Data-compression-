try:
    import ipfshttpclient
except:
    ipfshttpclient = None
def upload_file(path: str):
    if ipfshttpclient is None:
        raise RuntimeError('ipfshttpclient not installed')
    return ipfshttpclient.connect().add(path)
def download_cid(cid: str, out_path: str):
    if ipfshttpclient is None:
        raise RuntimeError('ipfshttpclient not installed')
    ipfshttpclient.connect().get(cid, target=out_path)
    return out_path
