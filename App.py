from MaxHeap import MaxHeap
import random

def test():
    l = [random.randint(1,10000) for x in range(500)]
    m = MaxHeap(initValues=set(l))

    print(m.pop())
    print(m)


if __name__ == "__main__":
    test()
