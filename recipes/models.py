from django.db import models

# Create your models here.
class RecipesList(models.Model):
    recipe_name = models.CharField(max_length=200,null=False,blank=False)
    recipe_dec = models.CharField(max_length=500,null=False,blank=False)
    recipe_rating = models.IntegerField(null=False,blank=False)
    recipe_directions = models.CharField(max_length=500,null=False,blank=False)
    recipe_ingredients = models.CharField(max_length=500,null=False,blank=False,help_text="Enter a value split by ' , ' ex: <b> nutritional yeast , soya sauce </b> ")
    recipe_img = models.ImageField(upload_to="RecipeImages",blank=True,null=True)

    def __str__(self):
        return self.recipe_name


class recipeRaquest(models.Model):
    user = models.CharField(max_length=200,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    recipe_name = models.CharField(max_length=200,null=False,blank=False)
    recipe_img = models.ImageField(upload_to="RecipeRequestImages",blank=True,null=True)

    def __str__(self):
        return f"{self.recipe_name} requested by {self.user} "
    
    # change the wrong class name to right
    class Meta:
        verbose_name_plural = " Recipe Request " 