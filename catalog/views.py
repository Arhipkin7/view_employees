from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django_filters.views import FilterView

from .models import Employee
from .filters import EmployeeFilter


class EmployeesView(FilterView):
    filterset_class = EmployeeFilter
    template_name = 'catalog/employees.html'
    context_object_name = 'employees'
    paginate_by = 10

    def get_filterset(self, filterset_class):
        r = self.request.GET
        if bool(r) and 'page' not in r:
            self.request.session['filter'] = r
        else:
            r = self.request.session.get('filter', self.request.GET)
        return filterset_class(r, queryset=Employee.objects.all())


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'catalog/employee_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Employee, pk=self.kwargs.get('pk'))


class EmployeesAlphabetView(ListView):
    model = Employee
    template_name = 'catalog/employees_alphabet.html'
