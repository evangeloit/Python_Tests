# File objects

# context manager
from __future__ import  print_function # Python 3.x print function for using end=' '

# with open('test.txt','r') as f:

    # size_to_read = 100
    # for line in f:
    #     print(line)


    # f_contents = f.read(size_to_read)
    # f_contents = f.readlines()
    # f_contents = f.readline()
    # print(f_contents)

    # f_contents = f.readline()
    # print(f_contents)

# f = open('test.txt', 'r') #  explicit reading / writing / appending
#
# print(f.name) # mode
#
# f.close()

# Open the file with context manager/ Automatically closes file ..clean up


# with open('test.txt','r') as f:
#
#     size_to_read = 10
#
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')
#
#     f.seek(0) # Set the position at the beginning of the file
#
#     f_contents = f.read(size_to_read)
#     print(f_contents)
##///////////////////////////////////////////////////////////////////////
    # print(f.tell()) # 10th char of the file

    # while len(f_contents) > 0:
    #     print(f_contents, end='*') # Every 10 chars puts a */ it advances its position everytime when we read
    #     f_contents = f.read(size_to_read)


# Write ...

# with open('test2.txt','w') as f: # if the file doesn't exist it will be created/ if it exist it will overwrite it !
#     f.write('Test')
#
#     f.seek(0) # Second test overwrote the second
#
#     # f.write('Test')
#     f.write('R')

# Test Code for reading from a file and write to a copy

# with open('test.txt','r') as rf: #reading our original file
#     with open('test_copy.txt', 'w') as wf: # writing to our copy
#         for line in rf:
#             wf.write(line)

# Test Code for reading an image file

# with open('galloping knights.jpg','rb') as rf: #reading our original file b = binary
#     with open('galloping knights_copy.jpg', 'wb') as wf: # writing to our copy
#         for line in rf:
#             wf.write(line)

# read in chunk size

with open('galloping knights.jpg','rb') as rf: #reading our original file b = binary
    with open('galloping knights_copy.jpg', 'wb') as wf: # writing to our copy
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0 :
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


