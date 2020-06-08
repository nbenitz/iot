
from django.db import models
from persona.models import User


class Topic(models.Model):
    id_topic = models.AutoField(primary_key=True)
    id_user_fk = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user_fk')
    topic = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'topic'
        
    def __str__(self):
        return self.topic
