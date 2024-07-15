from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'prep_time')
    search_fields = ('name', 'ingredients')
    list_filter = ('difficulty',)
    ordering = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            self.change_form_template = obj.name
        return form

    def change_view(self, request, object_id, form_url='', extra_context=None):
        recipe = self.get_object(request, object_id)
        extra_context = extra_context or {}
        if recipe:
            extra_context['title'] = f'Recipe: {recipe.name}'
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(Recipe, RecipeAdmin)
