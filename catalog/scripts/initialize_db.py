import pandas as pd
import numpy as np
import csv

from ..models import Employee, Department

FILE_NAME = 'data.csv'
SIZE_OF_EMPLOYEES = 31

fix = pd.read_csv('catalog/scripts/data.csv', quoting=csv.QUOTE_NONE, quotechar=" ", sep=',', encoding='utf8')


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


department = {0: 'Administrator',
              1: 'back-end dev',
              2: 'front-end dev'}

for i in np.arange(3):
    Department.objects.create(
        id=i,
        name=department[i]
    )

print(get_key(department, 'back-end dev'))
for i in np.arange(1, SIZE_OF_EMPLOYEES):
    Employee.objects.create(
        first_name=fix[' first_name'][i],
        second_name=fix[' second_name'][i],
        last_name=fix['last_name'][i],
        date_of_birth=fix[' date_of_birth'][i],
        phone_number=str(fix[' phone_number'][i]),
        start_date=fix[' start_date'][i],
        role=fix[' role'][i],
        departament=Department.objects.get(id=get_key(department, fix[' departament'][i]))
    )
