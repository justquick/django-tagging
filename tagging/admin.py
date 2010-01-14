from django.contrib import admin
from django import forms
from tagging.models import Tag, TaggedItem
from tagging.forms import TagAdminForm
from tagging import registry

class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm

admin.site.register(TaggedItem)
admin.site.register(Tag, TagAdmin)

class TaggedAdmin(admin.ModelAdmin):
    change_form_template = 'admin/tagging/change_form.html'
    change_list_template = 'admin/tagging/change_list.html'
    
    class Media:
        js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.4.0/jquery.min.js',)

for model,modeladmin in admin.site._registry.items():
    if model in registry:
        admin.site.unregister(model)
        admin.site.register(model, type('newadmin', (TaggedAdmin, modeladmin.__class__,), {}))