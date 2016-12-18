from operator import itemgetter


def main():
    file = open('result.txt', 'r')
    res_file = open('sorted_file.txt', 'w')
    lines = file.readlines()
    i = 0
    result = []
    for line in lines:
        result.append(line.split(' '))
        print(result[i][2])
        result[i][2] = int(result[i][2])
        i += 1
    # print(result)
    print(sorted(result, key=itemgetter(2), reverse=True))
    sort_result = sorted(result, key=itemgetter(2), reverse=True)
    res_file.write(''.join(str(x) for v in sort_result for x in v))
    file.close()
    res_file.close()


main()
