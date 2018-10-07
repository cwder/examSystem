from django.db import models

# Create your models here.

class ChoiceInfo(models.Model):
    question_id = models.IntegerField(u'题库id',  help_text=u'题库唯一标识')
    question = models.CharField(u'问题', max_length=255,blank=True,null=True,help_text=u'题目')
    answer = models.IntegerField(u'答案', blank=True, null=True, help_text=u'答案')
    item1 = models.CharField(u'选项1', max_length=255, blank=True, null=True, help_text=u'选项一')
    item2 = models.CharField(u'选项2', max_length=255, blank=True, null=True, help_text=u'选项二')
    item3 = models.CharField(u'选项3', max_length=255, blank=True, null=True, help_text=u'选项三')
    item4 = models.CharField(u'选项4', max_length=255, blank=True, null=True, help_text=u'选项四')

    def __str__(self):
        return self.question