from django.shortcuts import render,redirect

from django.http import HttpResponse

from .models import *

from django.contrib import messages

# Create your views here.

def hello_world(request):

    return HttpResponse("""<h1 style='color:red;'>hello world</h1>
                        <hr>
                        <h2>this is a web page</h2>""")

def homePage(request):
    recipes_data = RecipesList.objects.all()

    return render(request,"index.html",context={"recipes_data":recipes_data})

def recipeList(request):
    recipes_data = RecipesList.objects.all()

    if request.GET:
        search = request.GET.get("search")
        print(search)
        recipes_data = RecipesList.objects.filter(recipe_name__icontains = search)
    
    return render(request,"recipePage.html",context={"recipes_data":recipes_data})

def contact(request):

    if request.GET:
        user_name = request.GET.get("username")
        user_email = request.GET.get("email")
        user_recipe_name = request.GET.get("RecipeName")
        user_recipe_image = request.FILES.get("recipeImage")

        print(user_name,user_email,user_recipe_name,user_recipe_image)

        recipeRaquest.objects.create(user=user_name,email=user_email,recipe_name=user_recipe_name,recipe_img=user_recipe_image)
       
        messages.info(request, "request submited" )

        return redirect("/contact/")

    return render(request,"contact.html")


def recipe_view(request,id):
    recipes_data = RecipesList.objects.get(id=id)

    ingredients = recipes_data.recipe_ingredients.split(",")

    print(recipes_data)
    print(ingredients)
    return render(request,"recipeView.html",context={"recipes_data":recipes_data,"ingredients":ingredients})