def main():
    lst = list(map(int, input().split()))
    if lst[0] % 2 == 0:
        if len([x for x in lst if x % 2 == 0]) == 3: print('WIN')
        else: print('FAIL')
    else:
        if len([x for x in lst if x % 2 != 0]) == 3: print('WIN')
        else: print('FAIL')

if __name__ == '__main__':
    main()