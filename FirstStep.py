from distutils.file_util import write_file

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

# bước nhảy python tức là đi từ phần tử đầu, bỏ 1 ký tự và lấy cái tiếp theo

print(mystring[::2])

# Bỏ 2 ký tự lấy cái tiếp theo (cái thứ 3)
print(mystring[::3])

print(mystring[::3])

# start = 2 , step = 7, stop = 2  =>  bắt đầu từ index 2 , nhảy 7 bước từ index 0 là a đến index 7  rồi lấy từ 7 đi index 2 . tức là tại vị trí index 7 sẽ là 0 và lấy tiếp 2

# giải thích 2 lấy từ phần tử thứ 2 , chiều dài 7 ký index , mỗi lần cách 2 bước vd bỏ 1 bước lấy bước tiếp theo
# start = 2 , lenght = 7 , step = 2
print(mystring[2:7:2])

print(len(mystring))

# Thêm tham số truyền vào vào chuỗi
# Phải có dấu {} thì sau đó mới truyền chuỗi Trần Bảo Hữu vào trong được
print('Xin chào {}'.format('Trần Bảo Hữu'))

# thêm nhiều lỗ 1 lúc vào vị trí 1 , 2 , 3
print('Xin chào {} {} {}'.format('fox', 'brown', 'quick'))

# thêm nhiều lỗ 1 lúc và có điều chỉnh vị trí
print('Xin chào {2} {0} {1}'.format('fox', 'brown', 'quick'))

# thêm nhiều lỗ 1 lúc và có thêm biến để lưu trữ
print('Xin chào {f} {q} {b}'.format(f='fox', b='brown', q='quick'))

# Làm tròn float number
# cấu trúc {value:width.precision f
float_number = 1.23235435345324

print('The result was: {r:1.2f}'.format(r=float_number))

# Cách truyền biến f-String cho python 3.6 trở lên

name = 'Trần Bảo Hữu'
print(f'Xin chào {name}')

print(f'The result was: {float_number:1.2f}')

# ghi file

# write_file('myfile.txt','hahahhihihi ghi file ne')


# đọc file

my_file = open('C:\\Users\VACTRHU005\Documents\GitHub\DemoPython\myfile.txt')

print(my_file.read())

# đọc lại read lần nữa sẽ trả ra rỗng
print(my_file.read())

# để sửa việc read lần 2 rỗng thì ta phải reset con trỏ đọc file về lại vị trí ban đầu
my_file.seek(0)

print(my_file.read())

my_file.close()

# read file không cần quan tâm close file

with open('C:\\Users\VACTRHU005\Documents\GitHub\DemoPython\myfile.txt') as my_new_file:
    contents = my_new_file.read()


