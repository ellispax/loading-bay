from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from settings.models import Settings
from system.forms import DieselPurchaseForm, WorkLogForm, OtherExpensesForm, MoveLogForm
from django.contrib import messages
from system.models import DieselPurchase, WorkLog, OtherExpenses, MoveLog


#add advanced filtering for users to only view records associated with the equipment that they operate.
# Create your views here.


@login_required
def home(request):
    gen_settings = Settings.objects.get(id=1)
    context = {
        "page_nick": 'home',
        'title': 'Manager',
        "head": "Manager",
       
    }
    
    return render(request, 'manager/index.html', context)

@login_required
def Move_log_list(request):
    Move_log_records = MoveLog.objects.all().order_by('-date')
    gen_settings = Settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_machine'] = gen_settings.main_machine
    else:
        request.session['main_machine'] = ""

    context = {
        'title':'Movements Log',
        'head': 'Movements Log',
        'movelogs': Move_log_records
    }
    return render(request, 'manager/movelogList.html', context)
@login_required
def add_movelog(request):
    if request.method == 'POST':
        form = MoveLogForm(request.POST)
        if form.is_valid():
            record = form.save()
            message = ( f'New Movement Log record created succesfully.')
            messages.success(request,message)
            return redirect('movelog-list')
    else:
        form = MoveLogForm()

    gen_settings = Settings.objects.get(id=1)

    context = {
        'main_machine': gen_settings.main_machine,
        'title': 'Add Movement Log Record',
        'head': 'Movements Log Record',
        'form': form
    }
    return render(request, 'manager/addmovelog.html', context)


@login_required
def log_list(request):
    log_records = WorkLog.objects.all().order_by('-date')
    gen_settings = Settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_machine'] = gen_settings.main_machine
    else:
        request.session['main_machine'] = ""

    context = {
        'title':'Work Log',
        'head': 'Work Log',
        'logs': log_records
    }
    return render(request, 'manager/logList.html', context)



@login_required
def addWorkLog(request):
    if request.method == 'POST':
        form = WorkLogForm(request.POST)
        if form.is_valid():
            record = form.save()
            message = ( f'New Work Log record created succesfully.')
            messages.success(request,message)
            return redirect('log-list')
    else:
        form = WorkLogForm()

    gen_settings = Settings.objects.get(id=1)

    context = {
        'main_machine': gen_settings.main_machine,
        'title': 'Add Work Log Record',
        'head': 'Work Log Record',
        'form': form
    }
    return render(request, 'manager/addWorkLog.html', context)

@login_required
def diesel_list(request):
    diesel_records = DieselPurchase.objects.all()
    gen_settings = Settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_machine'] = gen_settings.main_machine
    else:
        request.session['main_machine'] = ""

    context = {
        'title':'Diesel Purchase',
        'head': 'Diesel Purchase Records',
        'dieselRecords': diesel_records
    }
    return render(request, 'manager/dieselList.html', context)


@login_required
def addDieselPurchaseRecord(request):
    if request.method == 'POST':
        form = DieselPurchaseForm(request.POST)
        if form.is_valid():
            record = form.save()
            message = ( f'New Diesel Purchase record created succesfully.')
            messages.success(request,message)
            return redirect('diesel-list')
    else:
        form = DieselPurchaseForm()
    
    gen_settings = Settings.objects.get(id=1)

    context = {
        'main_machine': gen_settings.main_machine,
        'title': 'Add Purchase Record',
        'head': 'Diesel Purchase Record',
        'form': form
    }
    return render(request, 'manager/dieselPurchase.html', context)

@login_required
def expense_list(request):
    expense_records = OtherExpenses.objects.all()
    gen_settings = Settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_machine'] = gen_settings.main_machine
    else:
        request.session['main_machine'] = ""

    context = {
        'title':'Other Expenses',
        'head': 'Other Expenses Records',
        'expenseRecords': expense_records
    }
    return render(request, 'manager/expenses.html', context)


@login_required
def addOtherExpense(request):
    if request.method == 'POST':
        form = OtherExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'New Expense record created successfully.')
            return redirect('expenses-list')
    else:
        form = OtherExpensesForm()

    gen_settings = Settings.objects.get(id=1)

    context = {
        'main_machine': gen_settings.main_machine,
        'title': 'Add Expense Record',
        'head': 'Expenses Record',
        'form': form
    }
    return render(request, 'manager/addExpense.html', context)