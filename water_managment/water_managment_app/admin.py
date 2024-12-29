from django.contrib import admin

from water_managment_app.models import *

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(UserTable)
admin.site.register(ConnectionTable)
admin.site.register(ComplaintTable)
admin.site.register(PaymentTable)
admin.site.register(WaterQualityTable)
admin.site.register(AreaTable)
admin.site.register(ReaderTable)
admin.site.register(NotificationTable)
admin.site.register(SubAdminTable)
