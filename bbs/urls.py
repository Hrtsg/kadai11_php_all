from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    # 一覧ページのビュー
    path('', views.IndexView.as_view(), name='index'),
    #投稿詳細ページ
    path('<int:pk>/',views.DetailView.as_view(),name='detail'), 
    #新規投稿ページ
    path('create/', views.CreateView.as_view(),name='create'),
    #投稿編集のページ
    path('<int:pk>/update/',views.UpdateView.as_view(),name='update'),
       #削除
    path('<int:pk>/delete/',views.DeleteView.as_view(),name='delete'),
]
