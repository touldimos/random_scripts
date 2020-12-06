s = input('Αλφαριθμητικό: ')

if len(s) == 1:
    print('Μήκος = 1')
else:
    alist = []
    cond = 0
    for i in range(len(s)):
        alist.append(s[i])
        adict = {s: len(s)}
        if (s[i] == s[-i - 1]):
            cond += 1
        else:
            cond += 0
    if cond == len(s):
        print(adict)
        print(alist)
    else:
        print('Δεν είναι παλίνδρομο')