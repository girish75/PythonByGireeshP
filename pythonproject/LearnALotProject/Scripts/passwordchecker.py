import sys

import requests
import hashlib


def return_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    hashobj = requests.get( url )
    # print(hashobj)
    if hashobj.status_code != 200:
        raise RuntimeError( f'Error fetching: {hashobj.status_code} check the API and try again' )
    return hashobj


def read_response(all_hash):
    print( all_hash.text )


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split( ':' ) for line in hashes.text.splitlines())

    for hashtail, count in hashes:
        # print(hashtail, count )
        if hashtail == hash_to_check:
            return count
    return 0

def pawned_api_check(password):
    # print(password.encode('utf-8'))
    # print(hashlib.sha1(password.encode('utf-8')))
    # print( hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_Char, tail = sha1password[:5], sha1password[5:]
    # print(first5_Char, "Next is remaining :", tail)
    all_hash = return_api_data( first5_Char)
    #read_response(all_hash)
    return get_password_leaks_count(all_hash,tail)


def main(args):
    for password in args:
        count = pawned_api_check(password)
        if count:
            print(f'{password} was found {count} times ... you should change your password')
        else:
            print(f'{password} was Not breached: Carry on!!')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))





