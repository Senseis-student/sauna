from django.db import models

class Map(models.Model):
	business_map = models.TextField('Карта')

	class Meta:
		verbose_name = 'Карта'
		verbose_name_plural = 'Карты'


