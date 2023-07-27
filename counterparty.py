
class Counterparty:
    def __init__(self, **kwargs):
        client_data_defaults = {
            'id': '___',
            'name': '_______________________',
            'contract_date': '"___"________ ___г.',

            'representative_post': '_______________________',
            'representative_name': '_______________________',
            'representative_document': '______________________________________________',
            'document_number': '_________',
            'document_date': '"___"________ ___г.',

            'rental_period': '_______________',
            'rental_cost': '__________(_______)',
            'VAT': '__________(_______)',
            'security_payment': '_______________',

            'authorized_to_transfer_property': '______________________________________________',
            'authorized_to_return_property': '______________________________________________',

            'purposes_of_use': '___________________________________',
            'operating_address': '___________________________________',

            'address': '___________________________________',
            'post_address': '______________________________________________',
            'phone_number': '______________',
            'fax': '_____________',
            'email': '_______________________',

            'OGRN': '______________',
            'INN': '__________',
            'KPP': '_________',

            'payment_account': '____________________',
            'bank_name': '______________________________________________',
            'correspondent_account': '____________________',
            'BIK': '________',
        }
        for client_data, default in client_data_defaults.items():
            setattr(self, client_data, kwargs.get(client_data, default))

    def __repr__(self):
        dict_of_values = self.__dict__
        output = ''
        for attr in dict_of_values:
            if not callable(getattr(self, attr)) and not attr.startswith('__') and '_' not in str(dict_of_values[attr]):
                output += f' {attr}: {dict_of_values[attr]}'
        return output
