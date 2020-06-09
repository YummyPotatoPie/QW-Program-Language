import KEY_WORDS as KW
import REGISTERS as RG

def CODE_LINES(FILE_PATH: str): #Построчный анализ
    LINES = []
    CODE = open(FILE_PATH, 'r')
    for line in CODE:
        if line == '\n':
            continue
        else:
            LINES.append(line)
    return LINES

def FILE_CHECK(FILE_PATH: str):
    try:
        CODE = open(FILE_PATH, 'r')
        return True
    except FileNotFoundError:
        return False

def CHECK(FILE_PATH: str): #Проверка расширения файла
    FILE_PATH += ' '
    if FILE_PATH[-5:-1] != '.qwl':
        return False
    return True

def LINES_TOKENS(LINE: str): #Создание токенов строк
    TOKENS = []
    LINE_TOKENS = []
    CODE = ''
    for i in range(len(LINE)):
        if LINE[i] == ' ':
            LINE_TOKENS.append(CODE)
            CODE = ''
        elif LINE[i] == ',' or LINE[i] == ';':
            LINE_TOKENS.append(CODE)
            LINE_TOKENS.append(LINE[i])
            CODE = ''
        elif (CODE in KW.KEY_WORDS) or (CODE in KW.REGISTERS):
            LINE_TOKENS.append(CODE)
            CODE = ''
        else:
            CODE += LINE[i]
    for i in range(len(LINE_TOKENS)):
        if LINE_TOKENS[i] == '':
            continue
        else:
            TOKENS.append(LINE_TOKENS[i])
    if TOKENS[-1] != ';':
        return 'ERROR: Invalid Syntax.'
    return TOKENS

def NUMBERS_ANALYSYS(TOKEN: str): #Функция проверки на число
    if TOKEN.isdigit():
        return True
    else:
        try:
            float(TOKEN)
            return True
        except ValueError:
            return False

def COMMAND_FUNC(COMMAND_TOKEN: list): #Функция проверки объявления процедур 
    if len(COMMAND_TOKEN) > 3:
        if COMMAND_TOKEN[2] == ',':
            if COMMAND_TOKEN[4] == '->':
                for i in range(len(RG.FUNC_REGISTERS_LINK)):
                    if COMMAND_TOKEN[1] == RG.FUNC_REGISTERS_LINK[i]:
                        RG.FUNC_REGISTERS[i] = COMMAND_TOKEN[-5:-1]
                        RG.FUNC_REGISTERS[i].append(';')
                        return '0'
                return 'ERROR: Invalid Register.'
            return 'ERROR: Invalid Syntax.'
        return 'ERROR: Invalid Syntax.'
    else:
        for i in range(len(RG.FUNC_REGISTERS_LINK)):
            if COMMAND_TOKEN[1] == RG.FUNC_REGISTERS_LINK[i]:
                RG.FUNC_REGISTERS[i]
                CODE_WORK(RG.FUNC_REGISTERS[i])
                return '0'
        return 'ERROR: Invalid Register.'
    return 'ERROR: Invalid Syntax.'

def COMMAND_SUM(COMMAND_TOKEN: list): #Функция проверки суммирования
    if COMMAND_TOKEN[2] == ',':
        for i in range(len(RG.DATA_REGISTERS_LINK)):
            if COMMAND_TOKEN[1] == RG.DATA_REGISTERS_LINK[i]:
                if NUMBERS_ANALYSYS(COMMAND_TOKEN[3]) and NUMBERS_ANALYSYS(str(RG.DATA_REGISTERS[i])):
                    RG.DATA_REGISTERS[i] = float(RG.DATA_REGISTERS[i]) + float(COMMAND_TOKEN[3])
                    return '0'
                else:
                    return 'ERROR: Invalid Types.'
        return 'ERROR: Invalid Register.'
    return 'ERROR: Invalid Syntax.'

def COMMAND_PROD(COMMAND_TOKEN: list): #Функция проверки умножения
    if COMMAND_TOKEN[2] == ',':
        for i in range(len(RG.DATA_REGISTERS_LINK)):
            if COMMAND_TOKEN[1] == RG.DATA_REGISTERS_LINK[i]:
                if NUMBERS_ANALYSYS(COMMAND_TOKEN[3]) and NUMBERS_ANALYSYS(str(RG.DATA_REGISTERS[i])):
                    RG.DATA_REGISTERS[i] = float(RG.DATA_REGISTERS[i]) * float(COMMAND_TOKEN[3])
                    return '0'
                else:
                    return 'ERROR: Invalid Types.'
        return 'ERROR: Invalid Register.'
    return 'ERROR: Invalid Syntax.'

