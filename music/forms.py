<<<<<<< HEAD
# from django.contrib.auth.models import User
# from django import forms

# class UserForm(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput)

# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password']


from django import forms
from django.contrib.auth.models import User

from .models import Album, Song


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
=======
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']
>>>>>>> 29336ae68317eba223cfd8941a730b885f3238df
