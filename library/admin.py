from django.contrib import admin
from .models import Book, Users, UserBook

admin.site.register(Users)
admin.site.register(Book)
admin.site.register(UserBook)