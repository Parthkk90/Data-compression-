import magic, os
def detect_file_type(path: str) -> dict:
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    mime = magic.from_file(path, mime=True)
    category = 'binary'
    if mime.startswith('image/'):
        category = 'image'
    elif mime.startswith('text/') or mime in ('application/json','application/xml','text/csv'):
        category = 'text'
    elif mime.startswith('audio/'):
        category = 'audio'
    return {'category': category, 'mime': mime, 'subtype': mime.split('/')[-1]}
