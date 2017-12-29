from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=30)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.album_title + ' - ' + self.artist

#on album delete, models.CASCADE deletes all related songs
#although the tutorial uses CharField for most, I think I need to change some
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    file_type = models.CharField(max_length=10)
    
    def __str__(self):
        return self.song_title