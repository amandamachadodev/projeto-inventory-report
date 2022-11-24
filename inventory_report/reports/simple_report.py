class SimpleReport:
    @classmethod
    def generate(cls, data):
        return (
            f'Data de fabricação mais antiga: '
            f'{cls.get_date_fabrication(data)}\n'
            f'Data de validade mais próxima: '
            f'{cls.get_date_validation(data)}\n'
            f'Empresa com mais produtos: '
            f'{cls.get_company_more_products(data)}'
        )

    @classmethod
    def get_date_fabrication(cls, data):
        return min([product['data_de_fabricacao'] for product in data])

    @classmethod
    def get_date_validation(cls, data):
        return min([product['data_de_validade'] for product in data])

    @classmethod
    def get_company_more_products(cls, data):
        return max(
            [product['nome_da_empresa'] for product in data],
            key=[product['nome_da_empresa'] for product in data].count
        )
