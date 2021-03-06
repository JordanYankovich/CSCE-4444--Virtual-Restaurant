from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Category, MenuItem

# Create your views here.
def index(request):
	categories_list = Category.objects.order_by('name')
	context = {'categories_list': categories_list}
	return render(request, 'menu/index.html', context)

def categories(request, category_id):
	return HttpResponse("You're looking at category %s." % category_id)
