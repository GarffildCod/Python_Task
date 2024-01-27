list_text = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB"
list = [i for i in list_text]

def RLE(string):
    if not all(symmm.isupper() for symmm in string):
        raise 
    if not string:
        return ""
    current_symmm = string[0]
    current_count = 1
    result = ""
    for symmm in string[1:]:
        if symmm == current_symmm:
            current_count += 1
        else:
            result += current_symmm + str(current_count)
            current_symmm = symmm
            current_count = 1
    result += current_symmm + str(current_count)
    return result
print(RLE(list_text))