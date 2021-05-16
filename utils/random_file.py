import os
KB_conv_bytes = 2**10
MB_conv_bytes = 2**20
GB_conv_bytes = 2**30
ORIGINAL_FILE_BASE_PATH = "data/original/"


def create_random_file(file_base_name: str, GB=0, MB=0, KB=0, Bytes=0):
    file_size_byte = GB*GB_conv_bytes + MB*MB_conv_bytes + KB*KB_conv_bytes + Bytes

    base_name, extension = os.path.splitext(file_base_name)

    file_size = [GB, MB, KB, Bytes]
    file_size_name = ["GB", "MB", "KB", "Bytes"]
    size_suffix = ""
    for i in range(len(file_size)):
        if file_size[i]:
            size_suffix = size_suffix + "_" + f"{file_size[i]}{file_size_name[i]}"

    print(size_suffix)
    print(base_name+size_suffix+extension)
    print(ORIGINAL_FILE_BASE_PATH+base_name+size_suffix+extension)

    with open(ORIGINAL_FILE_BASE_PATH+base_name+size_suffix+extension, "wb") as f:
        f.seek(file_size_byte)
        f.write(b"\0")
    print(f"File Created Successfully of size: {size_suffix.replace('_', ' ').strip()}")


if __name__ == "__main__":
    file_base_name = "random_file.txt"
    create_random_file(file_base_name=file_base_name, KB=100)

