from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        'Sonho de valsa',
        'Lacta',
        '08/03/2022',
        '08/12/2022',
        '3690',
        'em ambiente arejado'
    )
    message = (
        f'O produto {product.nome_do_produto}'
        f' fabricado em {product.data_de_fabricacao}'
        f' por {product.nome_da_empresa}'
        f' com validade até {product.data_de_validade}'
        f' precisa ser armazenado {product.instrucoes_de_armazenamento}.'
    )
    assert product.__repr__() == message
