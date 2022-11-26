import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        data = cls.read(path)
        if type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
            
    @classmethod
    def read(cls, path):
        report = []
        with open(path, encoding="utf-8") as file:
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