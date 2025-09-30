from django.contrib import admin
from apps.models import Book, Author, Product, Category


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass