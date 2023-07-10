from django.contrib import admin
from .models import Interviewee,Experience,Position,MatchPosition,Project
# Register your models here.
admin.site.register(Interviewee)
admin.site.register(Experience)
admin.site.register(Position)
admin.site.register(MatchPosition)
admin.site.register(Project)
