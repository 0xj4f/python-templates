import os
import datetime
import sounddevice as sd
import soundfile as sf

"""
record_microphone.py v1.0.0

REQUIREMENTS:
sudo apt-get install portaudio19-dev
pip3 install sounddevice soundfile

USAGE: 
python3 record_microphone.py
Sound recording saved to: /tmp/2023-06-22-11-18.wav
"""


class SoundRecorder:
    def __init__(self, output_path=None):
        if output_path is None:
            output_path = "/tmp"
        self.output_path = output_path
        self.duration = 5 # Duration of the recording in seconds
        self.sample_rate = 44100 # Sample Rate (CD quality)
        self.channels = 1 # Mono

    def record_sound(self):
        current_datetime = datetime.datetime.now()
        filename = current_datetime.strftime("%Y-%m-%d-%H-%M") + ".wav"
        output_file = os.path.join(self.output_path, filename)

        # Set the audio parameters
        duration = self.duration  
        sample_rate = 44100  
        channels = 1  

        # Record sound using the laptop microphone
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
        sd.wait()

        # Save the recorded sound to the output file
        sf.write(output_file, recording, sample_rate)

        print("Sound recording saved to:", output_file)


def main():
    recorder = SoundRecorder()
    recorder.record_sound()


if __name__ == "__main__":
    main()
