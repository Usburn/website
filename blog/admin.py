from django.contrib import admin

from .models import Reader , Project, Author, Comment

# Register your models here.


admin.site.register(Reader)



class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Author)
admin.site.register(Comment)