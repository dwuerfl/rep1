import multiprocessing
import time


def calc_pi(threadNumber):
    summary =float(0)
    for i in range(0,k):
        pi=(((-1)^i)/(2*i +1))
        for j in range(k):
            summary =summary+pi
            print(summary)
    print("Finished: Thread",threadNumber)

if __name__=="__main__":
    k =int(input("How many iteration of (k) do u want?>"))
    startTime = time.time()
    myProcesses = []
    for i in range(4):
        p = multiprocessing.Process(target=calc_pi,
            args=(k,))
        myProcesses.append(p)
    for x in myProcesses:
        x.start()
    for x in myProcesses:
        x.join()
    endTime = time.time()
    print("runtime = ",endTime -
        startTime,"sec.")