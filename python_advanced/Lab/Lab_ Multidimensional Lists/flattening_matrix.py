#01. Comprehension method
#---------------------------------------------------------------------
# rows = int(input())
# matrix = [[int(j) for j in input().split(', ')]for i in range(rows)]
# result = [item for sublist in matrix for item in sublist]
# print(result)


#02. For method
#---------------------------------------------------------------------
# rows = int(input())
# matrix = [[int(j) for j in input().split(', ')]for i in range(rows)]
#
# result = []
#
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         result.append(matrix[row_index][col_index])
#
# print(result)

#03. Extend method

rows = int(input())
result = []

for _ in range(rows):
    nums = [int(n) for n in input().split(', ')]
    result.extend(nums)

print(result)