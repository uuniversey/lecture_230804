

# # T = 10
# # for tc in range(1, T+1):
# #     N = int(input())
# arr = [list(map(int,input().split())) for _ in range(100)]
#
# for col in range(100):
#     if arr[99][col] == 2:                 # x(2)를 찾고 x에서의 idx값을 설정.
#         idx = col
#         start_point = 0
#         break
#
# for row in range(99, -1, -1):
#     print(row, idx)
#     if row == 0:
#         start_point = idx
#
#     elif idx-1 < 0 or idx+1 > 99:
#         if idx-1 < 0:
#             while arr[row-1][idx+1] == 0:
#                 idx += 1
#             idx += 1
#
#         elif idx+1 > 99:
#             while arr[row-1][idx-1] == 0:
#                 idx -= 1
#             idx -= 1
#
#     elif arr[row][idx-1] == 1:
#         if idx-1 == 0:
#             idx = 0
#         else:
#             while arr[row-1][idx-1] == 0:
#                 idx -= 1
#             idx -= 1
#
#     elif arr[row][idx+1] == 1:
#         if idx+1 == 99:
#             idx = 99
#         else:
#             while arr[row-1][idx+1] == 0:
#                 idx += 1
#             idx += 1
#
#     else:
#         continue
#
# print(f'#{9} {start_point}')