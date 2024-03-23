import os
import subprocess

class AudioAnalysisLLaVa:
    def __init__(self, audio_path):
        self.audio_path = audio_path
        self.audio_file = os.path.splitext(audio_path)[0] + ".wav"
        subprocess.run(["ffmpeg", "-i", audio_path, self.audio_file], capture_output = True)
    def summarize_lecture_video(self,input_file, output_summary):
        """
        Summarizes a lecture video using LLAVA.

        Args:
            input_file (str): Path to the input video file (.mp4 or .wav).
            output_summary (str): Path to save the generated summary text.

        Returns:
            None
        """

        # Check if LLAVA is installed


        # Validate input file format
        if not input_file.endswith((".mp4", ".wav")):
            print("Error: Invalid file format. Supported formats are .mp4 and .wav.")
            return

        # Extract audio if input is video
        if input_file.endswith(".mp4"):
            audio_file = os.path.splitext(input_file)[0] + ".wav"
            subprocess.run(["ffmpeg", "-i", input_file, audio_file],
                        capture_output=True)
        else:
            audio_file = input_file

        # Summarize using LLAVA
        command = ["llava", "summarize", audio_file, "-o", output_summary]
        subprocess.run(command)

        print(f"Lecture video summary saved to: {output_summary}")

    def summarize_lecture_audio(self, input_file, output_summary):
        """
        Summarizes a lecture audio file using LLAVA.

        Args:
            input_file (str): Path to the input audio file (.wav).
            output_summary (str): Path to save the generated summary text.

        Returns:
            None
        """

        

    # Example usage
input_video = "path/to/your/lecture.mp4"  # Or input_audio = "path/to/your/lecture.wav"
output_summary = "lecture_summary.txt"
#summarize_lecture_video(input_video, output_summary)
