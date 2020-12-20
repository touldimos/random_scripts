import statistics as st
def squares(*args):
    mesos=st.mean(args)
    for i in args:
        yield (st.mean(args)-i)**2
    return
for i in squares(3,4,5):
    print(i)
