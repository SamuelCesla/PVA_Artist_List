

# Register your models here.
from django.contrib import admin
from .models import Label, Interpret, Diskografie, Tour, Program

admin.site.register(Label)
admin.site.register(Interpret)
admin.site.register(Diskografie)
admin.site.register(Tour)
admin.site.register(Program)