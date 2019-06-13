from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
	path('category/', views.CategoryView.as_view(), name='category'),
	path('modify/', views.ModifyView.as_view(), name='modify'),
	path('range/', views.RangeView.as_view(), name='range'),
	path('recent/', views.RecentView.as_view(), name='recent'),
	path('add/', views.add, name='add'),
	path('<int:pk>/added/', views.AddedView.as_view(), name='added'),
	path('delete/', views.delete, name='delete'),
	path('update/', views.update, name='update'),
	path('duetoexpire/', views.ExpiringView.as_view(), name='duetoexpire')
]