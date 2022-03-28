from admin_panel.models import ParsedDocument
from parser import Parser


def docs_parsing_cron_job():
    parser = Parser()
    docs = parser.parse()

    ParsedDocument.objects.all().delete()

    for doc in docs:
        parsed_document = ParsedDocument(title=doc[0], link=doc[1])
        parsed_document.save()
