import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        data = cls.read_file(path)
        if type == "simples":
            simple = SimpleReport.generate(data)
            return simple
        else:
            complete = CompleteReport.generate(data)
            return complete

    @classmethod
    def read_file(cls, path):
        report = []
        with open(path) as file:
            if path.endswith(".csv"):
                reader = csv.DictReader(file)
                for element in reader:
                    report.append(element)
                return report
            elif path.endswith(".json"):
                report = json.load(file)
                return report
            else:
                report = xmltodict.parse(file.read())["dataset"]["record"]
                return report
