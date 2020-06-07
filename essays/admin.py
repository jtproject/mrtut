from django.contrib import admin

# Register your models here.
from .models import Essay

#class PostVoteUpAdmin(admin.TabularInline):
    #model = PostUp
#class PostVoteDownAdmin(admin.TabularInline):
    #model = PostDown

class PostAdmin(admin.ModelAdmin):
    #inlines = [PostVoteUpAdmin, PostVoteDownAdmin]
    list_display = ['__str__', 'title', 'concat_content', 'user', 'timestamp']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Essay

admin.site.register(Essay, PostAdmin)
