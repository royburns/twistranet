from django_twistranet.twistranet.models.community import Community   #, CommunityMembership
from django.contrib import admin

# class CommunityMembershipInline(admin.TabularInline):
#     model = CommunityMembership
#     extra = 1

class CommunityAdmin(admin.ModelAdmin):
    pass
    # inlines = (CommunityMembershipInline,)

admin.site.register(Community)