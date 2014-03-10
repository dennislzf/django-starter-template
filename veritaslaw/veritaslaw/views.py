from django.shortcuts import render_to_response, render
from django.template import RequestContext



def home(request):
	form_args={}
	print form_args
	return render_to_response("home.html",form_args, context_instance=RequestContext(request))
