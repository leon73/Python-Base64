__author__ = ('Leonardo F Oliveira')

__all__ = ['encode', 'decode']


class b64:

    def __init__(self):
        self.table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    def __str__(self):
        return 'Base64 Encoder / Decoder'

    def encode(self, text):
        bins = str()
        for c in text:
            bins += '{:0>8}'.format(str(bin(ord(c)))[2:])
        while len(bins) % 3:
            bins += '00000000'
        d = 1
        for i in range(6, len(bins) + int(len(bins) / 6), 7):
            bins = bins[:i] + ' ' + bins[i:]
        bins = bins.split(' ')
        if '' in bins:
            bins.remove('')
        base64 = str()
        for b in bins:
            if b == '000000':
                base64 += '='
            else:
                base64 += self.table[int(b, 2)]
        return base64

    def decode(self, text):
        bins = str()
        for c in text:
            if c == '=':
                bins += '000000'
            else:
                bins += '{:0>6}'.format(str(bin(self.table.index(c)))[2:])
        for i in range(8, len(bins) + int(len(bins) / 8), 9):
            bins = bins[:i] + ' ' + bins[i:]
        bins = bins.split(' ')
        if '' in bins:
            bins.remove('')
        text = str()
        for b in bins:
            if not b == '00000000':
                text += chr(int(b, 2))
        return text

    def test(self):
        e = 'Running Class Test'
        d = 'UnVubmluZyBDbGFzcyBUZXN0'        
        if e == decode(d) and d == encode(e):
            return True
        else:
            return False


_inst = b64()
encode = _inst.encode
decode = _inst.decode

if __name__ == '__main__':
    _inst.test()