def COMMAND_DIV(COMMAND_TOKEN: list): #Функция проверки деления
    if COMMAND_TOKEN[2] == ',':
        for i in range(len(RG.DATA_REGISTERS_LINK)):
            if COMMAND_TOKEN[1] == RG.DATA_REGISTERS_LINK[i]:
                if NUMBERS_ANALYSYS(COMMAND_TOKEN[3]) and NUMBERS_ANALYSYS(str(RG.DATA_REGISTERS[i])):
                    if float(COMMAND_TOKEN[3]) != 0.0:
                        RG.DATA_REGISTERS[i] = float(RG.DATA_REGISTERS[i]) / float(COMMAND_TOKEN[3])
                        return '0'
                    else:
                        return 'ERROR: Division By Zero.'
                else:
                    return 'ERROR: Invalid Types.'
        return 'ERROR: Invalid Register.'
    return 'ERROR: Invalid Syntax.'

def COMMAND_POW(COMMAND_TOKEN: list): #Функция проверки возведения в степень
    if COMMAND_TOKEN[2] == ',':
        for i in range(len(RG.DATA_REGISTERS_LINK)):
            if COMMAND_TOKEN[1] == RG.DATA_REGISTERS_LINK[i]:
                if NUMBERS_ANALYSYS(COMMAND_TOKEN[3]) and NUMBERS_ANALYSYS(str(RG.DATA_REGISTERS[i])):
                    RG.DATA_REGISTERS[i] = float(RG.DATA_REGISTERS[i]) ** float(COMMAND_TOKEN[3])
                    return '0'
                else:
                    return 'ERROR: Invalid Types.'
        return 'ERROR: Invalid Register.'
    return 'ERROR: Invalid Syntax.'

def COMMAND_PUT(COMMAND_TOKEN: list): #Функция проверки ввода
    if COMMAND_TOKEN[2] == ',':
        for i in range(len(RG.DATA_REGISTERS_LINK)):
            if COMMAND_TOKEN[1] == RG.DATA_REGISTERS_LINK[i]:
                if NUMBERS_ANALYSYS(COMMAND_TOKEN[3]) and NUMBERS_ANALYSYS(str(RG.DATA_REGISTERS[i])):
                    RG.DATA_REGISTERS[i] = float(COMMAND_TOKEN[3])
                    return '0'
                else:
                    if (COMMAND_TOKEN[3][0] == "'" and COMMAND_TOKEN[3][-1] == "'") or (COMMAND_TOKEN[3][0] == '"' and COMMAND_TOKEN[3][-1] == "'"):
                        RG.DATA_REGISTERS[i] = COMMAND_TOKEN[3]
                        return '0'
                    else:
                        return 'ERROR: Invalid Types.'
        return 'ERROR: Invalid Register.'
    return 'ERROR: Invalid Syntax.'

def COMMAND_OUT(COMMAND_TOKEN: list): #Функция проверки вывода
    for i in range(len(RG.DATA_REGISTERS_LINK)):
        if COMMAND_TOKEN[1] == RG.DATA_REGISTERS_LINK[i]:
            print(RG.DATA_REGISTERS[i])
            return '0'
    return 'ERROR: Invalid Register.'
    
def CODE_WORK(COMMAND_TOKEN: list): #Функция определения команды
    if COMMAND_TOKEN[0] == 'prod':
        COMM_END = COMMAND_PROD(COMMAND_TOKEN)
        return COMM_END
    elif COMMAND_TOKEN[0] == 'div':
        COMM_END = COMMAND_DIV(COMMAND_TOKEN)
        return COMM_END
    elif COMMAND_TOKEN[0] == 'sum':
        COMM_END = COMMAND_SUM(COMMAND_TOKEN)
        return COMM_END
    elif COMMAND_TOKEN[0] == 'pow':
        COMM_END = COMMAND_POW(COMMAND_TOKEN)
        return COMM_END
    elif COMMAND_TOKEN[0] == 'out':
        COMM_END = COMMAND_OUT(COMMAND_TOKEN)
        return COMM_END
    elif COMMAND_TOKEN[0] == 'put':
        COMM_END = COMMAND_PUT(COMMAND_TOKEN)
        return COMM_END
    elif COMMAND_TOKEN[0] == 'func':
        COMM_END = COMMAND_FUNC(COMMAND_TOKEN)
        return COMM_END
    else:
        return 'ERROR: Invalid Syntax.'

def MAIN_DEF():
    Key = ''
    print('Enter file path: ', end="")
    FILE_PATH = str(input())
    while True:
        if CHECK(FILE_PATH):
            if FILE_CHECK(FILE_PATH):
                PRE_TOKEN = CODE_LINES(FILE_PATH)
                for i in range(len(PRE_TOKEN)):
                    TOKENS = LINES_TOKENS(PRE_TOKEN[i])
                    if TOKENS != 'ERROR: Invalid Syntax.':
                        CODE = CODE_WORK(TOKENS) 
                        if CODE not in KW.ERRORS:
                            continue
                        else:
                            print(str(CODE) + ' Line: ' + str(i + 1))
                            break
                    else:
                        print('ERROR: Invalid Syntax.' + ' Line: ' + str(i + 1))
                        break
            else:
                print('ERROR: File Not Found')
        else:
            print('ERROR: Invalid Path Or File')
        print("To exit enter 'quit', to continue enter any key: ", end="")
        Key = str(input())
        if Key != 'quit':
            print('Enter file path: ', end="")
            FILE_PATH = str(input()) 
            continue
        else:
            break
