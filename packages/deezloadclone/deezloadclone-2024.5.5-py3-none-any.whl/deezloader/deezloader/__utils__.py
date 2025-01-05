#!/usr/bin/python3

def artist_sort(array: list):
	if len(array) > 1:
		for a in array:
			for b in array:
				if a in b and a != b:
					array.remove(b)

	array = list(
		dict.fromkeys(array)
	)

	artists = " & ".join(array)

	return artists

def check_track_md5(infos: dict):
	if "FALLBACK" in infos:
		song_md5 = infos['FALLBACK']['MD5_ORIGIN']
		version = infos['FALLBACK']['MEDIA_VERSION'] if 'MEDIA_VERSION' in infos['FALLBACK'] else None
	else:
		song_md5 = infos['MD5_ORIGIN']
		version = infos['MEDIA_VERSION'] if 'MEDIA_VERSION' in infos else None

	return song_md5, version

def check_track_token(infos: dict):
	if "FALLBACK" in infos:
		track_token = infos['FALLBACK']['TRACK_TOKEN']
	else:
		track_token = infos['TRACK_TOKEN']

	return track_token

def check_track_ids(infos: dict):
	if "FALLBACK" in infos:
		ids = infos['FALLBACK']['SNG_ID']
	else:
		ids = infos['SNG_ID']

	return ids

def check_episode_id(infos: dict):
	if "FALLBACK" in infos:
		episode_id = infos['FALLBACK']['EPISODE_ID']
	else:
		episode_id = infos['EPISODE_ID']

	return episode_id
