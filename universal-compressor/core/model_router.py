from models import image_vqvae, text_compressor, audio_vqvae
def route_and_compress(path: str, fileinfo: dict):
    cat = fileinfo.get('category')
    if cat == 'image':
        return image_vqvae.compress_image(path)
    elif cat == 'text':
        return text_compressor.compress_text(path)
    elif cat == 'audio':
        return audio_vqvae.compress_audio(path)
    else:
        raise NotImplementedError(f"No compressor for category: {cat}")
