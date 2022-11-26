from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):

        return (
            f"{super().generate(data)}\n"
            f"Produtos estocados por empresa:\n"
            f"{cls.get_quantity_products(data)}"
        )

    @classmethod
    def get_company(cls, data):
        company_products = dict()
        for element in data:
            if element["nome_da_empresa"] in company_products.keys():
                company_products[element["nome_da_empresa"]] += 1
            else:
                company_products[element["nome_da_empresa"]] = 1
        return company_products

    @classmethod
    def get_quantity_products(cls, data):
        products = cls.get_company(data)
        quantity_list = ""
        for title, quantity in products.items():
            quantity_list += f"- {title}: {quantity}\n"
        return quantity_list
