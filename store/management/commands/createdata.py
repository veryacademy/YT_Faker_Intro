import random

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from store.models import Category, Product, ProductImage, ProductType

CATEGORIES = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "T-shirt",
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "PoloShirt",
    "Beauty",
    "DIYTools",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "Lighting",
]

PRODUCTS = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "T-shirt",
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "PoloShirt",
    "Beauty",
    "DIYTools",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "Lighting",
]


class Provider(faker.providers.BaseProvider):
    def ecommerce_category(self):
        return self.random_element(CATEGORIES)

    def ecommerce_products(self):
        return self.random_element(PRODUCTS)


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):

        fake = Faker(["nl_NL"])
        fake.add_provider(Provider)

        # print(fake.ecommerce_products())

        for _ in range(15):
            d = fake.unique.ecommerce_category()
            Category.objects.create(name=d, slug=d)

        for _ in range(15):
            e = fake.unique.ecommerce_products()
            ProductType.objects.create(name=e)

        for _ in range(15):
            pt = fake.text(max_nb_chars=30)
            cid = random.randint(1, 15)
            ptid = random.randint(1, 15)
            Product.objects.create(
                product_type_id=ptid,
                category_id=cid,
                title=pt,
                description=fake.text(max_nb_chars=100),
                regular_price=(round(random.uniform(50.99, 99.99), 2)),
                discount_price=(round(random.uniform(10.99, 49.99), 2)),
            )

        for i in range(1, 16):
            ProductImage.objects.create(product_id=i, alt_text=fake.text(max_nb_chars=30), is_feature=True)

        check_category = Category.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of categories: {check_category}"))
