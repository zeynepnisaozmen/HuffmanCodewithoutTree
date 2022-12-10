import math
import sys
global olasılık
olasılık= []

class HuffmanKod:
    def __init__(self,olasılık):
        self.olasılık= olasılık

    def position(self, value, index):
        for j in range(len(self.olasılık)):
            if(value >= self.olasılık[j]):
                return j
        return index-1


    def hesapla(self):
        num = len(self.olasılık)
        huffman_kodu = [''] * num

        for i in range(num-2):
            val = self.olasılık[num-i-1] + self.olasılık[num-i-2]
            if(huffman_kodu[num - i - 1] != '' and huffman_kodu[num - i - 2] != ''):
                huffman_kodu[-1] = ['1' + symbol for symbol in huffman_kodu[-1]]
                huffman_kodu[-2] = ['0' + symbol for symbol in huffman_kodu[-2]]
            elif(huffman_kodu[num - i - 1] != ''):
                huffman_kodu[num - i - 2] = '0'
                huffman_kodu[-1] = ['1' + symbol for symbol in huffman_kodu[-1]]
            elif(huffman_kodu[num - i - 2] != ''):
                huffman_kodu[num - i - 1] = '1'
                huffman_kodu[-2] = ['0' + symbol for symbol in huffman_kodu[-2]]
            else:
                huffman_kodu[num - i - 1] = '1'
                huffman_kodu[num - i - 2] = '0'

            position = self.position(val, i)
            olasılık = self.olasılık[0:(len(self.olasılık) - 2)]
            olasılık.insert(position, val)
            if(isinstance(huffman_kodu[num - i - 2], list) and isinstance(huffman_kodu[num - i - 1], list)):
                complete_code = huffman_kodu[num - i - 1] + huffman_kodu[num - i - 2]
            elif(isinstance(huffman_kodu[num - i - 2], list)):
                complete_code = huffman_kodu[num - i - 2] + [huffman_kodu[num - i - 1]]
            elif(isinstance(huffman_kodu[num - i - 1], list)):
                complete_code = huffman_kodu[num - i - 1] + [huffman_kodu[num - i - 2]]
            else:
                complete_code = [huffman_kodu[num - i - 2], huffman_kodu[num - i - 1]]

            huffman_kodu = huffman_kodu[0:(len(huffman_kodu) - 2)]
            huffman_kodu.insert(position, complete_code)

        huffman_kodu[0] = ['0' + symbol for symbol in huffman_kodu[0]]
        huffman_kodu[1] = ['1' + symbol for symbol in huffman_kodu[1]]

        if(len(huffman_kodu[1]) == 0):
            huffman_kodu[1] = '1'

        count = 0
        final_code = ['']*num

        for i in range(2):
            for j in range(len(huffman_kodu[i])):
                final_code[count] = huffman_kodu[i][j]
                count += 1

        final_code = sorted(final_code, key=len)
        return final_code

string = input("Enter the string to compute Huffman Code: ")

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
length = len(string)

olasılık = [float("{:.2f}".format(frequency[1] / length)) for frequency in freq]
olasılık = sorted(olasılık, reverse=True)

huffmanClassObject = HuffmanKod(olasılık)
P = olasılık

huffman_kodu = huffmanClassObject.hesapla()

print(' Karakter | Huffman Kodu ')
print('----------------------')

for id, char in enumerate(freq):
    if huffman_kodu[id] == '':
        print(' %-4r |%12s' % (char[0], 1))
        continue
    print(' %-4r |%12s' % (char[0], huffman_kodu[id]))


