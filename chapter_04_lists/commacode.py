def comafy(list):
    val = ""
    for i in range(len(list)):
        if i == len(list) - 1:
            val  += "and " + list[i]
        else:
             val += list[i] + ", "
    
    return val

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comafy(spam))
print(comafy([]))
print(['apples', 'bananas'] in spam)