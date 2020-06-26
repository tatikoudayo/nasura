from django.shortcuts import render

# Create your views here.
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.http.response import HttpResponse
from .models import Food
from .forms  import FoodForm
from django.views.decorators.http import require_POST
from django.contrib import messages



def database(request):
	foods = Food.objects.all().order_by('id')
	form = FoodForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			messages.success(request, '投稿を受付ました。')
			d = {
				'form': form,
				'foods': foods,
			}
			return render(request, 'food.html', d)
		else:
			messages.error(request, '入力内容に誤りがあります。')
	d = {
		'form': form,
		'foods': foods,
	}
	return render(request, 'food.html', d)



@require_POST
def delete(request):
    delete_ids = request.POST.getlist('delete_ids')
    if delete_ids:
        Food.objects.filter(id__in=delete_ids).delete()
    return redirect('food:database')