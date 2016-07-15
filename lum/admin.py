from django.contrib import admin

from .models import Lab, Author, Publication

class PublicationsInline(admin.TabularInline):
    model = Publication.labs.through
    extra = 0

class AuthorsInline(admin.TabularInline):
    model = model = Author.labs.through
    extra = 0
from django.db import models
class LabAdmin(admin.ModelAdmin):



    def get_queryset(self, request):
        qs = super(LabAdmin, self).get_queryset(request)
        #qs = qs.annotate(models.Count('author_set'))
        qs = qs.annotate(models.Count('pub_set'))
        return qs

    def num_authors(self, obj):
        #return obj.author_set__count
        return obj.author_set.count()

    def num_papers(self, obj):
        return obj.pub_set__count

    num_papers.admin_order_field = 'pub_set__count'
    #num_authors.admin_order_field = 'author_set__count'

    list_display = (
        u'id',
        'name',
        'num_authors',
        'num_papers',
        'address',
        'organization',
        'department',
        'city',
        'province',
        'postal_code',
        'country',
        'phone',
    )


    #inlines = [PublicationsInline, AuthorsInline]
    search_fields = ('name', 'organization', 'department', 'address',)
    list_filter = ('country',)
admin.site.register(Lab, LabAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = (u'id', 'name')
    #raw_id_fields = ('labs',)
    search_fields = ('name',)
admin.site.register(Author, AuthorAdmin)


class PublicationAdmin(admin.ModelAdmin):
    list_display = (u'id', 'pmid', 'title', 'doi')
    #raw_id_fields = ('authors',)
admin.site.register(Publication, PublicationAdmin)