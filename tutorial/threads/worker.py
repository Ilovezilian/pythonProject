import threading, time, queue


# The worker thread gets jobs off the queue.  When the queue is empty, it
# assumes there will be no more work and exits.
# (Realistically workers will run until terminated.)
def worker():
    print("Runing worker")
    time.sleep(0.1)
    while True:
        try:
            arg = q.get(block=False)
        except queue.Empty:
            print("Worker", threading.currentThread(), end='')
            print("queue Empty")
            break
        else:
            print("Worker", threading.currentThread(), end='')
            print("Runing with args", arg)
            time.sleep(0.5)


# if __name__ == "__main__":
# Create queue
q = queue.Queue()

# Start a pool of 5 Workers
for i in range(5):
    t = threading.Thread(target=worker, name="worker%i" % (i + 1))
    t.start()

# Begin adding workers to the queue
for i in range(50):
    q.put(i)

# Give threads time to run
print("Main thread sleep")
time.sleep(5)
