import numpy as np
import sounddevice as sd

talking_frames = 0
TRIGGER_VOLUME = 15

def callback(indata, frames, time, status):
    global talking_frames
    volume_norm = np.linalg.norm(indata) * 10
    # print(f"Loudness: {round(volume_norm*1000)/1000}")
    if volume_norm > TRIGGER_VOLUME:
        talking_frames = 12

stream = sd.InputStream(callback=callback)
stream.start()
