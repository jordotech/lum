from django.contrib import admin

from .models import Lab, Author, Publication

class PublicationsInline(admin.TabularInline):
    model = Publication.labs.through
    extra = 0

class AuthorsInline(admin.TabularInline):
    model = model = Author.labs.through
    extra = 0

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
    inlines = [PublicationsInline, AuthorsInline]
    search_fields = ('name', 'organization', 'department', 'address',)
    list_filter = ('country',)
admin.site.register(Lab, LabAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = (u'id', 'name')
    #raw_id_fields = ('labs',)
    search_fields = ('name',)
admin.site.register(Author, AuthorAdmin)


class PublicationAdmin(admin.ModelAdmin):
    list_display = (u'id', 'pmid', 'abstract', 'doi')
    raw_id_fields = ('authors',)
admin.site.register(Publication, PublicationAdmin)