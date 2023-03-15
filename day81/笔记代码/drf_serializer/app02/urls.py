
from django.urls import path,re_path,include
from app02 import views
urlpatterns = [
    re_path('books/(?P<pk>\d+)', views.APP02BookView.as_view()),

]
