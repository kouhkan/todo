from django.db import models
from django.utils import timezone


class Todo(models.Model):
	STATUS = (
		('w', 'Working'),
		('d', 'Done'),
		('c', 'Cancel'),
	)
	title = models.CharField(max_length=60)
	description = models.TextField(max_length=500)
	created = models.DateTimeField(auto_now_add=True)
	do_date = models.DateTimeField(default=timezone.now, verbose_name="Do Date")
	status = models.CharField(max_length=1, choices=STATUS, default='w')

	class Meta:
		ordering = ('-do_date', )

	def __str__(self):
		return self.title
