from django.contrib import admin
from.models import user, item, lost_report, found_report, message, notification, rating

# Register your models here.
admin.site.register(user)
admin.site.register(item)
admin.site.register(lost_report)
admin.site.register(found_report)
admin.site.register(message)
admin.site.register(notification)
admin.site.register(rating)
