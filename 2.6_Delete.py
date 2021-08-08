# 我们的reviews收到越来越多的垃圾广告，之后我们要执行一个更好的解决办法
# 但是现在，写一个叫做‘can_spam'的函数，它选择包含字符串‘http'的'comment'字段中所有的’Review(s)'
# 然后删除它们

# products/utils.py

from . import models


def can_spam():  # 不需要request，
    spams = models.Review.objects.filter(comment__icontains='http')
    spams.delete()

    # 或者
    # models.Review.objects.filter(comment__icontains='http').delete()
