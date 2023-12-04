from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def products_pagination(request, products, results):
    ''' Handles Pagination '''
    paginator = Paginator(products, results)
    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        products = paginator.page(page_number)
    except EmptyPage:
        page_number = paginator.num_pages
        products = paginator.page(page_number)

    return products