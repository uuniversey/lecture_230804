

# 1945. 간단한 소인수분해

# import sys
# sys.stdin = open('input_1945.txt', 'r')
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     a = 0
#     b = 0
#     c = 0
#     d = 0
#     e = 0
#
#     while N % 2 == 0:
#         N //= 2
#         a += 1
#
#     while N % 3 == 0:
#         N //= 3
#         b += 1
#
#     while N % 5 == 0:
#         N //= 5
#         c += 1
#
#     while N % 7 == 0:
#         N //= 7
#         d += 1
#
#     while N % 11 == 0:
#         N //= 11
#         e += 1
#
#     print (f'#{tc} {a} {b} {c} {d} {e}')



# 5789. 현주의 상자 바꾸기

# import sys
# sys.stdin = open('input_5789.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, Q = map(int,input().split())
#     my_box = [0] * N
#     for case in range(1, Q+1):
#         i, R = map(int,input().split())
#         for num in range(i-1, R):
#             my_box[num] = case
#
#     print(f'#{tc}', *my_box)



# 6019. 기차 사이의 파리

# import sys
# sys.stdin = open('input_6019.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = list(map(int,input().split()))
#     distance = arr[0]
#     A_velo = arr[1]
#     B_velo = arr[2]
#     F_velo = arr[3]
#     fly_filght = 0


    # print(f'#{tc} {fly_filght}')

############# 시간으로 했더니 못하겠음 거리로 해야할듯?


# 9490. 풍선팡

# import sys
# sys.stdin = open('input_9490.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     max_v = 0
#     sum_v = 0
#     for row in range(N):
#         for col in range(M):
#             select = arr[row][col]
#             sum_v = select
#             for num in range(1,select+1):
#                 for di, dj in [[0,num], [num,0], [0,-num], [-num,0]]:
#                     if 0 <= row+di < N and 0 <= col+dj < M:
#                         sum_v += arr[row+di][col+dj]
#
#             if max_v < sum_v:
#                 max_v = sum_v
#
#     print(f'#{tc} {max_v}')



# 16910. 원 안의 점

# import sys
# sys.stdin = open('input_16910.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     point_num = 0
#
#     for row in range(N):
#         for col in range(N):
#             if row**2 + col**2 <= N**2:
#                 point_num += 1
#
#     result = (point_num - N) * 4 + 5        # + 5를 하는 이유 : 0,0 과 좌표 가장자리 4점이 빠져서
#     print(f'#{tc} {result}')



# 6485. 삼성시의 버스 노선

# import sys
# sys.stdin = open('input_6485.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     box = [0] * 5001
#
#     for i in range(N):
#         A, B = map(int,input().split())
#         for k in range(A, B+1):
#             box[k-1] += 1
#
#     P = int(input())
#     station = [0] * P
#     for j in range(P):
#         C = int(input())
#         station[j] = box[C-1]
#
#     print(f'#{tc}', *station)

#     # station = [str(a) for a in station]
#     # ans = ' '.join(station)
