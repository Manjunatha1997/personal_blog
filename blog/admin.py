from django.contrib import admin
from .models import Info,Experience,Skills,Contact,Portfolio

# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ['email','phone']
admin.site.register(Info,InfoAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title_or_designation','description','start_date','end_date','company']
admin.site.register(Experience,ExperienceAdmin)


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill_name','proficiency')
admin.site.register(Skills,SkillsAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','subject','email','tel']
admin.site.register(Contact,ContactAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['image']
admin.site.register(Portfolio,PortfolioAdmin)
