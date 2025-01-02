def rev(a, b):
        """
        rev(a, b)
        Changing a and b bettwen them 
        """
        return b, a
def shift_list(offset: int, list: str):
    """
    shift_list(offset, list)
    Shift given list to given offset
    """
    shifted_list = []
    for i in range(len(list)):
        new_index = (i + offset) % len(list)
        shifted_list.insert(new_index, list[i])
    return shifted_list    
def create_number(lst: str):
    """
    create_number(list)
    make from given list one number
    """
    num = ''
    for ele in lst:
        try:
            a = int(ele)
            num += str(ele)
        except:
            print("one of elements was deleted cause it is not an integer/float")
    
    return num
def sum_number(lst: str):
    """
    create_number(list)
    make from given list one number
    """
    num = 0
    for ele in lst:
        try:
            num += ele
        except:
            print("one of elements was deleted cause it is not an integer/float")
    
    return num
def inputMas(n: int, sc='\n') -> list:
    r'''
    returns an array from given numbers, 
    default splice char is "\n". You can set it using s=" "
    '''
    mas = []
    if sc=='\n':
        for i in range(n):
            mas.append(input()) 
    else:
        mas = input().split(sc)
    return mas