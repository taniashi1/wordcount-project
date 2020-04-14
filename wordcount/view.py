from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, "home.html", {"hey":"Tania"})

def count(request):
	text = request.GET["fulltext"]
	wordlist = text.split()
	my_dict = {}
	for word in wordlist:
		if word not in my_dict:
			my_dict[word] = 1
		else:
			my_dict[word] += 1

	sorted_list = sorted(my_dict.items(), key = operator.itemgetter(1), reverse = True)
	return render(request, "count.html", {"text":text, "total":len(wordlist), "sortedwords":sorted_list})


def about(request):
	return render(request, "about.html")