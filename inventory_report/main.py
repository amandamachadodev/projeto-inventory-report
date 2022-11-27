import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    _, path, type_file = sys.argv

    if path.endswith(".csv"):
        data = InventoryRefactor(CsvImporter)
    elif path.endswith(".json"):
        data = InventoryRefactor(JsonImporter)
    else:
        data = InventoryRefactor(XmlImporter)

    sys.stdout.write(data.import_data(path, type_file))
