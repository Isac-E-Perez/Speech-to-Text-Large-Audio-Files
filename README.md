# Speech to Text (Large Audio Files) Project
### About: 

For this project, I implemented speech to text of large audio files using Python. I used the libraries speech_recognition, os, AudioSegment from pydub, and split_on_silence from pydub.silence which helped me to build the project. 

The split_on_silence() function from pydub.silence module splits the audio data into chunks on the silence. min_silence_len parameter is the minimum length of silence that needs to be present for the split to occur. 

silence_thresh is the threshold where any dBFS (decibels relative to full scale) lower than the number indicated in the code will be considered silence, I have set the average dBFS to minus 14. keep_silence argument is the amount of silence left at the beginning and the end of each chunk detected in milliseconds.

Afterwards, the process is repeated over all the chunks and convert each speech audio into text. Finally all the text is added up all together to a paragraph format.

### Note:

The parameters in the code won't be perfect for all audio files. Mess with the parameters of the code for your unique audio file, if needed.

Be sure that the audio file that you want to convert to text is in the current directory and that it contains english speech.

The audio file also needs to be a .wav file.  
