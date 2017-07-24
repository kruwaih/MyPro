from django.contrib import admin
from .models import MyModel


class MyModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'update']
	search_fields = ['title']
	list_filter = ['title']

	class Meta:
		model = MyModel


admin.site.register(MyModel, MyModelAdmin)