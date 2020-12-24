import time

x = 100000 * 45
start_time = time.time()
if __name__ == '__main__':
    while x > 0:
        print("ho" + str(x))
        x = x - 1
    print(
        "---%s seconds---" % round((time.time() - start_time), )
    )
