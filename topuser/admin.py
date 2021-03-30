from django.contrib import admin

from .models import TopTwsScore, TopUserVolume, TopUserEco, TopUserEnv, TopUserHealth
# Register your models here.

admin.site.register(TopTwsScore),
admin.site.register(TopUserVolume),
admin.site.register(TopUserEco),
admin.site.register(TopUserEnv),
admin.site.register(TopUserHealth)