from page.models import Page

def sections(request):
    return {'sections': Page.objects.filter(in_navigation=True)}
