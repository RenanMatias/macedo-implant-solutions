import math

from django.core.paginator import Paginator


def make_pagination_range(page_range: dict, current_page: int, qty_pages=5) -> dict:
    """Create a pagination from the given amount

    Args:
        page_range (dict): Dictionary containing all pages
        current_page (int): Current Page
        qty_pages (int, optional): Total pages that are displayed in pagination. Defaults to 5.

    Returns:
        dict: Returns all the data needed to be applied to the template.
    """

    middle_range = math.ceil(qty_pages / 2)
    start_range = current_page - middle_range
    stop_range = (current_page + middle_range) - 1
    total_pages = len(page_range)

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    if stop_range >= total_pages:
        start_range = start_range - abs(total_pages - stop_range)

    pagination = page_range[start_range:stop_range]

    return {
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': qty_pages,
        'previous_page': current_page - 1,
        'current_page': current_page,
        'next_page': current_page + 1,
        'total_pages': total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
        'first_page_out_of_range': current_page < middle_range,
        'last_page_out_of_range': stop_range < total_pages,
    }


def make_pagination(request, queryset, per_page, qty_pages=5):
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(queryset, per_page)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        page_range=paginator.page_range,
        current_page=current_page,
        qty_pages=qty_pages,
    )

    return page_obj, pagination_range
