from django.contrib import admin
from django.db import models

from .models import Lab, Author, Publication, SearchStash, AuthorAffiliation

class PublicationsInline(admin.TabularInline):
    model = Publication.labs.through
    extra = 0
class SearchStashPubsInline(admin.TabularInline):
    model = Publication.labs.through
    extra = 0
class AuthorsInline(admin.TabularInline):
    model = model = Author.labs.through
    extra = 0

class SearchStashAdmin(admin.ModelAdmin):
    list_display = ('user', 'search_used',)
    #inlines = [SearchStashPubsInline,]
admin.site.register(SearchStash, SearchStashAdmin)

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

class AuthorAffiliationInline(admin.TabularInline):
    model = AuthorAffiliation
    extra = 0
class AuthorAdmin(admin.ModelAdmin):
    def affiliations_count(self, obj):
        return obj.authoraffiliation_set.all().count()
    list_display = (u'id',
                    'last_name',
                    'first_name',
                    'initials',
                    'affiliations_count',
                    )
    inlines = [AuthorAffiliationInline]
    search_fields = ('last_name',)
admin.site.register(Author, AuthorAdmin)

class AuthorAffAdmin(admin.ModelAdmin):
    list_display = (u'id',
                    'affiliation',
                    'author',
                    )
admin.site.register(AuthorAffiliation, AuthorAffAdmin)

class PublicationAdmin(admin.ModelAdmin):
    list_display = (u'id', 'pmid', 'title', 'doi')
    #raw_id_fields = ('authors',)
admin.site.register(Publication, PublicationAdmin)