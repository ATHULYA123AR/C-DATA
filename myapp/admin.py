from django.contrib import admin
from myapp.models import Signup,Education,Personal,Professional, Medical,Financial

# Register your models here.
admin.site.register(Signup)
admin.site.register(Education)
admin.site.register(Personal)
admin.site.register(Professional)
admin.site.register(Medical)
admin.site.register(Financial)

