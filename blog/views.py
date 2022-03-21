from django.shortcuts import render
from django.conf import settings
from django.views.generic import ListView, DetailView
from .forms import ContactForm
from .models import Person, Works
from django.db.models import F
from django.core.mail import send_mail
from django.template import RequestContext

class HomeView(ListView):
    model = Person
    template_name = 'blog/index.html'
    context_object_name = 'profile'


class WorksPageView(ListView):
    model = Works
    template_name = 'blog/works.html'
    context_object_name = 'works'
    paginate_by = 2


class WorksByCategoryView(ListView):
    context_object_name = 'work'
    allow_empty = False

    def get_queryset(self):
        return Works.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works_category'] = Works.objects.get(slug=self.kwargs['slug'])
        return context


class GetWorkView(DetailView):
    model = Works
    template_name = 'blog/description_work.html'   

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['about_work'] = Works.objects.get(slug=self.kwargs['slug'])

        # просмотры поста
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()

        return context


def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            email_subject = 'Сообщение через контактную форму'
            email_body = {
                'Имя отправителя': form.cleaned_data['name'],                
                'email отправителя': form.cleaned_data['email'],
                'Тело сообщения': form.cleaned_data['message'],
            }  
            new_line = "\n\n"           
            message = (f"{new_line.join(f'{key}: {value}'  for key, value in email_body.items())}")   

            mail = send_mail(email_subject, message, settings.EMAIL_HOST_USER, ['zakharkevich.v@gmail.com'], fail_silently=True)
            if mail:
                return render(request, 'blog/messages/message-success.html')
            else: 
                return render(request, 'blog/messages/message-error.html')
    else:
        return render(request, 'blog/index.html')



def e_handler404(request):
    context = RequestContext(request)
    response = render('blog/404.html', context)
    response.status_code = 404
    return response
 
 
def e_handler500(request):
    context = RequestContext(request)
    response = render('500.html', context)
    response.status_code = 500
    return response