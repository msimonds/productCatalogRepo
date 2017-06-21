from django.db import models

#adjacency list table that stores each genre and it's parent

class Genre(models.Model):
     MEDIA_CHOICES = (
        ("F", 'Film'),
        ("B", 'Book'),
        ("A", 'Album')
        )
     genre_name=models.CharField(max_length=200)
     parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

     def __str__(self):
          for choice in self.MEDIA_CHOICES:
               if(self.genre_name is choice[0]):
                  return choice[1]
          return self.genre_name

class Product(models.Model):

    media_type = models.CharField(max_length=50, choices=Genre.MEDIA_CHOICES)
    parent = models.ForeignKey(Genre)
    title = models.CharField(max_length=500)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images',blank=True, null=True, default=None)

    def __str__(self):
        return self.title

    def get_media(self):
        for choice in Genre.MEDIA_CHOICES:
               if(self.media_type is choice[0]):
                  return choice[1]
        return '?'

    def real_url(self):
        if not self.image:
            return 'static/catalog/images/noImageAvailable.png'
        return self.image.url









     
    
