from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'status', 'due_date', 'completed_at')
    list_filter = ('priority', 'status')
    search_fields = ('title', 'description', 'user__username')