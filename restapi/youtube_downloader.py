import os
import sys
import pytube
import argparse

class YouTubeDownloader:
    def __init__(self):
        self.setup_parser()

    def setup_parser(self):
        self.parser = argparse.ArgumentParser(description="YouTube Video Downloader")
        self.parser.add_argument('-u', '--url', help="URL of the YouTube video to download")
        self.parser.add_argument('-f', '--file', help="File containing a list of YouTube video URLs to download")

    def download_video(self, video_url):
        try:
            youtube = pytube.YouTube(video_url)
            video_stream = youtube.streams.get_highest_resolution()
            video_stream.download()

            original_filename = video_stream.default_filename
            print(f"Downloading {original_filename}")
            new_filename = original_filename.replace(" ", "-")
            os.rename(original_filename, new_filename)

            print("Video downloaded successfully.")
        except Exception as e:
            print("An error occurred while downloading the video:", str(e))

    def download_videos_from_file(self, file_path):
        if not os.path.exists(file_path):
            print(f"The file {file_path} does not exist.")
            return

        with open(file_path, 'r') as file:
            urls = file.readlines()

        for url in urls:
            url = url.strip()
            if url:
                print(f"Processing URL: {url}")
                self.download_video(url)

    def run(self):
        args = self.parser.parse_args()

        if args.url:
            self.download_video(args.url)
        elif args.file:
            self.download_videos_from_file(args.file)
        else:
            print("Please provide a URL with -u or a file with -f.")

if __name__ == "__main__":
    downloader = YouTubeDownloader()
    downloader.run()

"""
pip install pytube
to convert to mp3
ffmpeg -i filename.mp4 filename.mp3
"""