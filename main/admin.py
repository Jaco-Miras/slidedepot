from django.contrib import admin
from .models import (
<<<<<<< HEAD
    User,
=======
    Article,
    Presentation,
    Category,
>>>>>>> 0e4b74dbfe5c43681675f4b7d7a9973061847952
    Comment
)

# Register your models here.
<<<<<<< HEAD
admin.site.register(User)
admin.site.register(Comment)
=======


# admin.site.register(Article)
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')


admin.site.register(Category)
admin.site.register(Presentation)
admin.site.register(Comment)

# LogEntry.objects.all().delete()
>>>>>>> 0e4b74dbfe5c43681675f4b7d7a9973061847952
