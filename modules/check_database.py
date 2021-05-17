'''
Module for checking politicians for corruption.
'''

import os


def check_all_politicians(name: str):
    '''
    Check if person is a politician.
    '''
    path = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../database/all_politicians.txt'))
    with open(path, encoding='utf-8') as file:
        for line in file:
            names = set(name.lower().strip().split(' '))
            words = (line.lower().strip().split(' '))
            if names.issubset(words):
                return True, line.strip()
        return False, None


def check_knopkodavu(name: str):
    '''
    Check if politician is a button masher.
    '''
    path = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../database/knopkodavy.txt'))
    with open(path, encoding='utf-8') as file:
        for line in file:
            names = set(name.lower().strip().split(' '))
            words = (line.lower().strip().split(' '))
            if names.issubset(words):
                return True
        return False


def check_progulshiki(name: str):
    '''
    Check if politician skips meetings.
    '''
    path = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../database/progulshiki.txt'))
    with open(path, encoding='utf-8') as file:
        for line in file:
            names = set(name.lower().strip().split(' '))
            words = (line.lower().strip().split(' '))
            if names.issubset(words):
                return True
        return False


def check_vorishki(name: str):
    '''
    Check if politician has been involved in corruption schemes.
    '''
    path = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../database/vorishki.txt'))
    with open(path, encoding='utf-8') as file:
        for line in file:
            names = set(name.lower().strip().split(' '))
            words = (line.lower().strip().split(' '))
            if names.issubset(words):
                return True
        return False


def check_politician(name: str):
    '''
    Check politician for all three points.
    '''
    return check_vorishki(name), check_progulshiki(name), check_knopkodavu(name)
