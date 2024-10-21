from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters


# カテゴリを表すモデル
class Category(models.Model):
    title = models.CharField(max_length=255)  # カテゴリの名前を保存するフィールド

    class Meta:
        ordering = ('title',)  # カテゴリをタイトルのアルファベット順に並べ替える


class Job(models.Model):
    # カテゴリモデルとの関連付け。カテゴリが削除されると対応する求人も削除される。
    category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    position_salary = models.CharField(max_length=255)
    position_location = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    company_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='jobs',on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)  # 作成日が新しい順に並べ替える

    def created_at_formatted(self):
        return defaultfilters.date(self.created_at, 'M d, Y')  # 日付をフォーマットして返す

