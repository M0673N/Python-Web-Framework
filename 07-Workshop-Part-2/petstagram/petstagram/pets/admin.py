from django.contrib import admin

from petstagram.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'description')

    def likes_count(self, obj):
        return obj.like_set.count()


admin.site.register(Pet, PetAdmin)
