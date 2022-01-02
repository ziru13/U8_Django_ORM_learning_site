# we have a view for showing a product, 'produce_detail',
# but it currently shows the 'Review's in the order they were created,
# I'd rather show them newest-first, though.
# Can you use 'order_by' to sort them by 'created_at' in descending order?

# products/views.py

import datetime
from django.shortcuts import render, get_object_or_404
from . import  models


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
    # reviews = product.review_set.all()
    # start your code here
    reviews = product.review_set.all().order_by('created_at')
    return render(request, 'products/product_detail.html', {'product': product,
                                                            'review': reviews})