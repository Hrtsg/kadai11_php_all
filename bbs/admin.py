from django.contrib import admin
from .models import Article #models.py からArticleクラスをインポート

# Register your models here.
admin.site.register(Article) #DjangoAdminにArticleクラスを登録