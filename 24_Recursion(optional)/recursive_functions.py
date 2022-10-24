from typing import Optional


def to_power(x: Optional[int], exp: int) -> Optional[int]:
    '''
    Returns  x ^ exp
    >>> to_power(2, 3) == 8
    True
    >>> to_power(3.5, 2) == 12.25
    True
    >>> to_power(2, -1)
    ValueError: This function works only with exp > 0.
    '''
    
    
    if exp == 1:
        return x
    elif exp < 0:
        raise ValueError('This function works only with exp > 0')
    return x * to_power(x, exp - 1)


print(to_power(2, 3))
print(to_power(3.5, 2))
# print(to_power(2, -1))


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    '''
    Checks if input string is Palindrome
    >>> is_palindrome('mom')
    True
    >>> is_palindrome('sassas')
    True
    >>> is_palindrome('o')
    True
    '''
    
    
    if int(len(looking_str) / 2) == index:
        return True
    if int(len(looking_str) / 2 + 1) == index:
        return True
    if looking_str[index] != looking_str[-(index + 1)]:
        return False
    return is_palindrome(looking_str, index + 1)


print(is_palindrome('mom'))
print(is_palindrome('sassas'))
print(is_palindrome('o'))
print(is_palindrome('sassias'))


def mult(a: int, n: int) -> int:
    '''
    This function works only with positive integers
    >>> mult(2, 4) == 8
    True
    >>> mult(2, 0) == 0
    True
    >>> mult(2, -4)
    ValueError("This function works only with postive integers")
    '''
    
    
    if n == 1:
        return a
    elif n == 0:
        return 0
    elif n < 0:
        raise ValueError('This function works only with postive integers')
    return a + mult(a, n - 1)


print(mult(2, 4))
print(mult(2, 0))
# print(mult(2, -4))


def reverse(input_str: str) -> str:
    '''
    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
    '''
    
    
    if len(input_str) == 1:
        return input_str[-1]
    return input_str[-1] + reverse(input_str[:-1])


print(reverse('hello'))
print(reverse('o'))
print(reverse('urbanization'))


def sum_of_digits(digit_string: str) -> int:
    '''
    >>> sum_of_digits('26') == 8
    True
    >>> sum_of_digits('test')
    ValueError("input string must be digit string")
    '''
    
    
    if not digit_string.isdigit():
        raise ValueError('input string must be digit string')
    if len(digit_string) == 1:
        return int(digit_string[0])
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])


print(sum_of_digits('26'))
print(sum_of_digits('263'))
print(sum_of_digits('123456'))
print(sum_of_digits('test'))


def valid_parentheses(strng):
    '''
    task from codewars
    '''
    
    new_strng = ''
    for symbol in strng:
        if symbol in '()':
            new_strng += symbol
            
    def recursive_parentheses(new_strng):
        if len(new_strng) == 0:
            return True
        else:
            if '()' in new_strng:
                return recursive_parentheses(new_strng.replace('()', ''))
            return False
        
    return recursive_parentheses(new_strng)


print(valid_parentheses("hi(hi)()"))