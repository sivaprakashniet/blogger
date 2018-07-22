# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.views.generic import TemplateView
from .models import Clue
from .forms import ClueForm
from django.contrib import messages
from django.template.defaultfilters import slugify
import datetime

class BlogListView(TemplateView):

	def get(self,request):
		template = 'blog/blogs.html' 
		data = Clue.objects.filter(status=True).order_by("-modified_date")
		return render(request, template, {'blogs': data})

class BlogDetailView(TemplateView):
	template = 'blog/view_blog.html'
	def get(self, request, slug):
		blog = Clue.objects.get(slug = slug)
		return render(request, self.template, {'blog':blog, 'slug':slug})
	def post(self, request, slug):
	    Clue.objects.filter(slug = slug).delete()
	    messages.add_message(request, messages.SUCCESS, u"Blog has been deleted successfully!")
	    return redirect('blogs')	
		
class BlogView(TemplateView):
	template = 'blog/create_blog.html' 
	def get(self,request):
		data = Clue.objects.filter(status=True)
		return render(request, self.template, {'form': ClueForm()})
	def post(self,request):
		form = ClueForm(request.POST)
		if form.is_valid():
			frm = form.save(commit=False)
			frm.created_by = request.user
			frm.slug = slugify(frm.title)
			frm.save()
			messages.add_message(request, messages.SUCCESS, u"New blog has been created successfully!")
			return redirect('blogs')
		messages.add_message(request, messages.ERROR, u"Unable to process your request!")
		return render(request,self.template,{'form': form})

class BlogEditView(TemplateView):
	template = 'blog/edit_blog.html' 
	def get(self,request, slug):
		data = Clue.objects.get(slug = slug)
		if ((data.created_by == request.user) or request.user.is_superuser):
			return render(request, self.template, {'form': ClueForm(instance=data), 'slug':slug})
		return render(request, '403.html')

	def post(self,request, slug):
		form = ClueForm(request.POST)
		if form.is_valid():
			blog = Clue.objects.filter(slug = slug)
			blog.update(title= request.POST.get('title'), 
				clue_type=request.POST.get('clue_type'), 
				short=request.POST.get('short'), 
				content= request.POST.get('content'),
				modified_date=datetime.datetime.now())
			messages.add_message(request, messages.SUCCESS, u"Blog has been updated successfully!")
			return redirect('blogs')
		messages.add_message(request, messages.ERROR, u"Unable to process your request!")
		return render(request,self.template,{'form': form, 'slug':slug})	


