from django.contrib import admin
from .models import Users
from django.contrib.auth.hashers import (
    is_password_usable,
)
from .forms import UserForm

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = [field.name for field in Users._meta.fields]
    def save_model(self, request, obj:Users, form:UserForm, change):
        if form.is_valid() and obj.password!=None and obj.password !='' and is_password_usable(obj.password ):
            obj.set_password(obj.password)
        super(UserAdmin, self).save_model(request, obj, form, change)
