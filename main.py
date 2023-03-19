# python3

def parallel_processing(n, m, data):
    output = []
    
    time = [0]*n

    for i, work_time in enumerate(data):
        minTime = min(time)
        thread = time.index(minTime)
        output.append((thread, minTime))
        time[thread] += work_time

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    res = parallel_processing(n, m, data)

    for i, j in res:
        print(i, j)

if __name__ == "__main__":
    main()
