from django.contrib import admin
from .models import Missing
from .models import Physical_Description
from .models import Origin
from .models import Found_Person
from .models import Place_Missing

admin.site.register(Missing)
admin.site.register(Physical_Description)
admin.site.register(Origin)
admin.site.register(Found_Person)
admin.site.register(Place_Missing)