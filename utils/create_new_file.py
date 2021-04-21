#import os {This will be helpful for getting the file size}
def CreateNewFile(file_name,file_size_byte):
    with open(file_name, "wb") as f: 
        f.seek(file_size_byte)
        f.write(b"\0")
    #file_size = os.path.getsize(os.path.realpath(file_name)) -1 {this will return file size if needed}
    #print(file_size) {this will print the file size }

if __name__ == "__main__":
     file_name = "attempt1.txt"

     kilo_byte = 1024
     mega_byte = 1024*kilo_byte
     giga_byte = 1024 *mega_byte

     file_size_byte = 2*kilo_byte
     CreateNewFile(file_name=file_name,file_size_byte=file_size_byte)

