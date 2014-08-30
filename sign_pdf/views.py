from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

from precisely import settings
from precisely.settings import client
from sign_pdf.models import *

from django.core.urlresolvers import reverse
import urllib, datetime

import json

def home(request):
    docs = Document.objects.all()

    return render_to_response("index.html", {'docs':docs}, RequestContext(request)) 

def signed(request):
    if 'event' in request.GET:
        if request.GET['event'] == 'signature_request_signed':
            if 'signature_id' in request.GET:
                doc = Document.objects.get(signature_request_id=request.GET['signature_id'])
                doc.is_signed = True
                doc.save()
    return HttpResponseRedirect('/')

def send_to_sign(request):

    if request.POST:    
        subject = ''
        message = ''
        pdf_file = ''
        signer_name = ''
        signer_email = ''

        if 'name' in request.POST:
            signer_name = request.POST['name']

        if 'email' in request.POST:
            signer_email = request.POST['email']

        if 'subject' in request.POST:
            subject = request.POST['subject']

        if 'message' in request.POST:
            message = request.POST['message']

        if request.FILES:
            pdf_file = request.FILES['file']
        
        doc = Document()
        
        doc.receiver = signer_name
        doc.receiver_email = signer_email
        doc.pdf = pdf_file
        doc.save()

        try:

            files = [doc.get_file_url()]
        except:
            files = ['https://drive.google.com/file/d/0B0LIuW1RdH4XYl9vVHNJZ0JqMGc/edit?usp=sharing']
        
        signers = [
        {"name": signer_name, "email_address": signer_email}
        ]
         
        cc_email_addresses = ["tarek.sheasha@gmail.com"]
        signature_request = client.send_signature_request(
                                    test_mode=True, 
                                    files=None, 
                                    file_urls=files, 
                                    title=pdf_file.name, 
                                    subject=subject, 
                                    message=message, 
                                    signing_redirect_url=''.join([settings.DEPLOYED_ADDRESS, '/signed/']), 
                                    signers=signers, 
                                    cc_email_addresses=cc_email_addresses)

        doc.signature_request_id = signature_request.json_data['signatures'][0].json_data['signature_id']
        doc.save()
    return HttpResponseRedirect('/')
