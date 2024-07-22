from django.shortcuts import render
from django.http import HttpResponse #モジュールを読み込み
from django.db.models import Q #Qクラスのインポート
from django.views import generic #汎用ビューをインポート
from django.urls import reverse_lazy #reverse_lazy関数をインポート
from .models import Article #Article モデルクラスをインポート


# Create your views here.
# IndexViewクラスを作成
class IndexView(generic.ListView):
    model = Article
    template_name = 'bbs/index.html' #テンプレート名を指定

#DetailViewクラスを作成
class DetailView(generic.DetailView):
    model = Article
    template_name = 'bbs/detail.html'

#CreateViewクラスを作成
class CreateView(generic.edit.CreateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = '__all__'

#UpdateViewクラスを作成
class UpdateView(generic.edit.UpdateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = '__all__'

#DeleteViewクラスを作成
class DeleteView(generic.edit.DeleteView):
    model = Article
    template_name = 'bbs/delete.html'
    success_url = reverse_lazy('bbs:index')