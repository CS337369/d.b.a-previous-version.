from .models import Board, Comment
from .serializers import *
from .forms import CommentForm
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework import generics
from rest_framework.response import Response
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator




# class BoardViewSet(viewsets.ModelViewSet):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer

# BoardViewSetAsView = BoardViewSet.as_view({
#     "get": "list",
#     # "post": "create",
# })

class BoardListView(ListAPIView):
    # lookup_field = 'no'
    queryset = Board.objects.all().order_by('-b_no')
    serializer_class = BoardSerializer

# @csrf_exempt
# @method_decorator(csrf_exempt, name='dispatch')
class BoardCreateView(CreateAPIView):
    # lookup_field = 'no'
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer

    # def form_valid(self, form):
    #     board = form.save(commit=False)
    #     board.writer= self.request.user
    #     return super().form_valid(form)


class BoardDetailView(RetrieveAPIView):
    # lookup_field = 'no'
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        Board.objects.filter(pk=pk).update(b_count=F('b_count') + 1)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

# @csrf_exempt
class BoardUpdateView(UpdateAPIView):
    # lookup_field = 'no'
    queryset = Board.objects.all()
    serializer_class = BoardUpdateSerializer

# @csrf_exempt
class BoardDeleteView(DestroyAPIView):
    # lookup_field = 'no'
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

# @csrf_exempt
class CommentCreateView(generics.ListCreateAPIView):
    lookup_url_kwarg = "board_pk"
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # from_class = CommentForm

    # def post(self, request, Board_id, *args, **kwargs):
    #     # Board_id = self.board.pk
    #     serializer = CommentSerializer(data=request.data)
        
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(Board_id='board_pk')
        
    #     return Response(serializer.data)
        
    # def form_vaild(self, form):
    #     comment = form.save(commit=False)
    #     comment.writer = self.request.user
    #     comment.board = get_object_or_404(Board, pk=self.kwargs['board_pk'])
    #     comment.save()
    #     print(comment.writer)
    #     print(comment.board)
    #     return super().form_valid(form)


    def get_queryset(self):
        board_id = self.kwargs.get(self.lookup_url_kwarg)
        comments = Comment.objects.filter(Board_id=board_id)
        return comments

    def get_sucess_url(self):
        return reverse('BoardDetailView', kwargs = {'pk': self.object.board.pk})


# @csrf_exempt
class CommentDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # lookup_field = 'no'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# class CommentListView(ListAPIView):
#     # lookup_field = 'no'
#     queryset = Comment.objects.all()
#     serializer_class = CommentListView

#     def get_queryset(self):
#         return super().get_queryset()



