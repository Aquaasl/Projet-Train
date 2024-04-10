from train.models import TrainConfig
from django.contrib import admin

# Register your models here.

admin.site.register(TrainConfig, TrainConfigAdmin)

class TrainConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'status')
    search_fields = ('name',)
    list_filter = ('status',)

