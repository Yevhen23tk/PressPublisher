from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import (NewspaperCreationForm,
                    NewspaperUpdateForm, TopicCreateForm, TopicUpdateForm, RedactorCreateForm, RedactorUpdateForm)
from .models import (Newspaper,
                     Topic,
                     Redactor)


# @login_required
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


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = 'topic_list'
    template_name = 'news/topic_list.html'
    paginate_by = 5


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic
    context_object_name = 'topic'
    template_name = 'news/topic_detail.html'


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    form_class = TopicCreateForm
    success_url = reverse_lazy("news:topic-list")
    template_name = 'news/topic_form.html'


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    form_class = TopicUpdateForm
    success_url = reverse_lazy("news:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("news:topic-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    context_object_name = 'redactor_list'
    template_name = 'news/redactor_list.html'
    paginate_by = 5


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    context_object_name = 'redactor'
    template_name = "news/redactor_detail.html"


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm
    success_url = reverse_lazy("news:redactor-list")
    template_name = 'news/redactor_form.html'


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    success_url = reverse_lazy("news:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("news:redactor-list")