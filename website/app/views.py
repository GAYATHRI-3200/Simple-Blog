from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from app.models import AppPost
from app.forms import  CreateAppPostForm, UpdateAppPostForm
from django.http import HttpResponse
from account.models import Account

# Create your views here.

def create_app_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateAppPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author= Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form =  CreateAppPostForm()
	context['form'] = form	

	return render(request, "app/create_app.html", {})


def detail_app_view(request, slug):

	context = {}

	app_post = get_object_or_404(AppPost, slug=slug)

	context['app_post'] = app_post

	return render(request,'app/detail_app.html', context)

def edit_app_view(request, slug):
	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")

	app_post = get_object_or_404(AppPost, slug=slug)


	if app_post.author != user:
		return HttpResponse("you are not the author of that post")
	
	if request.POST:
		form = UpdateAppPostForm(request.POST or None, request.FILES or None, instance=app_post)	
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			app_post = obj

	form = UpdateAppPostForm(
			initial = {
					"title": app_post.title,
					"body": app_post.body,
					"image": app_post.image,
			}
		)
	context['form'] = form	

	return render(request, "app/edit_app.html", context)

#search bar
def get_app_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = AppPost.objects.filter(
			Q(title__icontains=q) |
			Q(body__icontains=q)
		).distinct()
		for post in posts:
			queryset.append(post)
	return list(set(queryset))


