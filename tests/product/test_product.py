from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        'Sonho de valsa',
        'Lacta',
        '08/03/2022',
        '08/12/2022',
        '3690',
        'Ambiente com clima fresco'
    )
    assert product.id == 1
    assert product.nome_do_produto == 'Sonho de valsa'
    assert product.nome_da_empresa == 'Lacta'
    assert product.data_de_fabricacao == '08/03/2022'
    assert product.data_de_validade == '08/12/2022'
    assert product.numero_de_serie == '3690'
    assert product.instrucoes_de_armazenamento == 'Ambiente com clima fresco'
