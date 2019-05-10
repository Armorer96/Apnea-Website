from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib import admin
from .models import About
#from .models import Demo


class AboutAdmin(admin.ModelAdmin):
    fields =["about_title",
            "about_content"]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
'''
class DemoAdmin(admin.ModelAdmin):
    fields =["demo_content"
            ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
'''

admin.site.register(About,AboutAdmin)

#admin.site.register(Demo,DemoAdmin)

# Register your models here.
