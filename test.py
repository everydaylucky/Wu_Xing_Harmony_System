from rmn import RMN
import cv2
import requests
import time
import os
import subprocess

m = RMN()
image = cv2.imread("last_frame.jpg")
results = m.detect_emotion_for_single_frame(image)
emotion = results[0]["emo_label"]


if emotion == "angry":
    emotion = "wood"
elif emotion == "disgust" or emotion == "neutral":
    emotion = "earth"
elif emotion == "fear" or emotion == "surprise":
    emotion = "water"
elif emotion == "happy":
    emotion = "fire"
elif emotion == "sad":
    emotion = "metal"


print("current emotions: " + str(emotion))
url = "http://i-2.gpushare.com:56666/upload"
file_path = "input.wav"  # path to file

with open(file_path, "rb") as file:
    files = {
        "file": file,
    }

    data = {"emotion": emotion}

    response = requests.post(url, files=files, data=data)
    # print(response.text)

if emotion == "earth":
    emotion = "wood"
elif emotion == "water":
    emotion = "earth"
elif emotion == "fire":
    emotion = "water"
elif emotion == "metal":
    emotion = "fire"
elif emotion == "wood":
    emotion = "metal"

response = requests.get("http://i-2.gpushare.com:56666/get-file/" + emotion)

if response.text == "no file found":
    print("No file found. ")
else:
    # Save the file
    filename = "audio.wav"
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"File saved as {filename}")

    # Play the file
    try:
        # This uses the default application to open the file
        if os.name == "nt":  # For Windows
            os.startfile(filename)
        elif os.name == "posix":  # For Linux and macOS
            subprocess.call(("xdg-open", filename))
    except Exception as e:
        print(f"Error playing file: {e}")
