from django.contrib import admin

# Register your models here.

from .models import Questions,Choice
admin.site.site_header="Polls Admin"
admin.site.site_title="Polls Admin Area"
admin.site.index_title="Welcome to the Polls Admin Area"

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['ques_text']}),
    ('Date Information',{'fields':['pub_date'],
    'classes':['collapse']}),]
    inlines=[ChoiceInline]
    

# admin.site.register(Questions)
# admin.site.register(Choice)
admin.site.register(Questions,QuestionAdmin)