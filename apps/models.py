from django.db.models import Model, CharField, DateField, ForeignKey, DecimalField, CASCADE, TextField, \
    PositiveIntegerField, DateTimeField, IntegerField, ManyToManyField


class Author(Model):
    name = CharField(max_length=100, unique=True)
    birth_date = DateField()

class Book(Model):
    title = CharField(max_length=200)
    author = ForeignKey(Author, on_delete=CASCADE, related_name="books")
    price = DecimalField(max_digits=10, decimal_places=2)
    published_date = DateField()


class Article(Model):
    title = CharField(max_length=200)
    content = TextField()
    views = PositiveIntegerField(default=0)
    created_at = DateTimeField(auto_now_add=True)


class Category(Model):
    name = CharField(max_length=155)


class Product(Model):
    name = CharField(max_length=100)
    price = DecimalField(max_digits=10, decimal_places=2)
    category = ManyToManyField(Category, blank=True)
    stock = IntegerField()
    created_at = DateTimeField(auto_now_add=True)