def sum_nums(*args):
    data = 0
    for i in args:
        data += i
    data_mean = data / len(args)
    return data , data_mean
a , b = sum_nums(10 , 20 , 30)
print(f'합은 : {a} , 평균은 {b}')
a , b = sum_nums(10 , 20 , 30 , 40 , 50)
print(f'합은 : {a} , 평균은 {b}')








# def sum_nums(*number):
#     result = 0
#     for n in number:
#         result +=n
#         result 
#     return result
# print(sum_nums(10,20,30))
