from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from lists.models import Item, List
from lists.forms import ItemForm

def home_page(request):
	return render(request, 'lists/home.html', {'form':ItemForm()})


def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	error=None

	if request.method == 'POST':
		try: 
			item = Item.objects.create(text=request.POST['item_text'], list=list_)
			item.full_clean()
			item.save()
			return redirect(list_)
		except ValidationError:
			item.delete()
			error = "You can't have an empty list item"

	return render(request, 'lists/list.html', {'list':list_, 'error':error})

def new_list(request):
	list_ = List.objects.create()
	item = Item.objects.create(text=request.POST['item_text'], list=list_)
	try: 
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'lists/home.html', {'error':error})
	return redirect(list_) # this is the 'get_absolute_url' function. 1. in model define the function (see model) then when you redirect to the db OBJECT it automatically generates the url.

# Create your views here.
