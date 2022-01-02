# 我们获得很多reviews，但是我们的总目录不是非常well-rated
# 更新‘current_average’ 函数，返回所有‘review’s的aggregrate average rating
# 给它key name为‘average’

# products/utils.py

from django.db.models import Avg

from . import models


def current_average():
    average_rating = models.Review.objects.aggregate(average=Avg('rating'))
    return average_rating

