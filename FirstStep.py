print('Hello Huu Tran')

abc = 123

print(abc)

mystring = 'abcdefghijkl'

print(mystring[-1])
print(mystring[9])


# Cách đọc cấu trúc là Start:Step:Stop

# lấy từ index 2 trở lên
print(mystring[2:])
# lấy từ index 0 đến index 2
print(mystring[:2])

#bước nhảy python tức là đi từ phần tử đầu, bỏ 1 ký tự và lấy cái tiếp theo

print(mystring[::2])

# Bỏ 2 ký tự lấy cái tiếp theo (cái thứ 3)
print(mystring[::3])

print(mystring[::3])


# start = 2 , step = 7, stop = 2  =>  bắt đầu từ index 2 , nhảy 7 bước từ index 0 là a đến index 7  rồi lấy từ 7 đi index 2 . tức là tại vị trí index 7 sẽ là 0 và lấy tiếp 2

# giải thích 2 lấy từ phần tử thứ 2 , chiều dài 7 ký index , mỗi lần cách 2 bước vd bỏ 1 bước lấy bước tiếp theo
# start = 2 , lenght = 7 , step = 2
print(mystring[2:7:2])