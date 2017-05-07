def BoilerPlate():
    title = [' ','BIBLE', ' ', 'by:',' ', 'Tommy H. Yeargin, Jr.',' ']
    length = len(max(title, key=len)) + 6
    print(length * '*')
    for i in range(0, len(title),1):
        print('*' + (((length - len(title[i]) - 2) / 2) * ' ') + str(title[i]) + (((length - len(title[i]) - 2) / 2) * ' ') + '*')
    print(length * '*')
