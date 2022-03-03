from django.contrib import admin
from home.models import owner,employee, total_employees

admin.site.register(owner)
admin.site.register(employee)
admin.site.register(total_employees)
