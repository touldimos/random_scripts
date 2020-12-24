import statistics as st

inputdata = []
with open('inputdata.txt', 'r') as fin:
    with open('outputdata.txt', 'w') as fout:
        for line in fin:
            inputdata.append(float(line))
        fout.write('Μέσος όρος = {:.3f} \nΤυπική απόκλιση = {:.3f}'.format(st.mean(inputdata), st.stdev(inputdata)))
