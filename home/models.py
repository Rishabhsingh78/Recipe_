from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100,db_index= True) # db_index for indexing the table
    receipe_description = models.TextField()
    receipe_slug = models.SlugField(unique= True)
    receipe_type = models.CharField(max_length=100,choices=(("Veg","Veg"),("Non-Veg","Non-Veg")))


class Ingredients(models.Model):
    receipe = models.ForeignKey(Receipe,on_delete=models.CASCADE,related_name="receipe_indredients")
    ingredients_name = models.CharField(max_length=100)
     