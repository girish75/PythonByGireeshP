import concurrent.futures
import time

def new_function(time_for_sleep=1):
    print(f'Sleeping {time_for_sleep} second...')
    time.sleep(time_for_sleep)
    return f'Done Sleeping...{time_for_sleep}'

if __name__ == "__main__":
    start = time.perf_counter()  # start time
    with concurrent.futures.ProcessPoolExecutor() as executor:
        time_for_sleep = [5,4,3,2,1]
        #results = [executor.submit(new_function, sec) for sec in time_for_sleep]
        results = executor.map(new_function, time_for_sleep)
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())
        for result in results:
            print(result)
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2 )} second(s)')