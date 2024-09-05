from django.contrib import admin
from product.models import Car, Comment


class CarAdmin(admin.ModelAdmin):
    list_display = ["make", "model", "year", "description", "owner"]
    list_filter = ('make', 'model')
    search_fields = ('make', 'model')


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'car', 'author']
    list_filter = ('car',)
    search_fields = ('content',)


admin.site.register(Car, CarAdmin)
admin.site.register(Comment, CommentAdmin)
