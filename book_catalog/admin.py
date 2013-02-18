from book_catalog.models import Page, News, Option, Series, Book
from django.contrib import admin

class BookCatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Series, BookCatalogAdmin)
admin.site.register(Book, BookCatalogAdmin)
admin.site.register(Page, BookCatalogAdmin)
admin.site.register(News)
admin.site.register(Option)