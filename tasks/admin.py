from django.contrib import admin
from .models import Taskstatus, Tag, Task


class TaskstatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Taskstatus._meta.fields]
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Taskstatus


admin.site.register(Taskstatus, TaskstatusAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]
    search_fields = ['name']

    class Meta:
        model = Tag


admin.site.register(Tag, TagAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.fields]
    search_fields = ['name', 'status', 'creator', 'assigned_to', 'tags']

    class Meta:
        model = Task


admin.site.register(Task, TaskAdmin)
