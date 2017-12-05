import string
import random
import hashlib
from colorama import Fore, Back
import os

green = Fore.GREEN
cyan = Fore.CYAN
white = Fore.WHITE
yellow = Fore.YELLOW
black = Back.BLACK

hashes = []
example_challenge = '9Kzs52jSfxjGJ54Sfjz5gZ1lls'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def header():
    print(yellow + '**************************************************************************')
    print(yellow + '****************************Nonce Finder**********************************')
    print(yellow + '**************************************************************************')

def generation(challenge=example_challenge, size=25):
    nonce = ''.join(random.choice(string.ascii_lowercase +
                                   string.ascii_uppercase +
                                   string.digits)for x in range(size))
    attempt = challenge+nonce
    return attempt, nonce

shaHash = hashlib.sha256()

def testAttempt():
    attempt, nonce = generation()
    shaHash.update(attempt.encode('utf-8'))
    solution = shaHash.hexdigest()
    with open('storage', mode='a') as f:
        f.write(solution + '\n')
    f.close()

    #Does not preclude the scenario of more than 3 zeros
    #Use RegEx instead
    if solution.startswith('000'):
        hashes.append(solution)
        with open('nonces', mode='a') as f:
            f.write(hashes[len(hashes) - 1] + '\n')
        f.close()
        cls()
        header()
        print('\n' * 2)
        print(green + black + 'Discovered a nonce!: ' + cyan + nonce)
        print(green + 'Solution: ' + cyan + solution)
        print('\n' * 5)
        print(yellow + 'Nonces found: ' + str(len(hashes)))

for i in range(0, 100000):
    testAttempt()