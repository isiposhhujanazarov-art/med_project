from django.contrib import admin

from .models import (
    Specialis, Vrachi, Hospital, Polyklinika,
    Patient, Diagnozu, PoseheniePolik, ViduOperacuu
)

admin.site.register(Specialis)
admin.site.register(Vrachi)
admin.site.register(Hospital)
admin.site.register(Polyklinika)
admin.site.register(Patient)
admin.site.register(Diagnozu)
admin.site.register(PoseheniePolik)
admin.site.register(ViduOperacuu)