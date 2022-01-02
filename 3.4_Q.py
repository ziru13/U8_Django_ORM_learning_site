# 现在我们油一个范围较大的reviews，我们要对我们展示的reviews挑剔
# 更新‘product_detail'视图， 只展示选择了的products的’Review‘，
# 一个’rating‘等于8或者以上review
# 或者是最近四周内创建的
# 不要改变ordering，我们要的仍然是最新的一个

# products/views.py

import datetime

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from . import models


def good_reviews(request):
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def recent_review(request):
    # today = datetime.datetime.today()   # 但是用now()可能会更加准确
    # delta = datetime.timedelta(days=-180)
    # newtime = today + delta
    # reviews = models.Review.objects.exclude(created_at__lt=newtime)  # 我的答案
    six_months_ago = datetime.datetime.today() - datetime.timedelta(days=180)
    reviews = models.Review.objects.exclude(created_at__lt=six_months_ago)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def product_detail(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    # reviews = product.review_set.all().order_by('created_at')

    # start your code from here
    four_weeks_ago = datetime.datetime.today() + datetime.timedelta(weeks=-4)
    reviews = product.review_set.filter(
        Q(rating__gte=8) | Q(created_at__gte=four_weeks_ago)
    ).order_by('created_at')

    return render(request, 'products/product_detail.html', {'product': product,
                                                            'review': reviews})

# four_weeks_ago是距离今天的四个星期后，因为today减去4个星期了
# 下面的created_at__gte, 因为four_weeks_ago是今天的四个星期后，但是我们要的是距离今天的四个星期内

