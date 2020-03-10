from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from repositories.models import Repository, Dependency
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the repository data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

DEPENDENCIES_NAMES = [
    'commander',
    'color',
    'ajax-request',
]

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from repository_data.csv into our Repository model"

    def handle(self, *args, **options):
        if Dependency.objects.exists() or Repository.objects.exists():
            print('Repository data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating dependency data")
        for dependency_name in DEPENDENCIES_NAMES:
            dep = Dependency(name=dependency_name)
            dep.save()
        print("Loading repository data for repositories available for repository")
        for row in DictReader(open('./repository_data.csv')):
            repository = Repository()
            repository.name = row['Name']
            raw_updated_date = row['Updated Date']
            updated_date = UTC.localize(
                datetime.strptime(raw_updated_date, DATETIME_FORMAT))
            repository.updated_date = updated_date
            repository.save()
            raw_dependency_names = row['Dependencies']
            dependency_names = [name for name in raw_dependency_names.split('| ') if name]
            for dep_name in dependency_names:
                dep = Dependency.objects.get(name=dep_name)
                repository.dependencies.add(dep)
            repository.save()
