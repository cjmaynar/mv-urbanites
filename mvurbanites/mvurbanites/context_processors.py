from page.models import Page

def sections(request):
    return {'sections': Page.objects.published().filter(in_navigation=True)}

def is_production(request):
    from settings import PRODUCTION

    return {'is_production': PRODUCTION}
