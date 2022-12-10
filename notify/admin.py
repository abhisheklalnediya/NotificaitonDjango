from django.contrib import admin
from notify.models import Notifications
# Register your models here.


class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'image', 'name')


admin.site.register(Notifications, NotificationsAdmin)
