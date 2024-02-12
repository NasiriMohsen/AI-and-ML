
def cal(i):
    list1 = []
    for i in range(1,i+1):
        y = (1)/i
        list1.append(y)
    avg = (1)/i
    avgsum = sum(list1)
    print(avg,avgsum)


while True:
    cal(int(input("len: ")))
