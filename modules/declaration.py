import requests
import pprint


class Declaration:
    def __init__(self, name):
        self.name = name
        self.declaration_id = self.get_declaration()['id']
        self.declaration = self.get_declaration_details()
        self.salary = self.get_salary()
        self.link = self.get_declaration_link()

    def get_declaration(self):
        url = 'https://public-api.nazk.gov.ua/v2/documents/list'
        params = {
            'query': self.name
        }

        response = requests.get(url, params=params)
        declarations = response.json()['data']
        for declaration in declarations:
            if declaration['declaration_type'] == 1:
                return declaration

    def get_declaration_details(self):
        url = 'https://public-api.nazk.gov.ua/v2/documents/'+self.declaration_id
        response = requests.get(url)
        return response.json()

    def get_declaration_link(self):
        return 'https://public.nazk.gov.ua/documents/' + self.declaration_id

    def get_salary(self):
        income_sources = self.declaration['data']['step_11']['data']
        total_income = 0
        for source in income_sources:
            if source['person_who_care'][0]['person'] == '1':
                total_income += int(source['sizeIncome'])

        return total_income


# declaration = Declaration("Петро Порошенко").get_declaration()
# print(pprint.pprint(declaration['data'][0]))
# print()
# print(pprint.pprint(declaration['data'][3]))
# print(declaration['data'][0]['data']['step_0']['data']['declaration_type'])
# print(declaration['data'][4]['declaration_type'])
# print(declaration['data'][0]['data']['step_1']['data']['workPost'])
