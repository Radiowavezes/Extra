'''
Module to validate email adresses
'''

class Authorization:
    '''
    A class to validate an email
    -------
    Atributes:
    email:str
        adress
    -------
    Methods:
    validate(email):
    Cheks if an email is corrects
    '''
    def __init__(self, email:str):
        self.email = validate(email)

    @staticmethod
    def validate(email):
        '''
        Cheks if every symbol in adress is allowed according to proper syntax.
        Allowed symbols are stored to the symbols string, '@' must appear only
        one time and the last part of domain must not be shorter than 2 chars
        '''
        symbols = '!#$%&\'*+-./=?^_`{|}~abcdefghijklmnopqrstuvwxyz0123456789'
        if email.count('@') == 1 and len(email.split('.')[-1]) > 2:
            for symbol in ''.join(email.split('@')):
                if symbol.lower() not in symbols:
                    raise ValueError("It's not an email address.")
            print('Hurray!!!')
            return email
        else:
            raise ValueError("It's not an email address.")


fake_gmail = Authorization('Radiowavezes@gmail.com')
