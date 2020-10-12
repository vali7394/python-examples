"""Write a function to compute 5/0 and use try/except to catch the exceptions."""


class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg


def div_by_zero():
    try:
        print(5 / 0)
    except ZeroDivisionError as r:
        raise CustomError('Division by Zero is nonsence')


div_by_zero()

"""Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print 
the user name of a given email address. Both user names and company names are composed of letters only. """


def get_usernames(emails):
    return list(map(lambda id: str(id).split('@')[0], emails))
