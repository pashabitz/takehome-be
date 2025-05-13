from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import House
from .serializers import HouseSerializer

class HouseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def apply_query_filters(self, query_params, queryset):
        """
        Dynamically apply filters to the queryset based on query parameters.
        """
        allowed_filters = [
            "bathrooms",
            "bedrooms",
            "year_built",
        ]
        allowed_operators = [
            "eq",
            "gte",
            "lte",
        ]
        for param in query_params:
            print(f"Processing filter: {param}")
            operator = param.split('__')
            if len(operator) > 1:
                param_name = operator[0]
                operator = operator[1]
            else:
                param_name = operator[0]
                operator = 'eq'

            if param_name not in allowed_filters:
                print(f"Filter {param_name} is not allowed.")
                continue
            if operator not in allowed_operators:
                print(f"Operator {operator} is not allowed.")
                continue
            filter_value = query_params.get(param)
            try:
                filter_value = float(filter_value)
            except ValueError:
                print(f"Invalid filter value for {param}: {filter_value}")
                continue
            
            try:
                queryset = queryset.filter(**{param: filter_value})
            except Exception as e:
                print(f"Error applying filter {param}: {e}")
                continue
        return queryset
            
    @action(detail=False, methods=['get'])
    def query(self, request):
        queryset = House.objects.all()

        try:
            queryset = self.apply_query_filters(request.query_params, queryset)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)