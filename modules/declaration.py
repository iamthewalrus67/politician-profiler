'''
Module for working with the state register of declarations
'''

import requests


class Declaration:
    '''
    Class for working with declarations.
    '''

    def __init__(self, name):
        '''
        Initialize declaration object.
        '''
        self.name = name
        declaration = self.get_declaration()
        if declaration is None:
            self.link = None
            self.salary = 0
        else:
            self.declaration_id = declaration['id']
            self.declaration = self.get_declaration_details()
            self.salary = self.get_salary()
            self.link = self.get_declaration_link()

    def get_declaration(self):
        '''
        Get latest yearly income declaration.
        '''
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
        '''
        Get detailed yearly income declaration.
        '''
        url = 'https://public-api.nazk.gov.ua/v2/documents/'+self.declaration_id
        response = requests.get(url)
        return response.json()

    def get_declaration_link(self):
        '''
        Get link to declaration.
        '''
        return 'https://public.nazk.gov.ua/documents/' + self.declaration_id

    def get_salary(self):
        '''
        Get total income from declaration. 
        '''
        income_sources = self.declaration['data']['step_11']['data']
        total_income = 0
        for source in income_sources:
            try:
                if source['person_who_care'][0]['person'] == '1':
                    total_income += int(source['sizeIncome'])
            except KeyError:
                if source['person'] == '1':
                    total_income += int(source['sizeIncome'])

        return total_income
