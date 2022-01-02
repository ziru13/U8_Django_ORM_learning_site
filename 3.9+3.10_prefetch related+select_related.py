from django.db.models import Q, Avg
from django.http import Http404
from django.shortcuts import render, get_object_or_404
import datetime

from . import models


def good_reviews(request):
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def recent_review(request):
    six_months_ago = datetime.datetime.today() - datetime.timedelta(days=180)
    reviews = models.Review.objects.exclude(created_at__lt=six_months_ago)
    return render(request, 'products/reviews.html', {'reviews': reviews})


# 3.9 prefetch_related: 两个challenges(还欠一个)
# 我们不能停止 给属于一个‘Product’的’Review‘s 的 ‘product_detail'中做的查询
# 但是我们可以将它移一下，以便当在拿product时就做好了
# 改变 ’product = get_object_or_404(...)‘ 为 一个 ’try‘和’except‘ (try, except, else)组合
# 如果 ’Product‘ 不存在，出发一个 ’Http404‘ exception
def product_detail(request, pk):

    # product = get_object_or_404(models.Product, pk=pk)
    # four_weeks_ago = datetime.datetime.today() - datetime.timedelta(weeks=4)
    # reviews = product.review_set.filter(
    #     Q(rating__gte=8) | Q(created_at__gte=four_weeks_ago)
    # ).order_by('-created_at')

    # start your code here
    try:
        product = models.Product.objects.prefetch_related('review_set').get(pk=pk)
    except models.Product.DoesNotExist:
        raise Http404
    else:
        four_weeks_ago = datetime.datetime.today() - datetime.timedelta(weeks=4)
        reviews = product.review_set.filter(Q(rating__gte=8) | Q(created_at__gte=four_weeks_ago)
                                        ).order_by('-created_at')

    return render(request, 'products/product_detail.html', {'product': product,
                                                            'reviews': reviews})


def product_list(request):
    products = models.Product.objects.annotate(avg_rating=Avg('review_rating')).all()
    return render(request, 'products/product_list.html', {'products': products})


# 4.0 select_related:
# 每一个’Review‘的视图都是关于它相关的‘Product’
# 这意味着我们必须至少做两个查询，一个是‘给Review’，一个给是‘Product’
# 在‘review_detail’视图中使用‘select_related’，去获得‘Product’的同时减少我们的查询到1一个
def review_detail(request, product_pk, pk):
    try:
        # review = models.Review.objects.get(product_id=product_pk, pk=pk)
        review = models.Review.objects.select_related('product').get(product_id=product_pk, pk=pk)
    except models.Review.DoesNotExist:
        raise Http404
    else:
        return render(request, 'products/review_detail.html', {'review': review})