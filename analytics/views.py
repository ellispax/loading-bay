from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from settings.models import Settings
from system.models import DieselPurchase, WorkLog, MoveLog
from django.http import JsonResponse
from django.db.models import Sum
from django.db.models.functions import TruncMonth
# from chartjs.views.lines import BaseLineChartView
from datetime import datetime, timedelta, date
import calendar
from calendar import monthrange
from django.db.models import Sum, Case, When, F, DecimalField


# Create your views here.


@login_required
def home(request):
    gen_settings = Settings.objects.get(id=1)
    context = {
        "page_nick": 'home',
        'title': 'Analytics',
        "head": "Analytics",
       
    }
    
    return render(request, 'analytics/index.html', context)



@login_required
def diesel_purchase_graph(request):
    monthly_data = DieselPurchase.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_litres=Sum('litres'), total_cost=Sum('total_cost')).order_by('month')

    print(monthly_data)
    context = {
        'monthly_data': monthly_data,
    }

    return render(request, 'analytics/diesel_purchase_graph.html', context)

@login_required
def income_graph(request):
    monthly_data = WorkLog.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_income=Sum('amnt_earned')).order_by('month')

    print(monthly_data)
    context = {
        'monthly_data': monthly_data,
    }

    return render(request, 'analytics/income_graph.html', context)  

# @login_required
# def work_hours(request):
#     combined_data = (
#         WorkLog.objects.annotate(month=TruncMonth('date'))
#         .values('month')
#         .annotate(
#             hours_worked=Sum('closingHr') - Sum('openingHr'),
#             hours_moved=Case(
#                 When(machine=F('machine'), then=F('closingHr') - F('openingHr')),
#                 default=0,
#                 output_field=DecimalField(),
#             ),
#         )
#         .order_by('month')
#     )

#     context = {'combined_data': combined_data}

#     return render(request, 'analytics/workHours.html', context)

# @login_required
# def work_hours(request):
#     work_data = WorkLog.objects.annotate(month=TruncMonth('date')).values('month').annotate(hours_worked=(Sum('closingHr') - Sum('openingHr'))).order_by('month')
#     move_data = MoveLog.objects.annotate(month=TruncMonth('date')).values('month').annotate(hours_moved=(Sum('closingHr') - Sum('openingHr'))).order_by('month')
#     monthly_data = (work_data, move_data)
#     print(monthly_data)

#     context ={
#         'work_data': work_data,
#         'move_data': move_data
#     }

#     return render(request, 'analytics/workHours.html', context)


# @login_required
# class MonthlyWorkingHoursChartView(BaseLineChartView):
#     def get_labels(self):
#         # Generate labels for the last 12 months
#         labels = [datetime.now().replace(day=1) - timedelta(days=x*30) for x in range(12)][::-1]
#         return [label.strftime('%b %Y') for label in labels]
    
#     def get_providers(self):
#         return ['WorkLog', 'MoveLog']

#     def get_data(self):
#         datasets = []
#         for model, label in zip([WorkLog, MoveLog], self.get_providers()):
#             data = []
#             for label in self.get_labels():
#                 start_date = label.replace(day=1)
#                 end_date = start_date.replace(day=calendar.monthrange(start_date.year, start_date.month)[1])
#                 total_hours = model.objects.filter(date__range=[start_date, end_date]).aggregate(
#                     total_hours=Sum('closingHr') - Sum('openingHr')
#                 )['total_hours'] or 0
#                 data.append(total_hours)
#             datasets.append(data)
#         return datasets
# # monthly_working_hours_chart = MonthlyWorkingHoursChartView.as_view()

