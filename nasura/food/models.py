from django.db import models

class Food(models.Model):
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    name  = models.CharField(
    	verbose_name='商品名', 
    	max_length=50,
    	)
    money = models.IntegerField(
    	verbose_name='価格'
    	)