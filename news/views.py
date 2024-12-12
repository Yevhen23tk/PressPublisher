from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import (NewspaperCreationForm,
                    NewspaperUpdateForm)
from .models import (Newspaper,
                     Topic,
                     Redactor)


@login_required
def index(request):
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        'num_newspapers': num_newspapers,
        'num_topics': num_topics,
        'num_redactors': num_redactors,
        'num_visits': num_visits + 1,
    }

    # return render(request, "news/index.html", context=context)
    return render(request, "news/index.html", context=context)


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    context_object_name = 'newspaper_list'
    template_name = "news/newspaper_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Newspaper.objects.all()


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    template_name = "news/newspaper_detail.html"


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperCreationForm
    success_url = reverse_lazy("news:newspaper-list")
    template_name = "news/newspaper_form.html"


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperUpdateForm
    success_url = reverse_lazy("news:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("news:newspaper-list")
