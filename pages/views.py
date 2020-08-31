from django.shortcuts import render
from django.http import HttpResponse
from pages import models
import os

# Create your views here.
def index(request):
	home_content = models.home_content.objects.all()
	section = models.home_content.objects.all()
	contacts = models.contact.objects.all()
	header = models.header.objects.all()
	return render(request, 'index.html', {'home_content': home_content, 'section': section, 'contacts': contacts, 'header': header})


def about(request):
	about_content = models.about_content.objects.all()
	contacts = models.contact.objects.all()
	header = models.header.objects.all()
	return render(request, 'about.html', {'about_content': about_content, 'contacts': contacts, 'header': header})


def service(request):
	service_content = models.service_content.objects.all()
	contacts = models.contact.objects.all()
	header = models.header.objects.all()
	return render(request, 'service.html', {'service_content': service_content, 'contacts': contacts, 'header': header})


def our_work(request):
	our_work_content = models.our_work_content.objects.all()
	contacts = models.contact.objects.all()
	header = models.header.objects.all()
	return render(request, 'work.html', {'our_work_content': our_work_content, 'contacts': contacts, 'header': header})


def portfolio(request):
	portfolio_content = models.portfolio_content.objects.all()
	contacts = models.contact.objects.all()
	header = models.header.objects.all()
	return render(request, 'portfolio.html', {'portfolio_content': portfolio_content, 'contacts': contacts, 'header': header})


def base(request):
	head = models.header.objects.all()
	contacts = models.contact.objects.all()
	header = models.header.objects.all()
	return render(request, 'base.html', {'head': head, 'contacts': contacts, 'header': header})

def references(request):
	reference = models.reference.objects.all()
	header = models.header.objects.all()

	# gets file_size from the database
	# helps to display file size of the last uploaded documment/media/
	last_file = models.reference.objects.last()
	file_path = last_file.file
	full_path = "static/" + str(file_path)
	file_size = os.path.getsize(full_path)

	return render(request, 'references.html', {'header': header, 'references':reference, 'file_size': file_size})
