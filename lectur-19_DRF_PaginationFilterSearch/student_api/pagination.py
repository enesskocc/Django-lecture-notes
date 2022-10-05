from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination



class MyPageNumberPagination(PageNumberPagination):
    page_size = 20 ## eger burayi yoruma alirsam, gider settings'De bakar.
    page_query_param = 'sayfa'
    # page_size_query_param = 'limit' ## Url uzerinden page size belirlenebilir.


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 20
    limit_query_param = 'adet'
    offset_query_param = 'haric'
    


class MycursorPagination(CursorPagination):
    page_size=10
    ordering = "first_name"
    