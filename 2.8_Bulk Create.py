# We accidentally deleted a few product reviews and need to get them back
# It happened between backups
# we have a couple of logs, so we know the rating just not the comments
# it's not ideal but it'll have to do.
# 1
# in the function named 'fix_25', can you use the 'bulk_create' method 
# to make three 'Review's for the 'Product' with an 'id' of 1?
# 2
# They should have 'rating's of 2, 3, 5

# products/emergency.py
from . import models


def fix_25(): 
    # product = models.Product.get(id=1)              # 先获取指定的对象
    # reviews = models.Review.objects.bulk_create([   # 然后
    #     models.Review(product=product, rating=2),
    #     models.Review(product=product, rating=3),
    #     models.Review(product=product, rating=5),
    # ])

    models.Review.objects.bulk_create([        # 记得添加[], 是一个list
        models.Review(product_id=1, rating=2),
        models.Review(product_id=1, rating=3),
        models.Review(product_id=1, rating=5)
    ])