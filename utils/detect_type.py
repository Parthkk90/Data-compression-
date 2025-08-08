# utils/detect_type.py

import os
import mimetypes

try:
    import magic  # python-magic for MIME detection
    MAGIC_AVAILABLE = True
except ImportError:
    MAGIC_AVAILABLE = False

def detect_file_type(file_path: str) -> str:
    """
    Detects the general file type: text, image, audio, video, csv, binary.
    Falls back to extension check if libmagic is unavailable.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    mime_type = None

    # Try python-magic first
    if MAGIC_AVAILABLE:
        mime_type = magic.Magic(mime=True).from_file(file_path)

    # Fallback to mimetypes
    if not mime_type:
        mime_type, _ = mimetypes.guess_type(file_path)

    if not mime_type:
        return "unknown"

    if "text" in mime_type:
        # Check specifically for CSV
        if file_path.lower().endswith(".csv"):
            return "csv"
        return "text"
    elif "image" in mime_type:
        return "image"
    elif "audio" in mime_type:
        return "audio"
    elif "video" in mime_type:
        return "video"
    elif mime_type in ["application/vnd.ms-excel", "text/csv"]:
        return "csv"
    else:
        return "binary"
