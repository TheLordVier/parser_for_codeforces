from django.contrib import admin
from .models import Problem


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('problem_name', 'themes', 'number_solutions', 'number', 'rating', 'is_used')
    list_filter = ('themes', 'rating', 'is_used')
    search_fields = ('problem_name', 'number')

    # Action to add to set the is_used flag
    actions = ['mark_as_used']

    def mark_as_used(self, request, queryset):
        updated_count = queryset.update(is_used=True)
        self.message_user(request, f'{updated_count} problem(s) have been marked as used.')

    mark_as_used.short_description = 'Mark as Used'


admin.site.register(Problem, ProblemAdmin)
