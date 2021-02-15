from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Board(models.Model):
    b_no = models.AutoField(primary_key=True)
    b_title = models.CharField(max_length=255)
    b_note = models.TextField(null=True, help_text="내용을 입력하세요.")
    b_writer = models.CharField(null=True, max_length=50)
    parent_no = models.IntegerField(default=0, null=True)
    b_count = models.PositiveIntegerField(default=0)
    b_date = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    usage_flag = models.CharField(null=True, max_length=10, default='1')

    def __str__(self):
        return self.b_title


class Comment(models.Model):
    Board = models.ForeignKey(Board, related_name='comments', on_delete=models.CASCADE)
    c_writer = models.CharField(User, null=True, max_length=50)
    c_note = models.TextField(null=True, help_text="내용을 입력하세요.")
    c_date = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.c_note
