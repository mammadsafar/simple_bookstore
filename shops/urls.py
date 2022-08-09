from django.urls import path, include

from . import views

urlpatterns = [
    # # path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('', views.PlanListView.as_view(), name='plan_list'),

    path('buy/<int:pk>/', views.buy_plan, name='buy_plan'),
    # path('<int:pk>/', views.book_detail, name='book_detail'),
    # path('create/', views.BookCreateView.as_view(), name='book_create'),
    # path('update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    # path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),


]
