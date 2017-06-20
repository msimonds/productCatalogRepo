from django.test import TestCase
from .models import Product, Genre
from . import views

# Create your tests here.
class ProductTests(TestCase):

    def test_make_genre(self):
        #Todo: randomize the names so each addition is unique
        parent_name = "Drama"
        name="LGBTQ"
        media_type="F"
        media_object = views.makeGenre(media_type, None)
        p = views.makeGenre(parent_name, media_object)
        genre_obj = views.makeGenre(name, p)    
        self.assertEqual(Genre.objects.filter(genre_name=name).exists(), True)
        
        
