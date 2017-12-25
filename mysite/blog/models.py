from django.db import models
from django.utils import timezone
import random

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class GuessNumbers(models.Model):
    # 필요한 데이터 정의
    name = models.CharField(max_length = 24)
    blog = models.CharField(max_length = 255, default = '[1, 2, 3, 4, 5, 6]')
    text = models.CharField(max_length = 255)
    num_lotto = models.IntegerField(default = 5)
    update_date = models.DateTimeField()

    # 메소드 정의
    def generate(self):
        self.blog = ""
        origin = list(range(1,46)) #[1, 2, 3.....44, 45]
        for _ in range(0, self.num_lotto): # self.num_lotto 수만큼 반복해서 아래를 수행한다.
            random.shuffle(origin) # origin 리스트 순서를 섞는다.
            guess = origin[:6] #index번호 0부터 5 까지를 뽑아낸다.
            guess.sort()
            self.blog += str(guess) + '\n'
        self.update_date = timezone.now()