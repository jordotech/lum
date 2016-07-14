from django.core.management.base import BaseCommand
from metapub import PubMedFetcher
import csv
from lum.models import Publication, Author, Lab
class Command(BaseCommand):
    help = "Import PMID data from csv"
    def get_doi(self, row):
        doi_url = row[14]
        if 'doi.org' in doi_url:
            return doi_url.split('http://dx.doi.org/')[-1]
        return ''
    def get_authors(self, row):
        authors_row = row[2]
        name_list =  authors_row.split(';')
        ret = []
        for name in name_list:
            author = Author.objects.get_or_create(name=name)[0]
            ret.append(author)
        return ret
    def get_pmid(self, row):
        if len(row[15]) > 0:
            return row[15]
        elif len(row[16]) > 0:
            return row[16]
        else:
            return ''
    def get_lab(self, row):
        lab = None
        organization = row[31]
        department = row[32]
        address = row[33]
        city = row[34]
        province = row[35]
        postal_code = row[36]
        country = row[37]
        try:
            lab = Lab.objects.get(address=address, city=city)
        except:
            lab = Lab(
                address=address,
                department=department,
                organization=organization,
                city=city,
                province=province,
                postal_code = postal_code,
                country=country,
            )
            lab.save()
        return lab
    def handle(self, *args, **options):
        csvfile = "pmids.csv"
        with open(csvfile, 'rU') as f:
            reader = csv.reader(f)

            count = 0
            for row in reader:
                if count == 0:
                    count += 1
                    continue #skip first header row
                if count == 10: break
                ref_id = row[0]
                ref_type = row[1]

                year = row[3]
                article_title = row[4]
                secondary_author = row[5]
                journal_title = row[6]
                place_published = row[7]
                publisher = row[8]
                volume = row[9]
                issue = row[10]
                pages = row[11]
                date = row[12] #bad data in csv, don't use...
                alt_journal = row[13]
                doi = self.get_doi(row)
                print doi
                #pmid_from_ref = row[15]
                #pmid_from_updates = row[16]
                pmid = self.get_pmid(row)
                abstract = row[17]


                url = row[18]
                file_attachments = row[19]
                author_address_from_pubmed = row[20]
                figure = row[21]
                cis_acc = row[22]
                access_date = row[23]
                luminex_product = row[24]
                db_name = row[25]
                db_provider = row[26]
                language = row[27]
                reprint_author_name = row[28]
                blank = row[29]
                reprint_author_email = row[30]


                cis_keywords = row[38]
                ecopy = row[39]
                paper_type = row[40]
                species = row[41]
                assay = row[42]
                sample_type = row[43]
                whos_kit = row[44]
                misc = row[45]
                application = row[46]
                market_segment = row[47]
                subsidiary_author = row[48]
                custom_6 = row[49]
                journal_keywords = row[50]
                issn = row[51]


                pub = Publication(
                    pmid=pmid,
                    doi=doi,
                    abstract=abstract,
                )
                fresh_data = None
                if len(pmid) < 1:
                    fetch = PubMedFetcher()
                    try:
                        fresh_data = fetch.article_by_doi(doi)
                        fresh_data = fresh_data.to_dict()
                    except:
                        pass
                    else:
                        pub.pmid = fresh_data['pmid']

                pub.save()
                authors = self.get_authors(row)
                for author in authors:
                    pub.authors.add(author)
                lab = self.get_lab(row)

                if lab:
                    for author in authors:
                        author.labs.add(lab)
                    pub.labs.add(lab)




                count += 1
