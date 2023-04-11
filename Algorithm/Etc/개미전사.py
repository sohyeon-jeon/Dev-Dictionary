'''
문제 설명

개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 합니다. 메뚜기 마을에는 여러 개의 식량창고가 있는데 식량창고는 일직선으로 이어져 있습니다.

각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는 선택적으로 약탈하여 식량을 빼앗을 예정입니다. 이때 메뚜기 정찰병들은 일지선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있습니다.

따라서 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 합니다.

예시)



이때 개미 전사는 두 번째 식량창고와 네 번째 식량창고를 선택했을 때 최댓값인 총 8개의 식량을 빼앗을 수 있습니다. 개미 전사는 식량창고가 이렇게 일직선상일 때 최대한 많은 식량을 얻기를 윈합니다.

개미전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오.


입력 조건

첫째 줄에 식량창고의 개수 N이 주어집니다. (3≤N≤100)
둘째 줄에 공백을 기준으로 각 식량창고에 저장된 식량의 개수 K가 주어집니다. (0≤K≤1,000)

출력 조건

첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하세요.

입력 예시 및 출력

입력 예시:
4
1 3 1 5
출력 예시:
8
'''
n=int(input())
array=list(map(int,input().split()))
d=[0]*100

# 한 칸 띄워서 식량 창고 털기
d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])
print(d[n-1])