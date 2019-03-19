

class BaseTwo(object):


    def __init__(self):
        pass
        
    
    def convert(self, base10):
        base10 = int(base10)
        base2 = None
        try:
            base2 = self._divideByTwo(base10, [])
            return base2
        except:
            return "unknown error"
    
    def _divideByTwo(self, base10convert, base2Stack = []):
        if (base10convert > 0):
            base2Stack.append(base10convert%2)
            return self._divideByTwo(int(base10convert/2), base2Stack)
        else:
            convertStackToStrings = map(str, base2Stack[::-1])
            base2Out = ''.join(convertStackToStrings)
            return base2Out
        