import statistics as st

inputdata = []
with open('inputdata.txt', 'r') as reader:
    for line in reader:
        inputdata.append(float(line))

with open('outputdata.txt', 'w') as f:
    f.write('Μέσος όρος = ' + str(format(st.mean(inputdata), '.3f')) + '\n')
    f.write('Τυπική απόκλιση = ' + str(format(st.stdev(inputdata), '.3f')))
