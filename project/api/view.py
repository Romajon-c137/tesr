from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import *
from apps.main.models import Lab, Result


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ResultViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    http_method_names = ['post']
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    # pagination_class = StandardResultsSetPagination


class LabAPIView(APIView):
    def get(self, request):
        labs = Lab.objects.all()
        serializer = LabSerializer(labs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        new_data = request.data
        try:
            lab = Lab.objects.get(oder_number=new_data['oder_number'])
            serializer = LabSerializer(lab, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Lab.DoesNotExist:
            serializer = LabSerializer(data=new_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)