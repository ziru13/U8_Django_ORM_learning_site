# we've decided that we'd rather have review ratings be a scale of 1-10 instead of 1-5.
# that we want to update all of our existing records so they accurately reflect the new scale.
# Write a function named 'double_ratings' that uses '.update()'
# and an 'F' object to double the current 'rating' value for all the existing 'Review' objects

# products/emergency.py

from django.db.models import F
from . import models


def double_ratings():
    # models.Review.all().update(rating=F('rating')*2)

    # 也可以不写all(), 因为除非你表明用'.except()/.filter()/.get(),
    # 所有的queries都有有一个没有表明出来的'.all()'

    models.Review.objects.update(rating=F('rating')*2)