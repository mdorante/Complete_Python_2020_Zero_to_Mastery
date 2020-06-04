import requests
import hashlib
import sys

# This script takes a password, turns it into a SHA1 hash,
# sends the first 5 charactes of the hash to the pwned passwords API and returns a list of all passwords in the API's database
# that start with the same 5 hash characters, then compares the remaining characters of the hashes
# to the remaining characters of the hash that was just created and if it has a match, it will return the number
# of times the password has been pwned, if it doesn't have a match in the list, then the password has never
# been pwned and is a nice, usable password

# NOTE: pwned = victim of a data breach


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    # NOTE: the pwnedpasswords api takes in a hash, not the actual password or it'll return a 400 error

    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check API and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, remaining = sha1_password[:5], sha1_password[5:]

    # We're requesting the pwnedpassword API for a list of password hashes that start with the first 5 characters of the hash we just created above
    response = request_api_data(first5)
    return get_password_leaks_count(response, remaining)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} has been pwned {count} times... consider another one')
        else:
            print(f'{password} has not been pwned, go ahead and use it!')


if __name__ == '__main__':
    main(sys.argv[1:])
