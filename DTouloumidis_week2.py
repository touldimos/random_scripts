year = int(input('Year: '))
if year%100 == 0:
    if year%400 == 0:
        disekto = True
    else:
        disekto = False
else:
    if year%4 == 0:
        disekto = True
    else:
        disekto = False

print(disekto)