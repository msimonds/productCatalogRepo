from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from PIL import Image
import itertools
import os, sys

from django.conf import settings

from .models import Genre, Product


def index(request):
    
    #this needs to just display all the products
    latest_prod_list = Product.objects.all()
    template = loader.get_template('catalog/index.html')
    context = {        
        'latest_prod_list' : latest_prod_list     
        }    
    return render(request, 'catalog/index.html', context)

def detail(request, prod_id):    
    #this will list the hierarchy and the breadcrumbs
    this_product = get_object_or_404(Product, pk=prod_id)
   
    breadcrumbs=getBreadcrumb(this_product.parent, [])
   
    
    hierarchy_list = getFullHierarchy()
    template = loader.get_template('catalog/detail.html')
    context = {
        'breadcrumbs' : breadcrumbs,
        'hierarchy_list' : hierarchy_list,
        'prod' : this_product
        }
    return render(request, 'catalog/detail.html', context)
    
def add(request):
    template = loader.get_template('catalog/add.html')
    return render(request, 'catalog/add.html',{})


def process(request):
    #check if item already is in database
    #build the adjacency list (genre model)
    media_object = Genre.objects.get(parent=None, genre_name=request.POST['media'])
    genre_objects = Genre.objects.filter(parent=media_object, genre_name=request.POST['genre'])
    if( not genre_objects.exists()):
       genre_objects = [makeGenre(request.POST['genre'], media_object)]
    parentG=genre_objects[0]   
    if(request.POST['subgenre'] !=""):
        subgenre_objects = Genre.objects.filter(parent=parentG,
                                                genre_name=request.POST['subgenre'])
        if(not subgenre_objects.exists()):
            subgenre_objects=[makeGenre(request.POST['subgenre'], parentG)]           
        parentG=subgenre_objects[0]
       
    #build the product model
  
    p = Product(media_type=request.POST['media'], parent=parentG,
                title=request.POST['title'], description=request.POST['description'],
                price=request.POST['price'])
    if(request.FILES):
        img_path = handle_uploaded_file(request.FILES['pic'])
        p.image=request.FILES['pic'].name
        
    p.save()
    return redirect('catalog:index')

#returns relative path of file
def handle_uploaded_file(f):
    path = settings.MEDIA_ROOT+'/'+f.name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    im = Image.open(path)
    new_size = 150, 150
    im.thumbnail(new_size, Image.ANTIALIAS)
    im.save(path)
    
    
    
                         
           
def makeGenre(name, parentObject):    
    g=Genre(parent=parentObject, genre_name=name)
    g.save()
    return g                         

def getBreadcrumb(genre_node, trail):
    if(genre_node.parent is None):        
        return trail + [str(genre_node)]
    else:        
        return getBreadcrumb(genre_node.parent, trail+[str(genre_node)])

#grabs the expanded hierarchy for a given media type, formatted for Django's unordered list 
def getHierarchy(depth, parent_node, hierarchy):
    children_list = Genre.objects.filter(parent=parent_node)
    c_list=[]
    if not children_list:
       return hierarchy + [str(parent_node)]
    for child in children_list:            
        c_list += getHierarchy(depth+1, child, hierarchy)
    return hierarchy + [str(parent_node), c_list]        
    
def getFullHierarchy():
    full_list = []
    for choice in Genre.MEDIA_CHOICES:
        media = Genre.objects.get(genre_name=choice[0])
        full_list += getHierarchy(0, media, [])   
    return full_list

           
        

    
    

