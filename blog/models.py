# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify

""" Excepton handling """
class ModelManager(models.Manager):
	def get_or_none(self, **kwargs):
		try:
			return self.get(**kwargs)
		except ObjectDoesNotExist:
			return None

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, blank=True, null=False)
    class Meta:
        abstract = True

class ClueType(BaseModel):
	objects = ModelManager()
	name = models.CharField(max_length=50, null=False, verbose_name="Name")
	description = models.TextField(null=True, blank=True, verbose_name="Description")
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

class Clue(BaseModel):
	objects = ModelManager()
	title = models.CharField(max_length=200, null=False, verbose_name="Title")
	short = models.TextField(max_length=200, null=False, verbose_name="Short Story")
	clue_type = models.ForeignKey(ClueType, null=False, blank=False)
	content = HTMLField(verbose_name="Story")
	slug = models.SlugField(unique=True)
	status = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title