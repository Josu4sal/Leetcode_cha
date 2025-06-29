roman_values={"I": 1,"V":5, "X" : 10, "L": 50, "C" : 100, "D" :500, "M" :1000}

def converter(rom_val, usr_num):
    total=0
    j=0
    while j< len(usr_num):
        if rom_val[usr_num[j]]< rom_val[usr_num[j+1]] and j+1< len(usr_num) :
            total+=roman_values[usr_num[j+1]]-rom_val[usr_num[j]]
            j+=2
        else:
            total+=roman_values[usr_num[j]]
            j+=1
    return total

print(converter(roman_values, "MCMXCIV"))
