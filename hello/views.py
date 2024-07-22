from django.shortcuts import render
from django.http import HttpResponse #モジュールを読み込み
from django.db.models import Q #Qクラスのインポート
from django.views import generic #汎用ビューをインポート
from .models import Article #Article モデルクラスをインポート


# Create your views here.
# IndexViewクラスを作成
class IndexView(generic.ListView):
    model = Article
    template_name = 'hello/index.html' #テンプレート名を指定