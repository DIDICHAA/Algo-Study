'''
문자열을 3등분, 가운데 문자열을 공백으로 바꿈
3분할 해서 2에 해당하는 부분을 계속해서 없애나가는 로직
양 옆이 대칭되고, 숫자에 따라 그냥 같은 모양이 늘어나가심...
'''

def change(n):
    if n == 1:
        return '-'

    left = change(n//3)
    center = ' ' * (n//3)
    return left + center+ left

while True:
    try:
        N = int(input())
        print(change(3**N))
        
    except:
        break