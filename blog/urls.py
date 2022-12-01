from django.urls import path
from . import views

urlpatterns = [
    # 이 부분을 채울 겁니다!
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]