
from django.urls import path,re_path
from api import views
urlpatterns = [
    path('books/', views.BookAPIView.as_view()),
    path('books2/', views.BookView.as_view()), #继承了ListApiView
    re_path('books/(?P<pk>\d+)', views.BookAPIView.as_view()),
]
