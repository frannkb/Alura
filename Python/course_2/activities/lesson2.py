class Music:
	list = []

	def __init__(self, name, artist, duration):
		self.name = name
		self.artist = artist
		self.duration = duration

		Music.list.append(self)
	
	def __str__(self):
		return f'{self.name} | {self.artist} | {self.duration}'

	def list_musics():
		for music in Music.list:
			print(f'{music.name} | {music.artist} | {music.duration}')

rock_music = Music('thunder','Imagine Dragons', '3:20')


Music.list_musics()
