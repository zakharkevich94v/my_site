from django.contrib import admin
from .models import (
    Person, 
    Works, 
    Category, 
    Tags, 
    WorkScreenshots
)
from django.utils.safestring import mark_safe


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name', 'email_addres', 'profile_picture')    
    readonly_fields = ('profile_picture',)

    def profile_picture(self, obj):        
        if obj.profile_pic:
            return mark_safe(f'<img src="{obj.profile_pic.url}" width=70 >')
        else:
            return f'Фотография профиля отсутствует'

    profile_picture.short_description = 'Фотография профиля'


class WorkScreenshotsAdmin(admin.StackedInline):
    model = WorkScreenshots
    extra = 1


@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description_cust', 'preview')
    list_filter = ('category',)
    search_fields = ('title',)
    readonly_fields = ('preview', 'views')
    prepopulated_fields = {'slug':('title',)}
    filter_horizontal = ('tag',)
    inlines = [WorkScreenshotsAdmin]
    
    def description_cust(self, obj):
        return mark_safe(f'<pre>{obj.description[:150]}</pre>')
    
    description_cust.short_description = 'Описание проекта'
    

    def preview(self, obj):
        if obj.work_preview:        
            return mark_safe(f'<img src={obj.work_preview.url} width=70 >')
        else: 
            return f'Превью работы отсутсвует'

    preview.short_description = 'Превью работы'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}