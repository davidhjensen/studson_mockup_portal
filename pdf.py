# views.py
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from xhtml2pdf import pisa
from .models import Mockup
from PIL import Image

def generate_pdf(request):
    mockup = Mockup.objects.latest('id')  # Get the latest mockup from the database
    # Your image manipulation and PDF generation logic here using Pillow and ReportLab
    # Generate PDF content
    template_path = 'pdf_template.html'
    context = {'mockup': mockup}
    template = get_template(template_path)
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="mockup.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
