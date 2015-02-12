from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    priority = models.PositiveIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])

    TODO = 0
    DOING = 1
    DONE = 2
    STATUS_OPTS = (
        (TODO, 'ToDo'),
        (DOING, 'Doing'),
        (DONE, 'Done')
    )

    status = models.PositiveSmallIntegerField(verbose_name="Task Status", choices=STATUS_OPTS, default=0)
    due_date = models.DateField()
