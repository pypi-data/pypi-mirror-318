#!/usr/bin/python3

from deezloader.models.track import Track
from deezloader.models.album import Album
from deezloader.models.playlist import Playlist

class Smart:
	def __init__(self) -> None:
		self.track: Track = None
		self.album: Album = None
		self.playlist: Playlist = None
		self.type = None
		self.source = None