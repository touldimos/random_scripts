import statistics

def squares(my_list):
    mean = statistics.mean(my_list)
    for i in my_list:
        yield abs(i - mean) ** 2

for i in squares([3, 4, 5]):
    print(i)