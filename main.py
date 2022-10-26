import concurrent.futures
from time import time, sleep
from threading import Thread


def factorize(*number):
    result = []
    for i in number:
        operate_list = []
        for j in range(2, i + 1):
            if i % j == 0:
                operate_list.append(j)
        result.append(operate_list)
    return result


if __name__ == '__main__':
    # test main thread python
    timer = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(a, b, c, d, sep='\n')
    print(f'Main thread python done in {time() - timer:.2f} seconds')

    # test with threading in 4 threads
    timer_2 = time()
    threads = []
    for _ in range(4):
        thread = Thread(target=factorize, args=(128, 255, 99999, 10651060))
        threads.append(thread)
        thread.start()
    [thread.join() for thread in threads]
    print(f'Test with threading in 4 threads done in {time() - timer_2:.2f} seconds')

    # test with TreadPoolExecutor with 4 threads
    timer_3 = time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(factorize, (128, 255, 99999, 10651060))
    print(f'Test with TreadPoolExecutor with 4 threads done in {time() - timer_3:.2f} seconds')

    # test with ProcessPoolExecutor with 4 threads
    timer_4 = time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(factorize, (128, 255, 99999, 10651060))
    print(f'Test with ProcessPoolExecutor with 4 threads done in {time() - timer_4:.2f} seconds')

