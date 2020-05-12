from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views import generic
from wiki.forms import PageForm
from wiki.models import Page
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.utils.text import slugify



class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })


class PageCreateView(CreateView):
    def get(self, request):
      context = {'form': PageForm()}
      return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
      form = PageForm(request.POST)
      if form.is_valid():
        page = form.save(commit=False)
        page.author = request.user
        page.save()
        return HttpResponseRedirect(
            reverse('wiki-details-page', args=[page.slug]))
      # else if form is not valid
      return render(request, 'create.html', { 'form': form })





class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page,
          'form': PageForm()
        })

    def post(self, request, slug):
      
      form = PageForm(request.POST)

      page = self.get_queryset().get(slug__iexact=slug)

      page.title = request.POST['title']
      page.content = request.POST['content']
      page.author = request.user
      page.slug = slugify(page.title)
      page.save()
      
      return HttpResponseRedirect(reverse('wiki-details-page', args=[page.slug]))


