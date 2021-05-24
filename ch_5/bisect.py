from bisect import bisect_left, bisect_right

#값이 [left_value, right_value]인 데이터 개수를 반환
def count_by_range(array, left, right):
  left_index = bisect_left(array, left)
  right_index = bisect_right(array, right)
  return right_index-left_index
  #만약 x의 개수를 구하려고하는데
  #배열안에 x가 없다면 0이 반환된다.