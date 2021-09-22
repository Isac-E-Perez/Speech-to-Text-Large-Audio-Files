# importing libraries

import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

root = sr.Recognizer()  # create a speech recognition object


# creating a function that will split the audio file into chucks and apply speech recognition to each chunk

def large_audio(path):
    sound = AudioSegment.from_wav(path)  # opens the audio file using pydub
    chunks = split_on_silence(sound,  # splits the audio sound where silence is 700 milliseconds or more and get chunks
                              min_silence_len=500,  # this could be adjusted (dependent on audio file)
                              silence_thresh=sound.dBFS - 14,  # dependent on audio file
                              keep_silence=500)  # keep hte silence for 1 second (adjustable)

    folder_name = 'audio-chunks'  # create a directory to store the audio chunks

    # os.path - path module suitable for the operating system Python is running on

    if not os.path.isdir(folder_name):  # used to check whether the specified path is an existing directory or not
        os.mkdir(folder_name)  # used to create a directory named path with the specified numeric mode
    whole_text = ""

    for i, audio_chunk in enumerate(chunks, start=1):  # process each chunk (allows to iterate through a sequence
        # but it keeps track of both the index and the element)
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")  # export audio chunk and saves it in (combines one
        # or more path names into a single path
        audio_chunk.export(chunk_filename, format="wav")  # the 'folder_name' directory

        # recognize the chunk

        with sr.AudioFile(chunk_filename) as source:
            audio_listened = root.record(source)

            # try converting audio to text

            try:
                text = root.recognize_google(audio_listened)  # performs speech recognition on audio_listened
            except sr.UnknownValueError as e:
                print("Error: ", str(e))
            else:
                text = f"{text.capitalize()}"
                print(chunk_filename, ":", text)
                whole_text += text

    # return the text for all chunks detected

    return whole_text


path = "Isac.wav"
print("\nFull text:", large_audio(path))
