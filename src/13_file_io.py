"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
import os
import sys
# YOUR CODE HERE

text_file = open(os.path.join(sys.path[0], "foo.txt"), "r")
content = text_file.read()
print(content)
text_file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
new_file = open("bar.txt", "w")
new_file.write("Line 1 \nLine 2 \nLine 3")
new_file.close()

new_file = open("bar.txt", "r")
new_file_content = new_file.read()
print(new_file_content)
new_file.close()
