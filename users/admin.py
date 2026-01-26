import uuid

from django.contrib import admin

from users.models import Doctor, Patient


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'specialization',
        'phone',
    )

    search_fields = (
        'first_name',
        'specialization',
        'phone',
    )
    exclude = ('last_login', 'password', 'groups', 'user_permissions', 'username', 'is_active',
               'is_superuser', 'is_staff', 'date_joined', 'role', 'email', 'Active')
    def save_model(self, request, obj, form, change):
        if not obj.username:
            obj.username = f"patient_{uuid.uuid4().hex[:10]}"
        super().save_model(request, obj, form, change)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'phone',
    )

    search_fields = (
        'first_name',
        'phone',
    )
    exclude = ('last_login', 'password', 'groups', 'user_permissions', 'username', 'is_active',
               'is_superuser', 'is_staff', 'date_joined', 'role', 'email', 'Active')
    def save_model(self, request, obj, form, change):
        if not obj.username:
            obj.username = f"patient_{uuid.uuid4().hex[:10]}"
        super().save_model(request, obj, form, change)


