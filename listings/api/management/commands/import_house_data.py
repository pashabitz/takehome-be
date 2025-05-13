import os
from django.core.management.base import BaseCommand, CommandError
from api.models import House

class Command(BaseCommand):
    help = 'Imports data about houses'
    def __init__(self):
        super().__init__()
        self.data_path = 'sample-data'

    def add_arguments(self, parser):
        # TODO: Add any arguments here
        pass

    def process_one_csv_file(self, filename):
        lines = []
        with open(os.path.join(self.data_path, filename), 'r') as file:
            header_line = file.readline()
            for line in file:
                fields = line.strip().split(',')
                # add to lines
                lines.append(fields)
        return lines

    def load_data(self):
        records_written = 0
        for filename in os.listdir(self.data_path):
            data = self.process_one_csv_file(filename)
            for line in data:
                try:
                    house = House.from_csv_line(line)
                    house.save()
                    records_written += 1
                except Exception as e:
                    raise CommandError(f"Error processing line: {line}, Error: {e}")
        print(f"Successfully imported {records_written} records.")

    def handle(self, *args, **options):
        self.load_data()