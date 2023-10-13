from django.shortcuts import render, redirect
from .form import *
from .models import *
# Create your views here.

def index(request):
    return render(request, "PersonalF/index.html")


def income_setup(request):
    income_type = incometype.objects.all()
    Itype_form = incomeT_registry()

    if request.method == "POST":
        form1 = incomeT_registry(request.POST)
        if form1.is_valid():
            form1.save()
    return render(request, "PersonalF/income.html", 
                {"income": Itype_form, 
                "inlist": income_type,
                })


def budget_setup(request):
    budget_type = budgettype.objects.all()
    Btype_form = budgetT_registry()

    if request.method == "POST":
        form2 = budgetT_registry(request.POST)
        if form2.is_valid():
            form2.save()
    return render(request, "PersonalF/budget.html", {
                "budget":Btype_form,   
                "bulist": budget_type
                })

def details(request):
    incomes_list = income.objects.all()
    budget_list = budget.objects.all()

    Income = income_registry()
    Budget = budget_registry()
    if request.method == "POST":
        detail_income = income_registry(request.POST)
        if detail_income.is_valid():
            detail_income.save()

    if request.method == "POST":
        detail_budget = budget_registry(request.POST)
        if detail_budget.is_valid():
            detail_budget.save()
        
    return render(request, "PersonalF/details.html",{
        "income":Income,
        "budget":Budget,
        "allincomes":incomes_list,
        "allbudgets":budget_list
    })


# deleting the income types and budget types

def deleteI(request, id):
    itype = incometype.objects.get(pk=id)
    itype.delete()

    return redirect('income')

def deleteG(request, id):
    gtype = budgettype.objects.get(pk=id)
    gtype.delete()

    return redirect('budget')


# deleting the details of income and budgets
def delete_DI(request, id):
    itype = income.objects.get(pk=id)
    itype.delete()

    return redirect('details')

def delete_DG(request, id):
    gtype = budget.objects.get(pk=id)
    gtype.delete()

    return redirect('details')

def status(request):

    expence_list = expence.objects.all()
    incomes_list = income.objects.all()
    budget_list = budget.objects.all()
    budgets = budgettype.objects.all()
    total_income = sum([i.amount for i in incomes_list])
    Alist = {}
    for i in budget_list:
        blist=[]
        for j in expence_list:
            if i.Itype == j.Itype:
                blist.append(j.amount)
        Alist[str(i.Itype)] = blist
    
    list1 = []
    for value in Alist.values():
        list1.append(sum(value))


            
    return render(request, "PersonalF/status.html",{
        "allincomes":incomes_list,
        "allbudgets":budget_list,
        "Totalincome":total_income,
        "Alist":Alist,
        "L":list1
    })

def daily_expences(request):
    today = today_expences_form()
    allExpences = expence.objects.all()
    if request.method == "POST":
        today_expence = today_expences_form(request.POST)
        if today_expence.is_valid():
            today_expence.save()
    return render(request, "PersonalF/daily_expences.html",{
        "Eform":today,
        "allExpences":allExpences
    })