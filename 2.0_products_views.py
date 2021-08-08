# 2.2 Filter
# 我们在系统中获得很多的reviews，但是我们需要能够给用户们展示有decent ratings的products
# 填写’good reviews‘，让它返回一个’raitng‘为3或者更高的’Review‘对象们的QuerySet，
# 会使用到’gte‘字段查询，’大于或者等于‘，
# 确保将’Review‘s提供到template中，在context dictionary中以’reviews‘的形式
# 2.4 exclude
# 用户们喜欢我们的‘good reviews’ feature，但是他们希望能够只看到最新的features，
# 第一，import ‘datetime’ library到views.py顶部
# 第二，在‘recent_review'视图中，使用’datetime.datetime.today()'以及‘datetime.timedelta'
#      去获取一个180日前的新的datetime


from django.shortcuts import render
import datetime

from . import models


def good_reviews(request):
    # start your code here
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def recent_review(request):
    today = datetime.datetime.today()   # 但是用now()可能会更加准确
    delta = datetime.timedelta(days=-180) 
    newtime = today + delta
    reviews = models.Review.objects.exclude(created_at__lt=newtime)
    return render(request, 'products/reviews.html', {'reviews': reviews})
