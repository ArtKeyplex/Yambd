import os

from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import (
    Categories,
    Comment,
    Genre,
    Genre,
    Title,
    Reviews,
    User,
)


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from *.csv"

    def handle(self, *args, **options):
        file_names = {
            'users': User,
            'category': Categories,
            'titles': Title,
            'genre': Genre,
            'genre_title': Genre,
            'review': Reviews,
            'comments': Comment,
        }

        for file in file_names:
            if User.objects.exists():
                print(f'{file} data already loaded...exiting.')
                print(ALREDY_LOADED_ERROR_MESSAGE)
                return
            print(f'Loading {file} data')

            directory = os.path.abspath('api_yamdb/static/data/')
            file_way = os.path.join(directory, file + '.csv')
            for row in DictReader(
                open(file_way, encoding="utf-8"),
                delimiter=';'
            ):
                object, created = file_names[file].objects.get_or_create(**row)
