# Five-Element (Wu Xing) Harmony System 

Five-Element Facial Expression Recognition
---
Running `video.py` will automatically open the camera to detect facial expressions and upload them to the server for processing and recognition.


Five-Element Music Style Transfer
---
Replace the `input.wav` file in the folder with the music you want to transform, and rename the file to `input.wav`. The system will then use the results of your facial expression recognition to transform the uploaded music into a corresponding Five Elements music style. Please ensure that the uploaded music is within 20 seconds in length.
See this video for demonstration:
https://github.com/user-attachments/assets/353e5bc7-fdf7-40aa-b36e-889a0854861b


Five-Element Chat
---
Please follow the instructions provided in this link: https://github.com/michael-wzhu/ChatMed to deploy the ChatMedConsult conversation model, and then use the text in our `prompt.txt` as the system prompt.

Five-Element Music Generation
---
Please enter the following command in the terminal    
`cd musicgen`   
`sudo apt-get install ffmpeg`    
`pip install reuiqrements.txt`   
Then open `musicgen.py`, in `description`, you can change the prompt in the `description` to the music prompt generated in Five-Element Chat, and then change the `earth` in `torchaudio.load('./earth.wav')` to the corresponding five-element music type. Then run `musicgen.py` to generate music.
