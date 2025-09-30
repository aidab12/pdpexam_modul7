from faker import Faker
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
import datetime

from apps.models import (
    Author, Book, Product
)


class BookListModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        published_date = attrs['published_date']
        now = datetime.date.today()
        if published_date > now:
            raise ValidationError('Вы не можете вводить будущую дату!')
        return super().validate(attrs)

    def create(self, validated_data):
        author = self.context['author'].user

        if not author:
            faker = Faker()
            full_name = f'{self.faker.first_name()} {self.faker.last_name()}'
            author = Author.objects.create(name=full_name)



class AuthorListModelSerializer(ModelSerializer):
    books = BookListModelSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = '__all__'



class ProductListModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'











