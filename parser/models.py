from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Problem(models.Model):
    themes = models.TextField(verbose_name='Themes')
    number_solutions = models.IntegerField(**NULLABLE, verbose_name='Number solutions')
    problem_name = models.CharField(max_length=300, verbose_name='Problem name')
    number = models.CharField(max_length=200, verbose_name='Number')
    rating = models.IntegerField(**NULLABLE, verbose_name='Rating')
    is_used = models.BooleanField(default=False, verbose_name='Is_used')

    def __str__(self):
        return f'Problem: {self.problem_name}'

    class Meta:
        verbose_name = 'problem'
        verbose_name_plural = 'problems'
