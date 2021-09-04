from library.multiproc import *
from library.synchronus import *


start = time.perf_counter()  # start time
# Running task synchronously or sequentially
# do_function()
# do_function()


# EXAMPLE OF MULTIPROCESSING FOR 2 FUNCTIONS



start = time.perf_counter()



# doing multiprocessing using old method.
#These function runs in different processes and run in parallel.

#let us create 2 processes first and running the functions under those processes.



if __name__ == '__main__':
    # p1 = Process( target=some_function )
    # p2 = Process( target=some_function )
    #
    # p1.start()
    # p2.start()
    #
    # p1.join() # the join help us to complete all the processes first before command will go to the next commands written below.
    # p2.join()
    processes = []
    for _ in range(10):
        p = Process( target=some_function, args=[1.5] )
        p.start()
        processes.append(p)
    for process in processes:
        process.join() # the join help us to complete all the processes first before command will go to the next commands written below.


    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2 )} second(s)')

