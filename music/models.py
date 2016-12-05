<<<<<<< HEAD
# from django.db import models
# from django.core.urlresolvers import reverse

# # Create your models here.
# class Album(models.Model):
# 	artist = models.CharField(max_length = 250)
# 	album_title = models.CharField(max_length = 500)
# 	genre = models.CharField(max_length = 100)
# 	# album_logo = models.CharField(max_length = 1000)
# 	album_logo = models.FileField()

# 	def get_absolute_url(self):
# 		return reverse('music:detail', kwargs = {'pk' : self.pk})

# 	def __str__ (self):
# 		return self.album_title + ' - ' + self.artist


# class Song(models.Model):
# 	album = models.ForeignKey(Album, on_delete = models.CASCADE)
# 	file_type = models.CharField(max_length = 10)
# 	song_title = models.CharField(max_length =250)
# 	is_favorite = models.BooleanField(default = False)

# 	def __str__ (self):
# 		return self.song_title




from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
=======
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Album(models.Model):
	artist = models.CharField(max_length = 250)
	album_title = models.CharField(max_length = 500)
	genre = models.CharField(max_length = 100)
	# album_logo = models.CharField(max_length = 1000)
	album_logo = models.FileField()

	def get_absolute_url(self):
		return reverse('music:detail', kwargs = {'pk' : self.pk})

	def __str__ (self):
		return self.album_title + ' - ' + self.artist


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	file_type = models.CharField(max_length = 10)
	song_title = models.CharField(max_length =250)
	is_favorite = models.BooleanField(default = False)

	def __str__ (self):
		return self.song_title
>>>>>>> 29336ae68317eba223cfd8941a730b885f3238df
