import csv
import sys
from django.core.management.base import BaseCommand, CommandError
from catalog.models import Authors


class Command(BaseCommand):
    """
    Command to import authors' .csv file
    """
    help = "Insert authors from the CSV file. " \
        "CSV file name(s) should be passed."

    def add_arguments(self, parser):
        """ Command arguments (possible to enter one or more files) """
        parser.add_argument('csvfiles', nargs='+', type=str,
                            help="Insert authors from the CSV file.")

    def handle(self, *args, **options):
        for filename in options['csvfiles']:
            self.stdout.write(self.style.SUCCESS(
                'Reading: {}'.format(filename)))
            try:
                with open(filename, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    next(reader)
                    try:
                        for row in reader:
                            self.insert_author_to_db(row[0])
                            self.stdout.write(self.style.SUCCESS(
                                'Insert: {}'.format(row[0])))
                    except csv.Error as e:
                        sys.exit('file {}, line {}: {}'.format(
                            filename, reader.line_num, e))
            except FileNotFoundError:
                raise CommandError("File {} does not exist!".format(filename))

    def insert_author_to_db(self, name):
        try:
            Authors.objects.create(name=name)
        except Exception as e:
            raise CommandError(
                "Error in inserting the author: {} - {}".format(name, str(e)))
