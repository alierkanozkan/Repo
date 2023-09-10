import hashlib

def calculate_file_sha256(file_path):
    sha256 = hashlib.sha256()
    
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            sha256.update(chunk)
    
    hash_value = sha256.hexdigest()
    return hash_value

def main():
    file_path = input("Path to file: ")
    print("Calculating SHA-256 hash value...")
    calculated_hash = calculate_file_sha256(file_path)
    print("Hash value of file: ", calculated_hash)
    user_input_hash = input("Enter SHA-256 hash value to compare: ")
    if user_input_hash == calculated_hash:
        print("Matched!")
    else:
        print("Missmatch! If all the given values correct then the file is corrupted.")

if __name__ == "__main__":
    main()
