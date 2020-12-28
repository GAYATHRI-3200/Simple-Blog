from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from account.models import Account
from app.views import get_app_queryset
from app.models import AppPost

# Create your views here.

APP_POSTS_PER_PAGE = 1

def home_screen_view(request):
	
	
	context = {}

	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)


	app_posts = sorted(get_app_queryset(query), key=attrgetter('date_updated'), reverse=True)
	context['app_posts'] = app_posts


	#context['some_string'] = "variable passing to views"
	#context['some_number'] = 123

	#context =  {
	#'some_string': "variable passing to views",
	#'some_number': 123
	#}

	#list_of_values = []
	#list_of_values.append("1st entry")
	#list_of_values.append("2nd entry")
	#list_of_values.append("3rd entry")
	#list_of_values.append("4th entry")
	#context['list_of_values'] = list_of_values
 	
	#accounts = Account.objects.all()
	#context['accounts'] = accounts


	#pagination
	page = request.GET.get('page',1)
	app_posts_paginator = Paginator(app_posts, APP_POSTS_PER_PAGE)

	try:
		app_posts = app_posts_paginator.page(page)
	except PageNotAnInteger:
		app_posts = app_posts_paginator.page(APP_POSTS_PER_PAGE)
	except EmptyPage:	
		app_posts = app_posts_paginator.page(app_posts_paginator.num_pages)

	context['app_posts'] = app_posts


	return render(request, "myapp/home.html", context)

	



