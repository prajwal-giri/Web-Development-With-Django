from django.contrib import admin
from .models import HeaderNav, FooterNav, HeroHeadSection, HeroMiddleSection, HeroEndSection
# Register your models here.

admin.site.register(HeaderNav)
admin.site.register(FooterNav)
admin.site.register(HeroHeadSection)
admin.site.register(HeroMiddleSection)
admin.site.register(HeroEndSection)
