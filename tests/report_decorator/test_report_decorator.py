from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorarate_relatorio():
    product = [{
        "id": 1,
        "nome_do_produto": "Sonho de valsa",
        "nome_da_empresa": "Lacta",
        "data_de_fabricacao": "08/03/2022",
        "data_de_validade": "08/12/2022",
        "numero_de_serie": "3690",
        "instrucoes_de_armazenamento": "Ambiente com clima fresco"
    }]
    colored = ColoredReport(SimpleReport).generate(product)

    expect = (
        f"\033[32mData de fabricação mais antiga:\033[0m \033[36m08/03/2022\033[On\n"
        f"\033[32mData de validade mais próxima:\033[0m \033[36m08/12/2022\033[0n\n"
        f"\033[32mEmpresa com mais produtos:\033[0m \033[31mLacta\033[0m"
        )
    assert colored == expect
