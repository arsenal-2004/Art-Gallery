from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Painting, Artist

def index(request):
	painting_list = Painting.objects.all()
	context = {'painting_list': painting_list}
	return render(request, 'ekart/index.html', context)

def detail(request, painting_id):
	painting = get_object_or_404(Painting, pk=painting_id)
	return render(request, "ekart/detail.html", {'painting': painting})

def search(request):
	txt = request.POST['t']
	painting_list = Painting.objects.filter(name__contains=txt)
	if (len(txt) == 0):
		return render(request, "ekart/index.html", {'error_message': 'Please enter some text', 'painting_list': Painting.objects.all()})
	elif (len(painting_list) == 0):
		return render(request, "ekart/index.html", {'error_message': 'No such painting exists. Please try with other words.', 'painting_list': Painting.objects.all()})
	else:
		return render(request, "ekart/results.html", {'painting_list': painting_list})
