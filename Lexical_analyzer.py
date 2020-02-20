import platform
import os

class Token:
     Types = ""
     data = 0

if(platform.system() == 'Linux'):
    clc = 'clear'
else:
    clc = 'cls'

os.system(clc)

source_code = ''

while True :

    print('.:: Choose your mode :')
    print('\t (1) :: Read file(Calculator.txt must exists)')
    print('\t (2) :: Type in Terminal')

    try:
        choose = int(input('Choose : '))
    except:
        os.system(clc)
        continue

    if (choose == 1):
        try :
            file1 = open("Calculator.txt","r+")
        except :
            file1 = open("Calculator.txt",'w')
            file1.close()
            file1 = open("Calculator.txt","r+")

        source_code = file1.read()
        os.system(clc)
        print('\t==================')
        print('\t  Read from file')
        print('\t==================\n\n')
        print(source_code)
        break
    elif (choose == 2):
        os.system(clc)
        print('\t==================')
        print('\tRead from Terminal')
        print('\t==================\n\n')
        print('\t Finish = $$')
        while True :
            rd = input()
            if(rd.find('$$') != -1):
                tmp = rd.find('$$')
                source_code = source_code + rd[0:tmp] + '\n'
                break
            else:
                source_code = source_code + rd +'\n'
    break



index = 0
state = 0
stop = 0
start = 0

#Types = ('ID','ASG','REAL','INT','LPAR','RPAR','PLUS','MINUS','SLASH','MULTIPLICATION')

Tok = []

while(index<len(source_code)):
    if(state == 0):
        if(source_code[index] == ' ' or source_code[index] == '\t' or source_code[index] == '\n'):
            state = 0
            start = index #? 
            index += 1
        elif(source_code[index].isdigit()):
            state = 1
            start = index #?
            index += 1
        elif(source_code[index].isalpha()):
            state = 3
            start = index #?
            index += 1
        elif(source_code[index] == '='):
            state = 4
            index += 1
        elif(source_code[index] == '('):
            state = 5
            index += 1
        elif(source_code[index] == ')'):
            state = 6
            index +=1
        elif(source_code[index] == '+'):
            state = 7
            index += 1
        elif(source_code[index] == '-'):
            state = 8
            index += 1
        elif(source_code[index] == '/'):
            state = 9
            index += 1
        elif(source_code[index] == '*'):
            state = 10
            index += 1
        elif(source_code[index] == '.'):
            state = 2
            index += 1
    elif(state == 1):
        if(source_code[index]== '.'):
            state = 2
            index += 1
        elif(source_code[index].isdigit()):
            state = 1
            index += 1
        elif (source_code[index].isalpha()):
            state = 11
            index += 1
        else:
            stop = index
            rd = source_code[start:stop]
            T = Token()
            T.Types = 'INT'
            T.data = int(rd)
            Tok.append(T)
            start = index - 1 #?
            stop = index - 1 #?
            state = 0

    elif(state == 2):
        if(source_code[index].isdigit()):
            state = 2
            index += 1
        elif (source_code[index].isalpha()):
            state = 11
            index += 1
        else :
            stop = index
            rd = source_code[start:stop]
            T = Token()
            T.Types = 'REAL'
            T.data = float(rd)
            Tok.append(T)
            start = index - 1 #?
            stop = index - 1 #?
            state = 0

    elif(state == 3):
        if(source_code[index].isalpha() or source_code[index].isdigit() or source_code[index] == '_'):
            state =3
            index += 1    
        else :
            stop = index
            rd = source_code[start:stop]
            T = Token()
            T.Types = 'ID'
            T.data = rd
            Tok.append(T)
            start = index - 1 #?  
            stop = index - 1 #?
            state = 0      
    elif(state == 4):
        T = Token()
        T.Types = 'ASG'
        T.data = ''
        Tok.append(T)
        start = index - 1 #?
        stop = index - 1 #?
        state = 0
    elif(state == 5):
        T = Token()
        T.Types = 'LPAR'
        T.data = ''
        Tok.append(T)
        start = index - 1 #?
        stop = index - 1 #?
        state = 0
    elif(state == 6):
        T = Token()
        T.Types = 'RPAR'
        T.data = ''
        Tok.append(T)
        start = index - 1 #?
        stop = index - 1 #?
        state = 0
    elif(state == 7):
        T = Token()
        T.Types = 'PLUS'
        T.data = ''
        Tok.append(T)
        start = index - 1 #?
        stop = index - 1 #?
        state = 0
    elif(state == 8):
        T = Token()
        T.Types = 'MINUS'
        T.data = ''
        Tok.append(T)
        start = index - 1 #?
        stop = index - 1 #?
        state = 0
    elif(state == 9):
        T = Token()
        T.Types = 'SLASH'
        T.data = ''
        Tok.append(T)
        start = index - 1 #?
        stop = index - 1 #?
        state = 0
    elif(state == 10):
        T = Token()
        T.Types = 'MULTIPLY'
        T.data = ''
        Tok.append(T)
        start = index - 1 #?
        stop = index - 1 #?
        state = 0
    elif(state == 11):
        if(source_code[index] == ' ' or source_code[index]=='\t' or source_code[index] == '\n'):
            stop = index
            rd = source_code[start:stop]
            T = Token()
            T.Types = 'INVALID ID'
            T.data = rd
            Tok.append(T)
            start = index - 1 #?  
            stop = index - 1 #?
            state = 0
        else:
            state = 11
            index += 1

## Printing : 
count = 0
print('\n')
for i in Tok:
    print(i.Types,end='(')
    print(i.data,end=') | ')

    if(count < 5):
        count+=1
    else:
        count = 0 
        print('\n')
    
print('\n')