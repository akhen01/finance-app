from django.db.models.base import Model as Model
from .models import Money, Budget
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import moneyForm, budgetForm

from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import datetime

class ObjDelete(LoginRequiredMixin, DeleteView):
    template_name = "PersonalF/object_delete.html"
    success_url = reverse_lazy("M-list")

    def get_object(self, queryset=None):
        model_name = self.kwargs.get('model_name')
        pk = self.kwargs.get("pk")

        model_mapping = {
            "Money":Money, 
            "Budget":Budget
        }

        model_class = model_mapping.get(model_name)
        obj = model_class.objects.get(pk=pk)
        if obj.owner != self.request.user:
            raise Http404("You do not have permission to view this object.")
        return obj
    
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return super().objDelete(request, *args, **kwargs)
    

class CreateBudeget(LoginRequiredMixin, CreateView):
    model = Budget
    form_class = budgetForm
    template_name = "PersonalF/createall.html"
    success_url = reverse_lazy("M-list")

    def form_valid(self, form):
        # Assign the currently logged-in user to the object
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    
class CreateMoney(LoginRequiredMixin, CreateView):
    model = Money
    form_class = moneyForm
    template_name = "PersonalF/createall.html"
    success_url = reverse_lazy("M-list")

    def form_valid(self, form):
        # Assign the currently logged-in user to the object
        form.instance.owner = self.request.user
        return super().form_valid(form)


class StatusLsit(LoginRequiredMixin, ListView):
    model = Budget
    template_name = "PersonalF/status.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_month = datetime.now().month
        income = Money.objects.filter(owner=self.request.user).filter(Mtype="income").filter(date__month=current_month)
        expence = Money.objects.filter(owner=self.request.user).filter(Mtype="expence").filter(date__month=current_month)
        total_income = sum([i.amount for i in income])
        context["income"] = income
        context["expence"] = expence
        context["totalincome"] = total_income

        context["budget"] = Budget.objects.filter(owner=self.request.user).filter(for_month__month=current_month)

        return context
    
class Details(LoginRequiredMixin, DetailView):
    template_name = "PersonalF/details.html"

    def get_object(self, queryset=None):
        model_name = self.kwargs.get('model_name')
        pk = self.kwargs.get("pk")

        model_mapping = {
            "Money":Money, 
            "Budget":Budget
        }

        model_class = model_mapping.get(model_name)
        obj = model_class.objects.get(pk=pk)
        if obj.owner != self.request.user:
            raise Http404("You do not have permission to view this object.")
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context["object"] = self.get_object()
        return context
    
class Update(LoginRequiredMixin, UpdateView):
    model = Money
    fields = "__all__"
    template_name = "PersonalF/update.html"
    success_url = reverse_lazy("M-list")

    def get_object(self, queryset=None):
        model_name = self.kwargs.get('model_name')
        pk = self.kwargs.get("pk")

        model_mapping = {
            "Money":Money, 
            "Budget":Budget
        }

        model_class = model_mapping.get(model_name)
        obj = model_class.objects.get(pk=pk)
        if obj.owner != self.request.user:
            raise Http404("You do not have permission to view this object.")
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get('model_name')
        model_mapping = {
            "Money":moneyForm, 
            "Budget":budgetForm
        }
        obj = self.get_object()
        my_class = model_mapping.get(model_name)
        context["object"] = obj
        context["form"] = my_class(instance = obj)
        return context
    
    def post(self, request, *args, **kwargs):
        model_name = self.kwargs.get('model_name')
        model_mapping = {
            "Money":moneyForm, 
            "Budget":budgetForm
        }
        self.form_class = model_mapping.get(model_name)
        self.object = self.get_object()
        form = self.form_class(request.POST, instance = self.object)
        if form.is_valid():
            update = form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
              self.get_context_data(form=form))