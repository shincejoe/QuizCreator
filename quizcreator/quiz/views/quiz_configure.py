from rest_framework import viewsets
from rest_framework.response import Response

from quiz.models import Quiz
from quiz.serializers.quiz_serializers import QuizFetchSerializer


class QuizConfigure(viewsets.ViewSet, viewsets.GenericViewSet):
    serializer_class = QuizFetchSerializer
    query_set = Quiz.objects.all()

    def list(self, request):
        try:
            initial_data = self.serializer_class(data=self.query_set, many=True)
            page = self.paginate_queryset(self.query_set)
            if page is not None:
                serialized_data = self.get_paginated_response(initial_data.data)
            else:
                serialized_data = initial_data.data

        except Exception as ex:
            print(str(ex))
            serialized_data = None
        return Response(serialized_data)

    def create(self, request):
        try:
            request_data = request.data
            '''
            updation
            '''
            if request_data['id']:
                quiz_object = Quiz.objects.filter(id=request_data['id'])
                serialized_data = self.serializer_class(data=request_data, instance=quiz_object)
                if serialized_data.is_valid():
                    serialized_data.save()
                    data = serialized_data.validated_data
                else:
                    data = None
            else:
                serialized_data = self.serializer_class(data=request_data)
                if serialized_data.is_valid():
                    serialized_data.save()
                    data = serialized_data.validated_data
                else:
                    data = None
            return Response(data=data)

        except Exception as ex:
            print(str(ex))
