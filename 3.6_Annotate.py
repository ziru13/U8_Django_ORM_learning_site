
# products/views.py
import datetime

from django.db.models import Q, Avg
from django.shortcuts import render, get_object_or_404
from . import models


def good_reviews(request):
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def recent_reviews(request):
    six_month_ago = datetime.datetime.today() - datetime.timedelta(days=180)
    reviews = models.Review.objects.exclude(created_at__lt=six_month_ago)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def product_detail(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    four_weeks_ago = datetime.datetime.today() - datetime.timedelta(weeks=4)
    reviews = product.review_set.filter(Q(rating__gte=8)|Q(created_at__gte=four_weeks_ago)).order_by('-created_at').all()
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews})

# 3.6 Annotate
# 现在需要给我们所有products一个视图的列表，我已经创建了URL和模板，以及视图的开始部分
# 让‘product_list'视图个每个’Product’列出一个平均rating
# 用‘annotate()’和‘Avg’ class，添加一个注解到queryset中，叫做‘avg_rating'
# 使用 ’review‘，而不是’review_set‘


def product_list(request):
    # products = models.Product.objects.all()

    # start your code here
    # 给它重新命名为avg_rating，从Review模型中获取rating这个字段
    products = models.Product.objects.annotate(avg_rating=Avg('review__rating'))   # 3.6
    return render(request, 'products/product_list.html', {'products': products})
