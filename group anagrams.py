'''[
anagrams: words contain the same characters but in different order
for example war = raw = awr = wra
the program count the number of anageams for a given array of anagrams

'''





list = ["aba","ase","set","baa","rtt","ttr","wer","wre","wer","erw"]
hash_table = {}


for i in range(0, len(list)):
    char_sum = 0
    char_mult = 1
    for j in list[i]:
       char_sum += ord(j)
       char_mult = char_mult * ord(j)
       key_value = char_sum+char_mult
    if key_value in hash_table:
        get_elem = hash_table.get(key_value)
        get_elem[1] += 1

    else:
        hash_table[key_value] = [list[i], 1]

print(hash_table)







