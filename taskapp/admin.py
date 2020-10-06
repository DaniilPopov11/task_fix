from django.contrib import admin

from .models import third_party,accounts

admin.site.register(third_party)
admin.site.register(accounts)