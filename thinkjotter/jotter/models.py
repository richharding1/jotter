from django.db import models

class Entry(models.Model):
    date = models.DateField()
    literature = models.CharField(max_length=50, null=True, blank=True)
    notes = models.TextField()
    def __str__(self):
        return f'Journal entry on {self.date}'

class Hashtag(models.Model):
    tag = models.CharField(max_length=50, null=True, blank=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='tag')
    def __str__(self):
        return f'Hashtag #{self.tag}'

class Category(models.Model):
    category = models.CharField(max_length=50, null=True, blank=True, choices=[
                ('diary', 'diary'), 
                ('contemplation', 'contemplation'), 
                ('study / learning', 'study / learning'),
                ('meeting', 'meeting'), 
                ('professional', 'professional'),
                ('exercise log', 'exercise log'), 
                ('other', 'other')


            ]
        )
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='category')
    def __str__(self):
        return f'Category {self.category}'