import time
import logging
from multiprocessing import Queue, Process

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorial(number, queue):
    uniq_numbers = []

    for i in range(1, number + 1):
        if number % i == 0:
            uniq_numbers.append(i)

    queue.put(uniq_numbers)


def factorize(*numbers):
    results = []
    processes = []
    queue = Queue()

    for number in numbers:
        pr = Process(target=factorial, args=(number, queue))
        pr.start()
        processes.append(pr)

    for pr in processes:
        pr.join()
        results.append(queue.get())

    return results


if __name__ == '__main__':
    time_start = time.time()

    for result in factorize(128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060, 128, 255, 99999, 10651060):
        print(result)

    time_end = time.time() - time_start

    print(f"execution time {time_end}")
