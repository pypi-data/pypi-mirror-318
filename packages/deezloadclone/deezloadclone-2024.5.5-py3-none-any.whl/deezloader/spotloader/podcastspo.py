import os
from os.path import isfile, join
from librespot.core import Session
from librespot.metadata import EpisodeId
from librespot.audio.decoders import VorbisOnlyAudioQuality
# keep
class PodcastDownloader:
    def __init__(self, username, password, episode_uri, quality, path):
        self.__episode_uri = episode_uri
        self.__dw_quality = quality
        # Ensure the path includes the filename and .ogg extension
        self.__episode_path = join(path, episode_uri.split(':')[-1] + '.ogg')
        self.__session = Session.Builder().user_pass(username, password).create()
    
    def print_file_location(self, file_path):
        file = os.path.abspath(file_path)
        print(f'Episode downloaded to {file}')
        return file

    def download_episode(self):
        # Check if the file already exists
        if isfile(self.__episode_path):
            ans = input(f"Episode \"{self.__episode_path}\" already exists. Do you want to redownload it? (y/n): ")
            if ans.lower() != 'y':
                print("Download skipped.")
                return

        episode_id = EpisodeId.from_uri(self.__episode_uri)

        try:
            audio_quality = VorbisOnlyAudioQuality(self.__dw_quality)
            stream = self.__session.content_feeder().load(
                episode_id,
                audio_quality,
                False,
                None
            )
        except RuntimeError:
            raise Exception("Episode not found or unavailable.")

        total_size = stream.input_stream.size

        # Open the file with the correct path and write the data
        with open(self.__episode_path, "wb") as f:
            c_stream = stream.input_stream.stream()
            data = c_stream.read(total_size)
            c_stream.close()
            f.write(data)

        # Return the file location
        return self.print_file_location(self.__episode_path)
