from django.contrib import admin
from pages import models


# Register your models here.
admin.site.register(models.home_content)
admin.site.register(models.about_content)
admin.site.register(models.service_content)
admin.site.register(models.portfolio_content)
admin.site.register(models.our_work_content)
admin.site.register(models.header)
admin.site.register(models.contact)
admin.site.register(models.reference)

admin.site.site_header = 'iCare Adminstration'
admin.site.site_title = 'icare Admin'
# admin.site.site_date =