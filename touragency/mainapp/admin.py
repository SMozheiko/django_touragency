from django.contrib import admin

# Register your models here.
from mainapp.models import Brand, SizeType, Item, Collection, Kind, Slide


admin.site.register(Collection)
admin.site.register(Brand)
admin.site.register(Item)
admin.site.register(SizeType)
admin.site.register(Kind)
admin.site.register(Slide)
