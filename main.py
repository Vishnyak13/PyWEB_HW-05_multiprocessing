from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from multiprocessing import Process
from multiprocessing.dummy import Pool
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
    print(f'Main thread python done in {time() - timer:.3f} seconds')
    sleep(1)

    # test with 1 process
    timer_1 = time()
    p = Process(target=factorize, args=(128, 255, 99999, 10651060))
    p.start()
    p.join()
    print(f'Test 1 process done in {time() - timer_1:.3f} seconds')
    sleep(1)

    # test with threading in 4 threads
    timer_2 = time()
    threads = []
    for _ in range(4):
        thread = Thread(target=factorize, args=(128, 255, 99999, 10651060))
        threads.append(thread)
        thread.start()
    [thread.join() for thread in threads]
    print(f'Test with threading in 4 threads done in {time() - timer_2:.3f} seconds')
    sleep(1)

    # test with TreadPoolExecutor with 4 threads
    timer_3 = time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(factorize, (128, 255, 99999, 10651060))
    print(f'Test with TreadPoolExecutor with 4 threads done in {time() - timer_3:.3f} seconds')
    sleep(1)

    # test with ProcessPoolExecutor with 4 processes
    timer_4 = time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(factorize, (128, 255, 99999, 10651060))
    print(f'Test with ProcessPoolExecutor with 4 processes done in {time() - timer_4:.3f} seconds')
    sleep(1)

    # test with Pool with 4 processes
    timer_5 = time()
    with Pool(4) as pool:
        pool.map(factorize, (128, 255, 99999, 10651060))
    print(f'Test with Pool with 4 processes done in {time() - timer_5:.3f} seconds')


