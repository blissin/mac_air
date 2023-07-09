from re import L


def test(a,b):
    return a+b

# print(test(b=1,a=3))

# def add_many(*args):
#     result=0
#     for i in args:
#         result = result + i
#     return result

# result=add_many(1,2,3,4,5)
# print(result)

# def print_kwargs(**kwargs):
#     print(kwargs)
# print_kwargs(b=1)

def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man=="사나이": 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("현주",30,1)