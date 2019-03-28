from converters.converter_baseclass import Converter
from main.decorators import Decorators

class BaseTwo(Converter):
    
    # override. use decorator to make safe and log source of any error
    @Decorators.catch_and_log
    def convert(self, number_to_convert):
        base10 = int(number_to_convert)
        base2 = self._divideByTwo(base10, [])
        return base2
    
    # convert base 10 number to base 2
    def _divideByTwo(self, base10convert, base2Stack = []):
        if (base10convert > 0):
            base2Stack.append(base10convert%2)
            return self._divideByTwo(int(base10convert/2), base2Stack)
        else:
            convertStackToStrings = map(str, base2Stack[::-1])
            base2Out = ''.join(convertStackToStrings)
            return base2Out
        