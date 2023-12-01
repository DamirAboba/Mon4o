from django.contrib import admin
from .models import Cabinet, UserActivity

admin.site.register(Cabinet)


class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('cabinet', 'start_time', 'end_time', 'amount')  # Отображаем поля в списке


admin.site.register(UserActivity, UserActivityAdmin)
