

import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import openai


class AudioAnalysis:
    def __init__(self, audio_path):
        self.audio_path = audio_path
        self.audio = AudioFileClip(self.audio_path)
        self.audio_duration = self.audio.duration
        self.audio_file = AudioSegment.from_wav(self.audio_path)
        self.audio_file = self.audio_file.set_channels(1)
        self.audio_file = self.audio_file.set_frame_rate(16000)
        self.audio_file = self.audio_file.set_sample_width(2)
        self.audio_file.export(self.audio_path, format="wav")

    def get_audio_duration(self):
        return self.audio_duration

    def transcribe_audio(self):
        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile(self.audio_path)
        with audio_file as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio)

    def transcribe_audio_openai(self):
        openai.api_key = ""
        response = openai.File.create(file=open(self.audio_path))
        return response

    def get_audio_transcription(self):
        return self.transcribe_audio()

    def transcription(self):
        transcibed_file = self.get_audio_transcription()
        audioclip = AudioFileClip(self.audio_path)

        r = sr.Recognizer()

        with sr.AudioFile(self.audio_path) as source:
            audio = r.record(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Google Speech Recognition didnt get it"

        except sr.RequestError:
            return "Request Error"

    def get_largeAudioTranscription(self):
        sound = AudioSegment.from_wav(self.audio_path)
        chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=sound.dBFS - 14, keep_silence=500)
        folder_name = "audio-chunks"
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        whole_text = ""

        for i, audio_chunk in enumerate(chunks, start=1):
            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
                try:
                    text = r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    print("Error:", str(e))

                else:
                    text = f"{text.capitalize()}. "
                    whole_text += text

        return whole_text

#write method to skip logistics/intro of lecture

    @staticmethod
    def summary(transcript):
        openai.api_key = ""
        response = transcript
        response += "Summary: "
        response = openai.Completion.create(engine="gpt-3.5-turbo-0125", prompt=ans, temperature=0.3,
                                            max_tokens=50,
                                            top_p=0.8,
                                            frequency_penalty=0,
                                            presence_penalty=0,
                                            stop=["\n", "Summary:"]
                                            )

        return response["choices"][0]["text"]
