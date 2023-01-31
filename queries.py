import datetime
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'employees_and_companies.settings'

django.setup()

from amp_comp_app.models import Person, Company, Employee




def get_person_name_by_id(person_id: int) -> str:
   """
   Given person id, return string that represents person full name
   :param person_id:
   :return:
   """
   # p = Person.objects.all().values('first_name').filter(id=person_id)
   # return p
   return Person.objects.get(id=person_id)


def get_people_by_age(age: int) -> list[Person]:
   """
   Given age in years, return list of persons of this age
   :param age:
   :return:
   """
   p = Person.objects.all()
   year = datetime.datetime.now().date().year - age
   p_list = p.filter(birth_date__year=year)
   return p_list


def get_people_cnt_by_gender(gender: str) -> list[Person]:
   """
   Given the gender, return list of people of this gender
   :param gender:
   :return:
   """

   ret_val = Person.objects.filter(gender=gender)
   return list(ret_val)


def get_companies_by_country(country: str) -> list[str]:
   """
   Given country name, return list of companies' names in this country
   :param country:
   :return:
   """
   c = Company.objects.filter(country__iexact=country)
   return list(c)


def get_company_employees(company_id: int, current_only: bool) -> list[Person]:
   """
   Given company id, return list of persons who work(ed) for this company
   :param company_id:
   :param current_only: if True, return only people who are currently work in the company
   :return:
   """
   if current_only == False:
      p = Person.objects.filter(employee__company__exact=company_id)
      return list(p)
   if current_only  == True:
      p = Person.objects.filter(employee__company__exact=company_id, employee__is_current_job__exact=True)
      return list(p)


def get_person_jobs(person_id: int) -> list[dict[str, str]]:
   """
   Given person_id, return list of dictionaries that map from company name to job title
   :param person_id:
   :return:
   """

   # p = Person.objects.get(id=person_id).company_set.values_list('company_name', 'employee__job_title')
   # jobs_list = []
   # for item in p:
   #    my_dict = {item[0]: item[1]}
   #    jobs_list.append(my_dict)
   # return jobs_list

   jobs = Employee.objects.prefetch_related('company').filter(person=person_id)
   for job in jobs:
      return [{job.company: job.job_title}]



if __name__ == '__main__':
   # print(get_person_name_by_id(4))
   # print(get_people_by_age(30))
   # print(get_people_cnt_by_gender('Male'))
   # print(get_companies_by_country('china'))
   # print(get_company_employees(7, False))
   # print(get_company_employees(7, True))
   print(get_person_jobs(4))
   print(get_person_jobs(5))