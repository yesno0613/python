selected = None
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에서 선택하세요> ')
print('선택한 값은:', selected)



# selected = None
# com_selected = '가위'
# while selected not in ['가위', '바위', '보']:
#     selected = input('가위, 바위, 보 중에서 선택하세요> ')
#     if(selected == '가위' or selected == '바위'or selected== '보'):
#         if (selected == '바위'):
#             selected=="selected"
#             print('u win')
#         else:
#             selected = None
#             print('이길때까지 무한 반복')
#     else:
#         print('가위 바위 보 중에서 하나만 선택 하세요')


# #어떤수를 입력받아 그 수까지의 합을 구한다.
# n = int(input('수를 입력하세요'))
# a = 0
# for i in range(1, n+1):
#     a += i
# print('1부터',n, '까지의 합은' ,a)
# print('1부터 {} 까지의 합은 {}'.format(n, a))
# print(f'1부터 {n} 까지의 합은 {a}' )    
