import mimetypes

def detect_file_type(path):
    mime, _ = mimetypes.guess_type(path)
    if mime:
        if "text" in mime or "csv" in mime or "json" in mime:
            return "text"
        elif "image" in mime:
            return "image"
        elif "audio" in mime:
            return "audio"
    return "unknown"
