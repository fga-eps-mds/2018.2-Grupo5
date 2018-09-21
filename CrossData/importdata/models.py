from django.db import models

class Genre(models.Model):

	id_igdb = models.IntegerField(
		('Genre ID'),
		help_text=("Genre id at IGDB"),
		primary_key=True,
	)

	name = models.CharField(
		('Genre name'),
		help_text=("Genre name"),
		max_length=100,
	)

class Stream(models.Model):

	id = models.IntegerField(
		('Stream ID'),
		help_text=("Id da stream na Twitch"),
		primary_key=True,
	)

	game_id = models.IntegerField(
		('Game ID'),
		help_text=("Id do jogo na Twitch")
	)

	language = models.CharField(
		('Language'),
		help_text=("Language of stream"),
		max_length=100,
		null=True
	)

	started_at = models.CharField(
		('Started date'),
		help_text=("Date when stream started"),
		max_length=100,
		null=True
	)

	type = models.CharField(
		('Type'),
		help_text=("Type of stream"),
		max_length=100,
		null=True
	)

	viewer_count = models.IntegerField(
		('Viewer count'),
		help_text=("Number of views in stream"),
		max_length=100,
		null=True
	)

	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)

	game = models.ForeignKey(
		Game,
		on_delete=models.CASCADE
	)

class User(models.Model):

	user_id = models.IntegerField(
		('User ID'),
		help_text=("User id at Twitch API"),
		primary_key=True,
	)

	display_name = models.CharField(
		('Display name'),
		help_text=("Display name"),
		max_length=100,
		null=True
	)

	type = models.CharField(
		('Type'),
		help_text=("Type"),
		max_length=100,
		null=True
	)

	view_count = models.IntegerField(
		('Count views'),
		help_text=("Views couting of user"),
		null=True
	)

	follows = models.IntegerField(
		('follows'),
		help_text=("Number of followers"),
		null=True
	)


class Game(models.Model):

	id_igdb = models.IntegerField(
		('IGDB ID'),
		help_text=("Id do jogo na IGDB"),
		null=True
	)

	id_steam = models.IntegerField(
		('STEAM ID'),
		help_text=("Id do jogo na Steam"),
		null=True
	)

	id_twitch = models.IntegerField(
		('TWITCH ID'),
		help_text=("Id do jogo na Twitch"),
		null=True
	)

	name = models.CharField(
		('Name'),
		help_text=("Name of game"),
		max_length=100,
		null=True
	)

	positive_reviews_steam = models.IntegerField(
		('Positive Reviews'),
		help_text=("Number of positive reviews at Steam"),
		null=True
	)

	negative_reviews_steam = models.IntegerField(
		('Negative Reviews'),
		help_text=("Number of negative reviews at Steam"),
		null=True
	)

	owners = models.IntegerField(
		('Owners'),
		help_text=("Name of the owners"),
		null=True
	)

	hypes = models.IntegerField(
		('Hypes'),
		help_text=("Number of access in the game befores its release"),
		null=True
	)

	popularity = models.FloatField(
		('Popularity'),
		help_text=("Popularity of game"),
		null=True
	)

	critics_rating = models.FloatField(
		('Critics Rating'),
		help_text=("Rating based on external critic scores"),
		null=True
	)

	time_to_beat = models.FloatField(
		('Time To Beat'),
		help_text=("Average time to beat the game"),
		null=True
	)

	average_forever = models.IntegerField(
		('Average Forever'),
		help_text=("Average forever of the game"),
		null=True
	)

	average_2weeks = models.IntegerField(
		('Average 2 weeks'),
		help_text=("Average forever of the game"),
		null=True
	)

	price = models.IntegerField(
		('Price'),
		help_text=("Price of the game"),
		null=True
	)

	language = models.CharField(
		('Languages'),
		help_text=("Language of the game"),
		null=True
	)

	genres = models.ManyToManyField(
		Genre,
		on_delete=models.CASCADE
	)

	#YouTube
	count_videos = models.IntegerField(
		('count_videos'),
		help_text=("Number of videos found in youtube request"),
		null=True
	)

	count_views = models.IntegerField(
		('count_views'),
		help_text=("Number of views summed from youtube videos"),
		null=True
	)

	count_likes = models.IntegerField(
		('count_likes'),
		help_text=("Number of likes summed from youtube videos"),
		null=True
	)

	count_dislikes = models.IntegerField(
		('count_dislikes'),
		help_text=("Number of dislikes summed from youtube videos"),
		null=True
	)

	count_comments = models.IntegerField(
		('count_comments'),
		help_text=("Number of comments summed from youtube videos"),
		null=True
	)

	def __str__(self):
	    """
	    Returns the object as a string, the attribute that will represent
	    the object.
	    """

	    return self.name

	class Meta:
	    """
	    Some information about feedback class.
	    """
	    verbose_name = ("Game BI")
        verbose_name_plural = ("Games BI")
