from django.shortcuts import render
from django.http import HttpResponse #モジュールを読み込み
from .models import Article #Article モデルクラスをインポート
from django.db.models import Q #Qクラスのインポート

# Create your views here.
def index(request):
    #Article テーブルのクラスContentフィールドの値が’ちゃお’もしくはIDが１であるレコードのみを取得
    # articles = Article.objects.filter(Q(content='ちゃお')|Q(pk=1)) 
    # ArticleテーブルのクラスContentフィールドすべてを取得
    articles = Article.objects.all()
    context = {
        'articles':articles, #contextに渡す
    }
    return render(request, 'hello/index.html', context) #テンプレートに渡す