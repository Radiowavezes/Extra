class RomanNumerals:

    from_roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }

    to_roman_dict = {
        0: '',
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }


    def to_roman(self, val: int) -> str:
        expression = [int(num) * 10 ** dec for dec, num in (enumerate(str(val)[::-1]))]

        while len(expression) < 4:
            expression.append(0)

        expression.reverse()

        result = ''

        for number in expression:
            if RomanNumerals.to_roman_dict.get(number) is None:
                if expression.index(number) == 0:
                    result += RomanNumerals.to_roman_dict.get(1000) * (number // 1000)

                elif expression.index(number) == 1:
                    if number > 500:
                        result += RomanNumerals.to_roman_dict.get(500)
                        number %= 500
                    result += RomanNumerals.to_roman_dict.get(100) * (number // 100)

                elif expression.index(number) == 2:
                    if number > 50:
                        result += RomanNumerals.to_roman_dict.get(50)
                        number %= 50
                    result += RomanNumerals.to_roman_dict.get(10) * (number // 10)

                elif expression.index(number) == 3:
                    if number > 5:
                        result += RomanNumerals.to_roman_dict.get(5)
                        number %= 5
                    result += RomanNumerals.to_roman_dict.get(1) * number

            else:
                result += RomanNumerals.to_roman_dict.get(number)

        return result


    def from_roman(self, roman_num: str) -> int:
        ind = 0
        result = 0
        number = 0

        while ind < len(roman_num):
            if ind < len(roman_num) - 1:
                if (
                    roman_num[ind] == 'I' and roman_num[ind + 1] in 'VX'
                    or roman_num[ind] == 'X' and roman_num[ind + 1] in 'LC'
                    or roman_num[ind] == 'C' and roman_num[ind + 1] in 'DM'
                    ):
                    number = (
                        RomanNumerals.from_roman_dict.get(roman_num[ind + 1]) -
                        RomanNumerals.from_roman_dict.get(roman_num[ind])
                        )
                    ind += 2
                else:
                    number = RomanNumerals.from_roman_dict.get(roman_num[ind])
                    ind += 1
            else:
                number = RomanNumerals.from_roman_dict.get(roman_num[ind])
                ind += 1
            result += number

        return result


a = RomanNumerals()
print(a.from_roman('DCCCLXXXIV'))
print(a.to_roman(884))
 