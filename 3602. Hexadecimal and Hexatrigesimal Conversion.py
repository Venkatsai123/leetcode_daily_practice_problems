def concatHex36( n):
    hexa = n*n
    hexatri = n*n*n

    hexa_str = ""
    hexa_tri_str = ""
    d= {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}
    while hexa >0 or hexatri >0:
        if(hexa>0):
            hexa_str += d[hexa%16]
            hexa //=16
        if(hexatri>0):
            hexa_tri_str += d[hexatri%36]
            hexatri //= 36
    return (hexa_str[::-1]+hexa_tri_str[::-1])
print(concatHex36(13))