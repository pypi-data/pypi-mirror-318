#!/usr/bin/python3

from deezloader.models.track import Track

class Playlist:
	def __init__(self) -> None:
		self.tracks: list[Track] = []
		self.zip_path = None