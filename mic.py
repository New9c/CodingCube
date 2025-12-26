import numpy as np
import sounddevice as sd

talking_frames = 0

def callback(indata, frames, time, status):
    global talking_frames
    volume_norm = np.linalg.norm(indata) * 10
    #if SETTINGS["print_loudness"]:
    #print(f"Loudness: {round(volume_norm*1000)/1000}")
    if volume_norm > 2:
        talking_frames = 15

stream = sd.InputStream(callback=callback)
stream.start()
