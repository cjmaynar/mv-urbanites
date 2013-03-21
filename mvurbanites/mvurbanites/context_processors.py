def sections(request):
    from page.models import Page

    return {'sections': Page.objects.filter(parent=None)}
