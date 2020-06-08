from django.contrib import admin

# Register your models here.
from .models import Station

class PostAdmin(admin.ModelAdmin):
    #inlines = [PostVoteUpAdmin, PostVoteDownAdmin]
    list_display = ['__str__', 'name', 'founder', 'founded_date']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Station

admin.site.register(Station, PostAdmin)
