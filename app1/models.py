from django.db import models
from django.forms import ModelForm

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=50,default=None)
    year_formed=models.PositiveIntegerField()
#django will automaticlly show space where there is a '_'
class Album(models.Model):
    name=models.CharField("album",max_length=50)
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
#first papam "album" is a pseudo name which django will display us instead of "name"
#primary keys(can be generated automatically) and foriegn keys
#primary_key=True in parameters
#coustom_id_name=models.AutoField(primary_key=True)
#above is auto-generated integer
#all albums made by an artist
#so here is a need of foriegn key
class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name','year_formed']
