import pathlib
file_path = 'theatres.txt'
theatres =[]
text= open(file_path)
with open(file_path, mode="r") as my_open_file:
    # recall: iterating over the file-object yields each line of the file
    # one line at a time
   # out = [line for line in my_open_file if line.startswith("theater")]
    out = my_open_file.readline()
    name=''.join(out).split(':')[1]
    print(name)


