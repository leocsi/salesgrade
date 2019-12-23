import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Name(models.Model):
    user_name = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')
    age= models.IntegerField(default=0)
    prof_comm_score = models.IntegerField(default=1)
    prof_comm_status = models.IntegerField(default=1)
    teamwork_score = models.IntegerField(default=1)
    teamwork_status =  models.IntegerField(default=1)
    prod_knowledge_score =  models.IntegerField(default=1)
    prod_knowledge_status =  models.IntegerField(default=1)
    part_comp_score =  models.IntegerField(default=1)
    part_comp_status =  models.IntegerField(default=1)
    relations_score =  models.IntegerField(default=1)
    relations_status =  models.IntegerField(default=1)
    strategy_score =  models.IntegerField(default=1)
    strategy_status =  models.IntegerField(default=1)
    loyality_score =  models.IntegerField(default=1)
    loyality_status =  models.IntegerField(default=1)
    overall_score = models.IntegerField(default = 7)

    def __str__(self):
        return self.user_name
    def was_published_recently(self):
        return self.publication_date >= timezone.now() - datetime.timedelta(days=1)

# class Age(models.Model):
#     name = models.ForeignKey(Name, on_delete=models.CASCADE)
#     user_age = models.IntegerField(default='N/I')
#     def __str__(self):
#         return str(self.user_age)

# #kpi 01
# class ProfessionCommunication(models.Model):
#     name = models.ForeignKey(Name, on_delete=models.CASCADE)
#     prof_comm_score = models.IntegerField(default=1)
#     prof_comm_status = models.IntegerField(default=1)

# #kpi 02
# class Teamwork(models.Model):
#     name = models.ForeignKey(Name, on_delete=models.CASCADE)
#     teamwork_score = models.IntegerField(default=1)
#     teamwork_status =  models.IntegerField(default=1)

# #kpi 03
# class ProductKnowledge(models.Model):
#     name = models.ForeignKey(Name, on_delete=models.CASCADE)
#     prod_knowledge_score =  models.IntegerField(default=1)
#     prod_knowledge_status =  models.IntegerField(default=1)
    
# #kpi 04
# class PartnerCompetition(models.Model):
#     name = models.ForeignKey(Name, on_delete=models.CASCADE)
#     part_comp_score =  models.IntegerField(default=1)
#     part_comp_status =  models.IntegerField(default=1)

# #kpi 05
# class Relations(models.Model):
#     name = models.ForeignKey(Name, on_delete=models.CASCADE)
#     relations_score =  models.IntegerField(default=1)
#     relations_status =  models.IntegerField(default=1)

# #kpi 06
# class Strategy(models.Model):
#     name = models.ForeignKey(Name, on_delete=models.CASCADE)
#     strategy_score =  models.IntegerField(default=1)
#     Strategy_status =  models.IntegerField(default=1)

# #kpi 07
# class Loyality(models.Model):
#     name = models.ForeignKey(Name, on_delete=models.CASCADE)
#     loyality_score =  models.IntegerField(default=1)
#     loyality_status =  models.IntegerField(default=1)

# #overall
# class Overall(models.Model):
#     name = models.ForeignKey(Name, on_delete=models.CASCADE)
#     overall_score = models.IntegerField(default = 7)