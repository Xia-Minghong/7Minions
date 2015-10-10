from django.shortcuts import render


from rest_framework.decorators import list_route, detail_route
from rest_framework import viewsets, permissions
from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework.response import Response
# Create your views here.
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    # provided: [GET].list(), [GET].retrieve(), [POST].create(), [PUT].update(), and [DELETE].destroy()

    # http://127.0.0.1:8000/feedbacks/1/get_feedbacks
    @detail_route(methods=['get'])
    def get_feedbacks(self, request, **kwargs):
        feedback_list = Feedback.objects.filter(event = kwargs['pk'])
        serializer = FeedbackSerializer(feedback_list, many=True)
        return Response(serializer.data, content_type="application/json")


# Create feedback
# POST:  http://127.0.0.1:8000/feedbacks/
# {
#     "event": 2,
#     "content": "haihui",
#     "rating": 4
# }