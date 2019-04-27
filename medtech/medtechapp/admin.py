from django.contrib import admin
from .models import *
# from .models import Solutions
# from .models import UserInfo
# from .models import NewEntryTable


admin.site.register(Solutions)
# admin.site.register(UserInfo)
admin.site.register(NewEntryTable)
admin.site.register(DonationTable)
admin.site.register(Hospital)
# Register your models here.
