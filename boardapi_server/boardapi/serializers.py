from .models import Board, Comment
from rest_framework import serializers

############ Comment ################


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'c_writer', 'c_note', 'c_date', 'updated_at']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'c_writer', 'c_note']

class CommentListView(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['c_writer', 'c_note', 'c_date']


############## Board #################


class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['b_no', 'b_title', 'b_note', 'b_writer', 'parent_no', 'b_date', 'b_count', 'updated_at', 'comments']


class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['b_title', 'b_note', 'b_writer']


class BoardUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['b_title', 'b_note']


class BoardDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Board
        fields = ['b_no', 'b_title', 'b_note', 'b_writer', 'b_date', 'comments']
