
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from falco.htmx import for_htmx
from falco.pagination import paginate_queryset
from falco.types import HttpRequest

from .forms import SomethingForm
from .models import Something


@for_htmx(use_partial="table")
def something_list(request: HttpRequest):
    somethings = Something.objects.order_by("-created_at")
    return TemplateResponse(
        request,
        "demo/something_list.html",
        context={"somethings_page": paginate_queryset(request, somethings), "fields": ('id', 'name', 'description', 'created', 'updated') },
    )


def something_detail(request: HttpRequest, pk):
    something = get_object_or_404(Something.objects, pk = pk)
    return TemplateResponse(
        request,
        "demo/something_detail.html",
        context={"something": something},
    )


def process_something_form(request: HttpRequest, pk = None):
    instance = get_object_or_404(Something.objects, pk= pk) if pk else None 
    form = SomethingForm(request.POST or None, instance=instance) 
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse("demo:something_detail", args=(pk,)) if pk else reverse("demo:something_list"))
    return TemplateResponse(
        request,
         "demo/something_form.html"  ,
        context={"instance": instance, "form": form},
    )

@require_http_methods(["DELETE", "POST"])

def something_delete(request: HttpRequest, pk):
    Something.objects.filter(pk=pk).delete()
    return HttpResponse() if request.htmx else redirect("demo:index")


