from django.contrib import admin
from upload_profile.models import Photo


# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_image', 'upload_date', 'introduce']

    def user_image(self, obj):
        return '<img src="/static/%s" hight="64" width="64" / ' % obj.photo

    user_image.allow_tags = True
    user_image.short_description = "圖片"

    list_display_links = ['user_name']
    list_filter = ['user_name', 'upload_date']
    search_fields = ['upload_date']
    list_editable = ['upload_date']

    class Meta:
        model = Photo


admin.site.register(Photo, PhotoAdmin)
