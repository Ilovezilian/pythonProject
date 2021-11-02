import threading, time

def thread_task(name, n):
    for i in range(n):
        print(name, i)

if __name__ == "__main__" :
    for i in range(10):
        T = threading.Thread(target=thread_task, args=(str(i), i))
        T.start()
        # time.sleep(10)

    time.sleep(10)
