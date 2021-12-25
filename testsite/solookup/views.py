from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views import generic
from django.views.generic import FormView, ListView, TemplateView 
from django.db.models import Q
from django.contrib import messages
import datetime
import io
import reportlab
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab_qrcode import QRCodeImage
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.rl_config import defaultPageSize
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import registerFont

from .models import Boat
from .forms import BoatForm
from .filters import BoatFilter

# View to make the PDF for a boat model with QR Code, Model, Serial Number, and Color
# @param:   request -> type of request (GET, POST, etc)
#           pk      -> primary key (so_num) of boat model being accessed
def generate_pdf(request, pk):
    # Set up fo the attachment to download
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Hinge_Sheet.pdf"'

    # Set the style for the PDF
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Top_CENTER',
                            parent=styles['Normal'],
                            fontName='Helvetica',
                            wordWrap='LTR',
                            alignment=TA_CENTER,
                            fontSize=26,
                            textColor=colors.black,
                            borderPadding=0,
                            leftIndent=0,
                            rightIndent=0,
                            spaceAfter=0,
                            spaceBefore=0,
                            splitLongWords=True,
                            spaceShrinkage=0.05,
                            ))
    styles.add(ParagraphStyle(name='Bottom_Center',
                            alignment=TA_LEFT,
                            fontName='Helvetica',
                            fontSize=7,
                            textColor=colors.darkgray,
                            leading=8,
                            textTransform='uppercase',
                            wordWrap='LTR',
                            splitLongWords=True,
                            spaceShrinkage=0.05,
                            ))

    # Get Boat Model using the primary key
    obj = Boat.objects.get(so_num=pk)

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(response)


    # Draw things on the PDF. Here's where the PDF generation happens.
    p.setFont("Helvetica", 26)
    p.drawString(230, 800, str(obj.model))
    p.drawString(170, 750, str(obj.so_num) + " - " + str(obj.dealer_name))
    p.drawString(230, 700, str(obj.color))
    p.drawString(230, 650, str(obj.serial_num))
    qr = QRCodeImage('tidewaterprodsite.pythonanywhere.com/solookup/' + str(obj.so_num), size=80 * mm)
    qr.drawOn(p, 182, 300)

    p.setFont("Helvetica", 47)
    p.drawString(160, 100, str(obj.serial_num))

    p.setTitle(str(obj.so_num) + "_Hinge_Sheet")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # return the rendered PDF as a attachment
    return response

# Error page
# @param:   request -> type of request (GET, POST, etc)
def nocontext(request):
    return HttpResponse("You reached a page with an illegal url. Should not be able to reach here in the first place.")

# Function that updates the current step of a boat
# @param:   request -> type of request (GET, POST, etc)
#           pk      -> primary key (so_num) of boat model being accessed
def update_step(request, pk):
    if request.method == "POST":
        # Get step the boat model is being updated too
        update = request.POST.get('Production_Steps')
        model = Boat
        
        # Set the current step to the update step
        if update == "gel":
            obj = Boat.objects.get(so_num=pk)
            obj.gel = datetime.date.today()
            obj.save()
        elif update == "skin":
            obj = Boat.objects.get(so_num=pk)
            obj.skin = datetime.date.today()
            obj.save()
        elif update == "bulk":
            obj = Boat.objects.get(so_num=pk)
            obj.bulk = datetime.date.today()
            obj.save()
        elif update == "floor":
            obj = Boat.objects.get(so_num=pk)
            obj.floor = datetime.date.today()
            obj.save()
        elif update == "box":
            obj = Boat.objects.get(so_num=pk)
            obj.box = datetime.date.today()
            obj.save()
        elif update == "pull":
            obj = Boat.objects.get(so_num=pk)
            obj.pull = datetime.date.today()
            obj.save()
        elif update == "grind":
            obj = Boat.objects.get(so_num=pk)
            obj.grind = datetime.date.today()
            obj.save()
        elif update == "cut":
            obj = Boat.objects.get(so_num=pk)
            obj.cut = datetime.date.today()
            obj.save()
        elif update == "patch":
            obj = Boat.objects.get(so_num=pk)
            obj.patch = datetime.date.today()
            obj.save()
        elif update == "hw":
            obj = Boat.objects.get(so_num=pk)
            obj.hw = datetime.date.today()
            obj.save()
        elif update == "cap":
            obj = Boat.objects.get(so_num=pk)
            obj.cap = datetime.date.today()
            obj.save()
        elif update == "foam":
            obj = Boat.objects.get(so_num=pk)
            obj.foam = datetime.date.today()
            obj.save()
        elif update == "con":
            obj = Boat.objects.get(so_num=pk)
            obj.con = datetime.date.today()
            obj.save()
        elif update == "mtr":
            obj = Boat.objects.get(so_num=pk)
            obj.mtr = datetime.date.today()
            obj.save()
        elif update == "rig":
            obj = Boat.objects.get(so_num=pk)
            obj.rig = datetime.date.today()
            obj.save()
        elif update == "uph":
            obj = Boat.objects.get(so_num=pk)
            obj.uph = datetime.date.today()
            obj.save()
        elif update == "cc":
            obj = Boat.objects.get(so_num=pk)
            obj.cc = datetime.date.today()
            obj.save()
        elif update == "insp":
            obj = Boat.objects.get(so_num=pk)
            obj.insp = datetime.date.today()
            obj.save()
        elif update == "ship":
            obj = Boat.objects.get(so_num=pk)
            print(update)
            print(obj)
            obj.ship = datetime.date.today()
            print(obj.ship)
            obj.save()

        # redircet user to the homepage
        return HttpResponseRedirect('/solookup/')

# Function to process data to save a new boat
# @param:   request -> type of request (GET, POST, etc)
def process_form_data(request):
    if request.method == "POST":
        post_data = request.POST

        new_boat = Boat(
            so_num = post_data['so_num'],
            model = post_data['model'],
            color = post_data['color'],
            dealer_name = post_data['dealer_name'],
            motor = post_data['motor'],
            anticipated_Start = post_data['anticipated_Start'],
            serial_num = post_data['serial_num']
        )

        # save the new boat into the table
        try:
            new_boat.save()
        except:
            messages.error(request,'There was an Error creating the boat')
            return HttpResponseRedirect('/solookup/newboat/')
        

        return HttpResponseRedirect('../../%s/' % (post_data['so_num']))
    else:
        form = BoatForm()
        return HttpResponse("This page is not supposed to be reachable, meant for POST request")


# Page to render the Boat Model for a certain boat
# @param:   generic.Detailview -> Django built-in Detail view to render html with boat info
class DetailView(generic.DetailView):
    model = Boat
    template_name = 'solookup/boat_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boats'] = Boat.objects.all()
        # print(context['boats'])
        return context

# Page to generate the Form for a new Boat
# @param:   generic.Createview -> Django built-in view to render html with form
class BoatGenerateView(generic.CreateView):
    model = Boat
    form_class = BoatForm

# Page to generate html from a given search
# @param:   ListView -> Django built-in view to render html with queried boats
class SearchResultsView(ListView):
    model = Boat
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Boat.objects.filter(so_num__icontains=query)
        return object_list

# Page to view all boats in the database
# @param:   ListView -> Django built-in view to render html with queried boats
class AllBoatsView(ListView):
    model = Boat
    template_name = "solookup/boat_full_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BoatFilter(self.request.GET, queryset=self.get_queryset())
        return context

    # def get_queryset(self):
    #     object_list = Boat.objects.all()
    #     return object_list

# Function to render html for the homepage
# @param:   request -> type of request (GET, POST, etc)
def home(request):
    return render(request, 'solookup/home.html')
