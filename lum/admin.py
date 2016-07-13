from django.contrib import admin

from .models import Lab, Author, Publication


class LabAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'name',
        'address',
        'organization',
        'department',
        'city',
        'province',
        'postal_code',
        'country',
        'phone',
    )
    search_fields = ('name',)
admin.site.register(Lab, LabAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = (u'id', 'name')
    raw_id_fields = ('labs',)
    search_fields = ('name',)
admin.site.register(Author, AuthorAdmin)


class PublicationAdmin(admin.ModelAdmin):
    list_display = (u'id', 'pmid', 'abstract', 'doi')
    raw_id_fields = ('authors',)
admin.site.register(Publication, PublicationAdmin)