import os

class TXL:
    def __init__(self):
        try:
            file_type = dict()
            os.chdir(r'C:\Users\asdas\Desktop\TXL')
            current_work_dir = os.getcwd()
            all_file = os.listdir(current_work_dir)
            for each_file in all_file:
                ext = os.path.splitext(each_file)[1]
                file_type.setdefault(ext, 0)
                file_type[ext] += 1
            self.TXLnum = file_type['.txt']
        except KeyError:
            self.TXLnum = 0

    def showTXL(self):
        if self.TXLnum == 0:
            print('no TXL')
        else:
            path ='C:\\Users\\asdas\\Desktop\\TXL'
            for filename in os.listdir(path):
                print(os.path.join(path, filename))
        os.system('pause')
        os.system('cls')

    def addTXL(self):
        nTXLnum = self.TXLnum + 1
        full_path = 'C:\\Users\\asdas\\Desktop\\TXL\\' + "TXL0" + str(nTXLnum) + '.txt'
        with open(full_path, 'w') as newfull:
            print('here is ' + str(nTXLnum) + ' TXL now')
        self.TXLnum += 1
        os.system('pause')
        os.system('cls')

    def delTXL(self):
        if self.TXLnum == 0:
            print('no TXL')
        else:
            i = 1
            while i:
                try:
                    j = 0
                    j = int(input('please choose one from "1" to "' + str(self.TXLnum) + '": '))
                    if j >= 1 and j <= (self.TXLnum + 1):
                        titTXL = 'C:\\Users\\asdas\\Desktop\\TXL\\TXL0'
                        endTXL = '.txt'
                        remTXL = titTXL + str(j) + endTXL
                        os.remove(remTXL)
                        for k in range(j+1, self.TXLnum+1):
                            src = titTXL + str(k) + endTXL
                            dst = titTXL + str(k-1) + endTXL
                            os.rename(src, dst)
                    else:
                        k = 1/0
                except ZeroDivisionError:
                    print('sorry,please choose one from "1" to "' + str(self.TXLnum) + '"')
                except TypeError:
                    print('sorry,please enter an int date ')
                else:
                    i = 0
            self.TXLnum -= 1
            print('delete success')
        os.system('pause')
        os.system('cls')

    def delallTXL(self):
        if self.TXLnum == 0:
            print('no TXL')
        else:
            print('delete all TXL?')
            i = 1
            while i:
                try:
                    j = int(input('YES:1\nNO:0\n'))
                    if j == 1:
                        for k in range(1, self.TXLnum+1):
                            titTXL = 'C:\\Users\\asdas\\Desktop\\TXL\\TXL0'
                            endTXL = '.txt'
                            remTXL = titTXL + str(k) + endTXL
                            os.remove(remTXL)
                        self.TXLnum = 0
                        print('YES YES YES YES YES')
                    elif j == 0:
                        print('NO NO NO NO NO NO')
                    else:
                        k =1/0
                except ZeroDivisionError:
                    print('sorry,please choose one of "1"and"0"\n')
                else:
                    i = 0
        os.system('pause')
        os.system('cls')

    def addLXR(self):
        if self.TXLnum == 0:
            print('no TXL')
        else:
            Temaddlist = ''
            k = 0
            i = 1
            while i:
                try:
                    k = int(input('please choose one TXL from "1" to "' + str(self.TXLnum) + '": '))
                    if k >= 1 and k <= (self.TXLnum + 1):
                        print('add LXR in ' + str(k) + ' TXL')
                    else:
                        n = 1 / 0
                except ZeroDivisionError:
                    print('sorry,please choose one from "1" to "' + str(self.TXLnum) + '"')
                except TypeError:
                    print('sorry,please enter an int date ')
                else:
                    i = 0
            Temaddname = input('please enter the name: ')
            Temaddlist += Temaddname + '  '

            while i == 0:
                try:
                    Temaddage = input('please enter the age: ')
                    Temaddage = int(Temaddage)
                except ValueError:
                    print('sorry,please enter an int date')
                else:
                    Temaddlist += str(Temaddage) + '  '
                    i = 1
            while i:
                try:
                    Temaddsex = int(input('\t1.man\n\t2.woman\n\t3.robot\nplease select an option: '))
                    if Temaddsex == 1:
                        Temaddlist += 'man  '
                    elif Temaddsex == 2:
                        Temaddlist += 'woman  '
                    elif Temaddsex == 3:
                        Temaddlist += 'robot  '
                    else:
                        j = 1 / 0
                except ZeroDivisionError:
                    print('sorry,please choose one of "1" , "2" and "3"\n')
                else:
                    i = 0
            while i == 0:
                try:
                    Temaddnum = input('please enter the number: ')
                    Temaddnum = int(Temaddnum)
                except ValueError:
                    print('sorry,please enter an int date')
                else:
                    Temaddlist += str(Temaddnum) + '\n'
                    i = 1
            print('\nTXL ' + str(k) + ':')
            print(Temaddlist)
            while i:
                try:
                    j = int(input('YES:1\nNO:0\n'))
                    if j == 1:
                        titTXL = 'C:\\Users\\asdas\\Desktop\\TXL\\TXL0'
                        endTXL = '.txt'
                        addLXRTXL = titTXL + str(k) + endTXL
                        with open(addLXRTXL, 'a') as aLT:
                            aLT.write(Temaddlist)
                        print('YES YES YES YES YES')
                    elif j == 0:
                        print('NO NO NO NO NO NO')
                    else:
                        k =1/0
                except ZeroDivisionError:
                    print('sorry,please choose one of "1"and"0"\n')
                else:
                    i = 0
        os.system('pause')
        os.system('cls')

    def showLXR(self):
        if self.TXLnum == 0:
            print('no TXL')
        else:
            i = 1
            while i:
                try:
                    k = int(input('please choose one TXL from "1" to "' + str(self.TXLnum) + '": '))
                    if k >= 1 and k <= (self.TXLnum + 1):
                        titTXL = 'C:\\Users\\asdas\\Desktop\\TXL\\TXL0'
                        endTXL = '.txt'
                        showLXRTXL = titTXL + str(k) + endTXL
                        print('\n\nTXL ' + str(k) + ':')
                        with open(showLXRTXL, 'r') as sLT:
                            for line in sLT:
                                print(line.strip())
                    else:
                        n = 1 / 0
                except ZeroDivisionError:
                    print('sorry,please choose one from "1" to "' + str(self.TXLnum) + '"')
                except TypeError:
                    print('sorry,please enter an int date ')
                else:
                    i = 0
        os.system('pause')
        os.system('cls')

    def delLXR(self):
        if self.TXLnum == 0:
            print('no TXL')
        else:
            k = 0
            m = 1
            while m:
                try:
                    k = int(input('please choose one TXL from "1" to "' + str(self.TXLnum) + '": '))
                    if k >= 1 and k <= (self.TXLnum + 1):
                        titTXL = 'C:\\Users\\asdas\\Desktop\\TXL\\TXL0'
                        endTXL = '.txt'
                        delLXRTXL = titTXL + str(k) + endTXL
                        zLT = {}
                        i = 1
                        with open(delLXRTXL, 'r') as dLT:
                            for line in dLT:
                                zLT[str(i)] = line.strip()
                                i += 1
                        print('\n\n' + 'TXL ' + str(k))
                        for j in range(1,i):
                            print(zLT[str(j)])
                        a = 1
                        while a:
                            try:
                                b = int(input('choose a LXR from "1" to "' + str(i-1) + '": '))
                                if b >= 1 and b <= i:
                                    del zLT[str(b)]
                                    for q in range(b+1, i):
                                        zLT[str(q-1)] = zLT[str(q)]
                                    zLT[str(i)] = ''
                                    i -= 1
                                    Temdellist = ''
                                    for q in range(1, i):
                                        Temdellist += zLT[str(q)] + '\n'
                                    with open(delLXRTXL, 'w') as dLT:
                                        dLT.write(Temdellist)
                                    print('delete success')
                                else:
                                    c = 1 / 0
                            except ZeroDivisionError:
                                print('sorry,choose a LXR from "1" to "' + str(i) + '": ')
                            else:
                                a = 0
                    else:
                        n = 1 / 0
                except ZeroDivisionError:
                    print('sorry,please choose one from "1" to "' + str(self.TXLnum) + '"')
                except ValueError:
                    print('sorry,please enter an int date ')
                else:
                    m = 0
        os.system('pause')
        os.system('cls')

    def delallLXR(self):
        if self.TXLnum == 0:
            print('no TXL')
        else:
            i = 1
            while i:
                try:
                    k = int(input('please choose one TXL from "1" to "' + str(self.TXLnum) + '": '))
                    if k >= 1 and k <= (self.TXLnum + 1):
                        titTXL = 'C:\\Users\\asdas\\Desktop\\TXL\\TXL0'
                        endTXL = '.txt'
                        deladdLXRTXL = titTXL + str(k) + endTXL
                        print('delete all LXR of TXL ' + str(k) + ': ')
                        a = input('YES:1\n')
                        if a == '1':
                            with open(deladdLXRTXL, 'w') as daLT:
                                daLT.write('')
                            print("OK")
                        else:
                            print('NO')
                    else:
                        n = 1 / 0
                except ZeroDivisionError:
                    print('sorry,please choose one from "1" to "' + str(self.TXLnum) + '"')
                except TypeError:
                    print('sorry,please enter an int date ')
                else:
                    i = 0
        os.system('pause')
        os.system('cls')

def startJM():
    print('0.out')
    print('1.show all TXL')
    print('2.add a new TXL')
    print('3.add a new LXR')
    print('4.del a TXL')
    print('5.del all TXL')
    print('6.show all LXR')
    print('7.del a LXR')
    print('8.del all LXR')


STXL = TXL()
i = 1
while i:
    startJM()
    j = 1
    while j:
        try:
            n = int(input())
        except ValueError:
            print('sorry,please enter an int date')
        else:
            j = 0
    if n == 1:
        STXL.showTXL()
    elif n == 2:
        STXL.addTXL()
    elif n == 3:
        STXL.addLXR()
    elif n == 4:
        STXL.delTXL()
    elif n == 5:
        STXL.delallTXL()
    elif n == 6:
        STXL.showLXR()
    elif n == 7:
        STXL.delLXR()
    elif n == 8:
        STXL.delallLXR()
    elif n == 0:
        i = 0