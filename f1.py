def convert_string_to_number(str):
    x=int(str)
    return x

def find_min(arr):
    currmin=arr[0]
    i=1
    while i<len(arr):
        if arr[i]<currmin:
            currmin=arr[i]
        i=i+1
    return currmin

def print_list(arr):
    i=0
    while i<len(arr):
        print(arr[i], end=" ")
        i+=1
    print()

def print_dict(dic):
    for i in dic:
        print(f'"{i}" {dic[i]}', end=" ")

def get_str_len(str):
    return len(str)

def remove_outer_characters(str):
    i=1
    txt=""
    while i < len(str)-1:
        txt=txt+str[i]
        i+=1
    return txt

def count_chars(str):
    i=0
    dic={}
    while i<len(str):
        if not str[i] in dic:
            dic.setdefault(str[i],str.count(str[i]))
        i+=1
    return dic