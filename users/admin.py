from django.contrib import admin

from .models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]

    class Meta:
        model = SignUp

admin.site.register(SignUp)
