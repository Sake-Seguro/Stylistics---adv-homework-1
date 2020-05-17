
from application.salary import calculating_salary
from application.db.people import getting_employees_names
from datetime import datetime

if __name__ == '__main__':

  calculating_salary()
  current_date = datetime.now()
  getting_employees_names()
  
  print('\n', current_date)
