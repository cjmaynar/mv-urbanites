from django.contrib import admin

from page.models import Page, TextComponent

class ComponentInline(admin.StackedInline):
    model = TextComponent
    extra = 0

class PageAdmin(admin.ModelAdmin):
    inlines = [ComponentInline,]

    class Media:
        js = (
            '/static/js/jquery-1.9.1.min.js',
            '/static/js/jquery-ui-1.10.2.custom.min.js',
            '/static/js/admin.js',
        )

admin.site.register(Page, PageAdmin)
