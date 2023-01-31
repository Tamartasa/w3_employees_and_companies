import os
import datetime

import django
import csv

os.environ['DJANGO_SETTINGS_MODULE'] = 'employees_and_companies.settings'

django.setup()

from amp_comp_app.models import Person, Company, Employee

if __name__ == '__main__':


    with open('persons.csv','r') as fh:
        persons_file = csv.DictReader(fh, delimiter=',')
        for item in persons_file:
            Person(id=int(item['id']), first_name=item['first_name'], last_name=item['last_name'],
                   personal_email=item['personal_email'],gender=item['gender'],
                   birth_date=datetime.datetime.strptime(item['birth_date'], "%m/%d/%Y").date()).save()


    # with open('companies.csv', 'r', encoding='utf-8') as fh:
    #     companies_file = csv.DictReader(fh, delimiter=',')
    #     for item in companies_file:
    #         Company(id=int(item['id']), company_name=item['company_name'], country=item['country'],
    #                 city=item['city'], address=item['address'], phone_num=item['phone_num']).save()


    with open('employees.csv', 'r') as fh:
        employees_file = csv.DictReader(fh, delimiter=',')
        for item in employees_file:
            Employee(id=int(item['id']), person=Person.objects.get(id=item['person_id']),
                     company=Company.objects.get(id=item['company_id']),
                     job_title=item['job_title'], is_current_job=item['is_current_job'].title(),
                     company_email=item['company_email']).save()





