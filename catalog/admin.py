from django.contrib import admin
from catalog.models import Authors, Books

''' Registering authors and books in the administration panel '''
admin.site.register(Authors)
admin.site.register(Books)
