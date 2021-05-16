#import os {This will be helpful for getting the file size}
KB_conv_bytes = 2**10
MB_conv_bytes = 2**20
GB_conv_bytes = 2**30


def create_random_file(file_name: str, GB=0, MB=0, KB=0, Bytes=0):
    file_size_byte = GB*GB_conv_bytes + MB*MB_conv_bytes + KB*KB_conv_bytes + Bytes
    with open('data/original/'+file_name, "wb") as f: 
        f.seek(file_size_byte)
        f.write(b"\0")
        print(f"File Created Successfully of size: {file_size_byte} bytes")
    #file_size = os.path.getsize(os.path.realpath(file_name)) -1 {this will return file size if needed}
    #print(file_size) {this will print the file size }

if __name__ == "__main__":
     file_name = "attempt1.txt"

     create_random_file(file_name=file_name, GB=1)

