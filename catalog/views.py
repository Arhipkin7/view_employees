import numpy as np

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django_filters.views import FilterView
from django.db.models.functions import Upper, Substr

from .models import Employee
from .filters import EmployeeFilter
from django.db.models.query import QuerySet
from collections import Counter

NUMBER_OF_GROUP = 7


# def letters(self):
#     letters = list([f['fl'] for f in Employee.objects.annotate(fl=Upper(Substr('last_name', 1, 1))).values('fl')])
#     k, m = divmod(len(letters), NUMBER_OF_GROUP)
#     letgroups = tuple((letters[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(NUMBER_OF_GROUP)))
#     str_for_links = {id: val[0] + '-' + val[-1] for id, val in enumerate(letgroups) if val}
#
#     print(letters)
#     letters_new = set(letters)
#     print(letters_new)
#     print(k)
#     print(m)
#     print(letgroups)
#     print(str_for_links)
#     return {
#         'letgroups': letgroups,
#         'letters': letters,
#         'str_for_links': str_for_links
#     }


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
    context_object_name = 'employees'

    @staticmethod
    def get_letter():
        letters = list(
            [f['let'] for f in Employee.objects.annotate(let=Upper(Substr('last_name', 1, 1))).values('let')])
        k, m = divmod(len(letters), NUMBER_OF_GROUP)
        get_groups = tuple((letters[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in np.arange(NUMBER_OF_GROUP)))
        str_for_links = {id: val[0] + '-' + val[-1] for id, val in enumerate(get_groups) if val}

        return {
            'get_groups': get_groups,
            'letters': letters,
            'str_for_links': str_for_links,
        }

    def get_queryset(self):
        letgroups = self.get_letter()
        try:
            # get_letters = self.request.GET['letters']
            return Employee.objects.annotate(let=Upper(Substr('last_name', 1, 1))).filter(
                let__in=letgroups['get_groups'][int(self.request.GET['letters'])])
        except KeyError:
            return Employee.objects.annotate(let=Upper(Substr('last_name', 1, 1))).filter(
                let__in=letgroups['get_groups'][0])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EmployeesAlphabetView, self).get_context_data(**kwargs)
        letgroups = self.get_letter()
        context['str_for_links'] = letgroups['str_for_links']
        return context
