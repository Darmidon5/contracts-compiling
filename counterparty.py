from json import loads


class Counterparty:
    def __init__(self, json_dict):
        client_data_defaults = {
            'id': '________',
            'name': '___________________________',
            'contract_date': '"____"__________ ____г.',

            'representative_post': '                (должность)                ',
            'representative_name': '                                (Ф.И.О.)                                ',
            'representative_document': '     (наименование документа, подтверждающего полномочия)     ',
            'document_number': '_________',
            'document_date': '"____"__________ ____г.',

            'rental_period': '__________________',
            'rental_cost': '______ (_______)',
            'VAT': '_________(_____________)',
            'security_payment': '______________________',

            'authorized_to_transfer_property': '______________________________',
            'authorized_to_return_property': '______________________________',

            'purposes_of_use': '______________________________',
            'operating_address': '___________________________________',

            'address': '',
            'post_address': '',
            'phone_number': '',
            'fax': '',
            'email_1': '___________________________',
            'email_2': '',

            'OGRN': '',
            'INN': '',
            'KPP': '',

            'payment_account': '',
            'bank_name': '',
            'correspondent_account': '',
            'BIK': '',
        }
        json_dict = loads(json_dict)
        for client_data, default in client_data_defaults.items():
            setattr(self, client_data, json_dict.get(client_data, default))

    def __repr__(self):
        dict_of_values = self.__dict__
        output = ''
        for attr in dict_of_values:
            if not callable(getattr(self, attr)) and not attr.startswith('__') and '_' not in str(dict_of_values[attr]):
                output += f' {attr}: {dict_of_values[attr]}'
        return output




