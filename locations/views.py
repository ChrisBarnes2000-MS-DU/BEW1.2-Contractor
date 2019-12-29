from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.urls import reverse_lazy

from locations.models import Question, Page

def logout_view(request):
    logout(request)

class PageListView(ListView):
    template_name = 'locations/list.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.all()

class PageDetailView(DetailView):
    model = Page
    template_name = 'locations/page.html'

class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageEditView(UpdateView):
    model = Page
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('list-page')


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
