from page.models import Page

def sections(request):
    return {'sections': Page.objects.published().filter(in_navigation=True)}
