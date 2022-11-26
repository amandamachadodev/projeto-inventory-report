import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        data = []
        if (not path.endswith(".csv")):
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as file:
                reader = csv.DictReader(file)
                for element in reader:
                    data.append(element)
                return data
