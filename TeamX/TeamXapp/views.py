from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import AllMembers, ScrumTeam, LeaveCalendar
from .forms import ContactForm


# Create your views here.
def base(request):
    return render(request, "/base.html")


def login(request):
    target_page = "./registration/login.html"
    return render(request, target_page)


def index(request, *args, **kwargs):
    if User.is_authenticated:
        target_page = './html/index.html'
    elif not User.is_authenticated:
        target_page = './html/landingpage.html'

    return render(request, target_page)


def all_teams(request, *args, **kwargs):
    team = ScrumTeam.objects.all()
    context = {"teams" : team}
    target_page = './html/all_teams.html'
    return render(request, target_page, context) 


def about(request, *args, **kwargs):
    target_page = './html/about.html'
    return render(request,  target_page ) 


def help(request, *args, **kwargs):
    target_page = './html/help.html'
    return render(request,  target_page )     


def contact(request, *args, **kwargs):
    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
        args = {'form' : form, 'text' : text}
        return render(request, self.template_name, args)

    def sendmail(subject, body, sender):
        send_mail(
            'Subject here',
            'Here is the message.',
            'sageteamxofficial@gmail.com',
            ['sageteamxofficial@gmail.com'],
            fail_silently=False,
        )

    target_page = './html/contact.html'
    return render(request,  target_page )        


def dashboard(request, *args, **kwargs):
    team_count = ScrumTeam.objects.all().count()
    team_active = ScrumTeam.objects.filter(team_status = 1).count()
    people_count = AllMembers.objects.all().count()
    context = {"team_count"   : team_count,
               "people_count" : people_count,
               "team_active"  : team_active 
               }
    target_page = './html/dashboard.html'
    return render(request,  target_page , context)     


def team_details(request, pk, *args, **kwargs):    
    team_stuff = ScrumTeam.objects.get(pk=pk)
    people_stuff = AllMembers.objects.filter(scrum_team_name=pk)
    leave_stuff = LeaveCalendar.objects.all()
    context = {"team"       : team_stuff,
               "all_people" : people_stuff,
               "all_leave"  : leave_stuff}
    target_page = './html/a_team.html'
    return render(request,  target_page , context)

    
def error_404(request, exception):
        return render(request,'./html/error_404.html')


def error_500(request):
        return render(request,'./html/error_500.html')

