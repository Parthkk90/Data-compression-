import wave, struct
with wave.open('audio.wav', 'w') as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(44100)
    frames = [0] * 44100
    for s in frames:
        f.writeframes(struct.pack('<h', s))
