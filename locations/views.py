from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from locations.forms import PageForm
from locations.models import Question, Page

def logout_view(request):
    # Redirect to a success page in settings.py.
    logout(request)

class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {'pages': pages})

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific locations page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {'page': page})

class PageCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': PageForm()}
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.published_date = timezone.now()
            page.save()
            return HttpResponseRedirect(reverse_lazy('details-page', args=[page.slug]))
        return render(request, 'create.html', {'form': form})

class PageEditView(CreateView):
    model = Page

    def get(self, request, slug):
        page = get_object_or_404(Page, slug=slug)
        if request.method == "POST":
            form = PageForm(request.POST, instance=page)
            if form.is_valid():
                page = form.save(commit=False)
                page.author = request.user
                page.published_date = timezone.now()
                page.save()
                return redirect('details-page', slug=page.slug)
        else:
            form = PageForm(instance=page)
        return render(request, 'create.html', {'form': form})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
