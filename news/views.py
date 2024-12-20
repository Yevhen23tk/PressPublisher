from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from news.forms import (
    NewspaperCreationForm,
    NewspaperUpdateForm,
    TopicCreateForm,
    TopicUpdateForm,
    RedactorCreateForm,
    RedactorUpdateForm,
    NewspaperSearchForm,
    TopicSearchForm,
    RedactorSearchForm,
)

from news.models import (Newspaper,
                         Topic,
                         Redactor)


# @login_required
# def index(request):
#     num_newspapers = Newspaper.objects.count()
#     num_topics = Topic.objects.count()
#     num_redactors = Redactor.objects.count()
#     num_visits = request.session.get("num_visits", 0)
#     request.session["num_visits"] = num_visits + 1
#
#     context = {
#         "num_newspapers": num_newspapers,
#         "num_topics": num_topics,
#         "num_redactors": num_redactors,
#         "num_visits": num_visits + 1,
#     }
#
#     return render(request, "news/index.html", context=context)
class IndexView(TemplateView):
    template_name = "news/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get and update the session visit count
        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1

        # Add your model counts to the context
        context["num_newspapers"] = Newspaper.objects.count()
        context["num_topics"] = Topic.objects.count()
        context["num_redactors"] = Redactor.objects.count()
        context["num_visits"] = num_visits + 1

        return context


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    context_object_name = "newspaper_list"
    template_name = "news/newspaper_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = NewspaperSearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get("title")

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset


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
    # template_name = 'news/newspaper_confirm_delete.html'


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "news/topic_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)

        topic = self.request.GET.get("topic", "")

        context["search_form"] = TopicSearchForm(initial={"topic": topic})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        topic = self.request.GET.get("topic")

        if topic:
            queryset = queryset.filter(name__icontains=topic)

        return queryset


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic
    context_object_name = "topic"
    template_name = "news/topic_detail.html"


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    form_class = TopicCreateForm
    success_url = reverse_lazy("news:topic-list")
    template_name = "news/topic_form.html"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    form_class = TopicUpdateForm
    success_url = reverse_lazy("news:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("news:topic-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "news/redactor_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)

        first_name = self.request.GET.get("first_name", "")

        context["search_form"] = RedactorSearchForm(initial={"first_name": first_name})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        redactor = self.request.GET.get("first_name")

        if redactor:
            queryset = queryset.filter(
                Q(first_name__icontains=redactor)
                | Q(last_name__icontains=redactor)
                | Q(username__icontains=redactor)
            )
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    context_object_name = "redactor"
    template_name = "news/redactor_detail.html"


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm
    success_url = reverse_lazy("news:redactor-list")
    template_name = "news/redactor_form.html"


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    success_url = reverse_lazy("news:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("news:redactor-list")
