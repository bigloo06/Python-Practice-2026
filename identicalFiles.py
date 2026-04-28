import hashlib # hashlib is used to generate cyrptographic hashes (converts an input into a fixed string of characters)
import sys # used to take command line arguments

def hash_file(file1, file2):
    h1 = hashlib.sha1() 
    # sha1 is a cryptographic hash function that converts an input into a 160 bit 40 digit hex string

    h2 = hashlib.sha1()

    with open(file1, 'rb') as file: 
        # rb is read binary mode used mostly for reading non-text files

        chunk = 0 
        # set chunk = 0 (anything is ok as long as it isn't empty bytes) 
        # we use chunks since if the file is very big (GB or TB), this could use a lot of RAM or even crash

        while chunk != b'': 
            # we loop until we reach the end of the file, since file.read returns empty byte (b'') at the end

            chunk = file.read(1024) 
            # reads 1024 bytes (1 kb) from the file

            h1.update(chunk) 
            # puts each individual chunk into the hash object

    with open(file2, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)
    return h1.hexdigest(), h2.hexdigest()
    # hexdigest returns a hash value as a hexadecimal string

if __name__ == '__main__':
    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

        op1, op2 = hash_file(file1, file2)
        # op1 and op2 will contain the hexdigest of the two given files

        if op1 == op2:
            print('Files are identical')
        else:
            print('Files are different')
    except:
        print('Two files not given')