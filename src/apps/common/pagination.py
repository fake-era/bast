from collections import OrderedDict

from rest_framework.pagination import \
    LimitOffsetPagination as _LimitOffsetPagination
from rest_framework.response import Response


def get_paginated_response(*,
                           pagination_class,
                           serializer_class,
                           queryset, request,
                           view, context=None,
                           **kwargs):
    paginator = pagination_class()

    page = paginator.paginate_queryset(queryset, request, view=view)

    if page is not None:
        serializer = serializer_class(page, many=True)
        if context is not None:
            serializer = serializer_class(page, many=True, context=context)
        return paginator.get_paginated_response(serializer.data, **kwargs)

    serializer = serializer_class(queryset, many=True)

    return Response(data=serializer.data)


class LimitOffsetPagination(_LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

    def get_paginated_data(self, data, **kwargs):
        response_data = OrderedDict(
            [(key, value) for key, value in kwargs.items()]
        )
        response_data = data.update(OrderedDict([
            ('limit', self.limit),
            ('offset', self.offset),
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
        return response_data

    def get_paginated_response(self, data, **kwargs):
        """
        We redefine this method in order to return `limit` and `offset`.
        This is used by the frontend to construct the pagination itself.
        """
        response_data = OrderedDict(
            [(key, value) for key, value in kwargs.items()]
        )
        response_data.update(OrderedDict([
            ('limit', self.limit),
            ('offset', self.offset),
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
        return Response(response_data)
