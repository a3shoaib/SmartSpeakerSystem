# Smart Reactive Speaker System

## Overview
An Embedded system powered by a Raspberry Pi 4, consisting of a small display, speaker, and camera. The camera scans the user’s face for a dominant emotion - which then selects music pertaining tp that emotion. Relevant information is then displayed: type of music, user mood, volume. The system contains dynamic screen lighting which changes the colour of the screen based on the user's emotion and shade of colour based on their audio level. 

![Image of System:](images/IMG_4093 (1).jpg)

## Architecture/Technical Details
The system consists of the following modules: main, backend, emotion detection, UI. 

The main module is called by a shell script, and starts the system by linking all the above-mentioned modules. These modules are run as sub-processes (using Python’s built-in subprocess module) of the main module to allow for responsive and parallel processing.

The backend module is responsible for music recommendation and audio. When an emotion is detected, it uses the YouTube Music API to play the music using VLC (due to its control over audio stream). When audio commands are received the backend module translate those commands into VLC commands to change the audio volume. 

The emotion detection module is responsible for detecing the user's facial expression. It uses OpenCV to detect a face and then uses the DeepFace library to detect the most dominant expression. Each frame is read in grayscale and passed to the Deepface library which returns many emotions each with acorresponding float value from 0-1, based on the dominance of each emotion. 

The UI module is responsible for rendering the UI which displays relevant information and showcasing the dynamic lighting feature (as stated in the overview). It was built using the Tkinter library (for performance reasons on the Raspberry Pi). When updated the emotion state and song information is received UI responsively updates to reflect the new information. Based on the emotion of the user, the background and UI elements slowly change to a new colour. Once the target color is reached, it pulses slowly to give a feeling of liveliness to the user. 

## Testing
The system was tested with all emotions that are detected by the DeepFace library. Furthermore, the dynamic lighting feature and UI were tested with every emotion input field and colour. An example of a test is shown: 

![ezgif com-video-to-gif-converter](https://github.com/a3shoaib/SmartSpeakerSystem/assets/112360617/f6ea2734-3cee-44a5-acc3-408908e6ff8f)
