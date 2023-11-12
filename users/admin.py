from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # 어드민 리스트에 보여질 필드들
    list_display = ['email', 'username', 'address', 'is_staff', ]
    # 어드민 검색에 사용될 필드들
    search_fields = ['email', 'username', ]
    # 어드민에서 필드를 편집할 때 나타날 필드 순서
    fieldsets = (
        (None, {'fields': ('email', 'password', 'address', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 
                                   'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # 새 사용자를 생성할 때 사용될 필드 순서
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'address', 'phone_number', 'password1', 'password2')}
        ),
    )

# Finally, register the CustomUserAdmin to handle CustomUser
admin.site.register(CustomUser, CustomUserAdmin)
