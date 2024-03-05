from django import forms
from .models import *
# from bootstrap_datepicker_plus import DatePickerInput

class AddEquipmentForm(forms.ModelForm):
    class Meta:
        model       = Equipment
        fields      = ['name', 'make', 'model','man_year', 'status']
        widgets     = {
            'status': forms.TextInput(attrs={'readonly':'readonly'})
        }

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model       = Equipment
        fields      = ['name', 'make','model', 'man_year', 'status']
        widgets     = {
            'name':forms.TextInput(attrs={'readonly':'readonly'}),
            'make':forms.TextInput(attrs={'readonly':'readonly'}),
            'model':forms.TextInput(attrs={'readonly':'readonly'}),
            'man_year':forms.TextInput(attrs={'readonly':'readonly'})

        }


class DieselPurchaseForm(forms.ModelForm):
    class Meta:
        model       = DieselPurchase
        fields      = ['machine', 'receiptNumber', 'date', 'supplier', 'unit_price', 'total_cost','litres']
        widgets     = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date', 'placeholder': 'mm/dd/yyyy'}),
            # 'date': forms.DateInput(attrs={'placeholder': 'mm/dd/yy'}),
            'litres':forms.TextInput(attrs={'readonly':'readonly'})
        }

class WorkLogForm(forms.ModelForm):
    class Meta:
        model       = WorkLog
        fields      = ['machine', 'customerName', 'phoneNumber', 'date', 'openingHr', 'closingHr', 'start_time', 'end_time', 'start_diesel', 'end_diesel', 'Fuel', 'amnt_earned', 'comment', 'paid']
        widgets     = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date', 'placeholder': 'mm/dd/yyyy'}),
            # 'date': forms.DateInput(attrs={'placeholder': 'mm/dd/yy'}),
            'phoneNumber': forms.TextInput(attrs={'placeholder':'+2637xxxxxxxx'})
        }


class MoveLogForm(forms.ModelForm):
    class Meta:
        model       = MoveLog
        fields      = ['machine', 'date', 'openingHr', 'closingHr', 'depart_from', 'destination','comment']
        widgets     = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date', 'placeholder': 'mm/dd/yyyy'}),
            # 'date': forms.DateInput(attrs={'placeholder': 'mm/dd/yy'}),
        }

class OtherExpensesForm(forms.ModelForm):
    class Meta:
        model       = OtherExpenses
        fields      = ['machine', 'receiptNumber', 'date', 'service', 'serviceProvider', 'total_cost']
        widgets     = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date', 'placeholder': 'mm/dd/yyyy'}),
            # 'date': forms.DateInput(attrs={'placeholder': 'mm/dd/yy'}),
        }