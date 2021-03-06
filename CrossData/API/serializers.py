from .models import *
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):

	class Meta:

		model = Game
		fields = '__all__'

class GameNameSerializer(serializers.ModelSerializer):

	class Meta:

		model = Game
		fields = ['name']


class YoutubeInfoSerializer(serializers.ModelSerializer):

	game = GameSerializer()

	class Meta:

		model = InfoYoutube
		fields = '__all__'


class SteamInfoSerializer(serializers.ModelSerializer):

	game = GameSerializer()

	class Meta:

		model = InfoSteam
		fields = '__all__'


class TwitchInfoSerializer(serializers.ModelSerializer):

	game = GameSerializer()

	class Meta:

		model = InfoTwitch
		fields = '__all__'


class TwitchStreamSerializer(serializers.ModelSerializer):

	game = GameSerializer()

	class Meta:

		model = TwitchStream
		fields = '__all__'

class ScreenshotSerializer(serializers.ModelSerializer):
    
    game = GameSerializer()

    class Meta:
        model = Screenshot
        fields = '__all__'

class PaletteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Palette
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
