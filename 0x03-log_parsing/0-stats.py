#!/usr/bin/python3
'''Script that reads stdin and computes metrics'''

import sys

def main():
    status = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    total = 0
    counter = 0

    try:
        for line in sys.stdin:
            line_list = line.split(" ")
            if len(line_list) > 4:
                code = line_list[-2]
                size = int(line_list[-1])
                if code in status:
                    status[code] += 1
                total += size
                counter += 1

            if counter == 10:
                counter = 0
                print('File size: {}'.format(total))
                for key, value in sorted(status.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))

    except KeyboardInterrupt:
        pass
    except Exception as err:
        print("An error occurred:", err)
    finally:
        print('File size: {}'.format(total))
        for key, value in sorted(status.items()):
            if value != 0:
                print('{}: {}'.format(key, value))

if __name__ == "__main__":
    main()
