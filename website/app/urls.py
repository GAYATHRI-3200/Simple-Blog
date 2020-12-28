from django.urls import path
from app.views import(
	
	create_app_view,
	detail_app_view,
	edit_app_view,
)

app_name = 'app'

urlpatterns = [
	path('create/', create_app_view, name="create"),
	path('<slug>/', detail_app_view, name="detail"),
	path('<slug>/edit', edit_app_view, name="edit"),
]
