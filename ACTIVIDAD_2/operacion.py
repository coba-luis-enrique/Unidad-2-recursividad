def binario(varible):
    if varible < 2:
        return varible
    else:
        return varible % 2 + (10*binario(varible // 2))