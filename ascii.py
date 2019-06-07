#draw a triangle
row = 0
column = 0
row_count = 20
row_count2 = row_count * 2
column_count = 2
row_char = " "
column_char = "^"

while row < row_count:
    row += 2
    print(row_char * (int(row_count-row)) + column_char * (row*2) + row_char * int(row_count-row))



# Drawing a flag

stripe_char = ""
star_char = ""
flag_size = 50
row = 0
iterations = 4
while row < iterations:
    row +=1 # = row+1
    print ("* " * 10 + ("~" * 39))
    print ("* " * 10 + (" " * 39))
print ("* " * 10 + ("~" * 39))
for stripe in range(1,6):
    print (" " * 59)
    print ("~" * 59)



#draw a grid
row = 0
column = 0
row_count = 10
column_count = 10
row_char = "*"
column_char = "+"

while row < row_count:
    row += 1
    print(f"{row_char}{column_char}" * column_count)
