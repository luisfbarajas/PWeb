from django.contrib import admin
from .models import Player, Stadium, Team
# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Stadium)