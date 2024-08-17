# Five-Element (Wu Xing) Harmony System 

## Executive Summary

### Deficiencies in Existing Oriental Music Therapy:
Current practices in Oriental music therapy, particularly within the framework of Five-Element Music Therapy (FEMT) based on traditional Chinese medicine, face several significant challenges. Unlike Western music therapy, which has seen increasing integration with technology and scientific validation, Oriental music therapy remains largely untouched by technological advancements. This results in a lack of personalization and accessibility, as traditional FEMT depends heavily on the expertise of the therapist to select music that aligns with the patient’s unique physical and emotional states. Without modern tools, the potential for widespread adoption is limited, as many patients do not have access to highly skilled practitioners.

Additionally, there is a scientific gap in validating the therapeutic efficacy of FEMT. With limited empirical studies and the absence of technology-enhanced tools, Oriental music therapy lacks the scalability and reproducibility seen in its Western counterpart. Furthermore, the therapeutic repertoire in FEMT is more restricted, and there is no standardized system to dynamically match the changing needs of the patient with the appropriate therapeutic music, often resulting in mismatches in treatment.

### How the Five-Element Harmony System Solves These Issues:
The Five-Element Harmony System bridges the technological gap in Oriental music therapy by integrating advanced AI tools, such as facial emotion recognition and dynamic music generation, into traditional FEMT. This system revolutionizes personalization in music therapy by continuously analyzing a patient’s emotional state in real-time and adjusting the music accordingly, ensuring that the therapy is always aligned with the patient’s current condition. It eliminates the need for expert practitioners to manually select the music, making FEMT more accessible to a wider audience.

By using AI, the system also expands the therapeutic repertoire available in FEMT, generating appropriate music that fits within the Five-Element framework and addressing the limitation of restricted musical selections. Furthermore, the tool adds a layer of scientific rigor to Oriental music therapy, as its data-driven approach can be validated through empirical studies, bringing FEMT closer to the scientifically supported frameworks found in Western music therapy. This technological integration not only enhances the effectiveness of music therapy within traditional Chinese medicine but also opens the door to scalable, reproducible, and personalized treatments that can compete with modern Western methods.

![Five-Element Harmony System](https://github.com/everydaylucky/Wu_Xing_Harmony_System/blob/main/newimg.png)

## Five-Element Facial Expression Recognition

Running `video.py` will automatically open the camera to detect facial expressions and upload them to the server for processing and recognition.


## Five-Element Music Style Transfer

Replace the `input.wav` file in the folder with the music you want to transform, and rename the file to `input.wav`. The system will then use the results of your facial expression recognition to transform the uploaded music into a corresponding Five Elements music style. Please ensure that the uploaded music is within 20 seconds in length.
See this video for demonstration:
https://github.com/user-attachments/assets/353e5bc7-fdf7-40aa-b36e-889a0854861b


## Five-Element Chat

Please follow the instructions provided in this link: https://github.com/michael-wzhu/ChatMed to deploy the ChatMedConsult conversation model, and then use the text in our `prompt.txt` as the system prompt.

## Five-Element Music Generation

Please enter the following command in the terminal    
`cd musicgen`   
`sudo apt-get install ffmpeg`    
`pip install reuiqrements.txt`   
Then open `musicgen.py`, in `description`, you can change the prompt in the `description` to the music prompt generated in Five-Element Chat, and then change the `earth` in `torchaudio.load('./earth.wav')` to the corresponding five-element music type. Then run `musicgen.py` to generate music.
