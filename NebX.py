import random
import string
import itertools
import math
import time

def f1(x):
    return [ord(c) for c in x]

def f2(x):
    return ''.join(chr(i) for i in x)

def f3(a, b):
    return [i*j for i, j in zip(a, b)]

def f4(x):
    return [i + random.randint(1, 10) for i in x]

def f5(x):
    return [i - random.randint(1, 5) for i in x]

def f6(x):
    return [i // 2 for i in x]

def f7(x):
    return [i * 3 for i in x]

def f8(x):
    return [i + 1 for i in x]

def f9(x):
    return [i - 1 for i in x]

def f10(x):
    return [i % 3 for i in x]

def f11(a, b):
    return [i ** b for i in a]

def f12(a, b):
    return [i // b for i in a]

def f13(a, b):
    return [i + b for i in a]

def f14(a, b):
    return [i - b for i in a]

def f15(x):
    return list(itertools.chain(*x))

def f16(a, b):
    return [i for i in a if i not in b]

def f17(a):
    return list(reversed(a))

def f18(a):
    return sorted(a, reverse=True)

def f19(a):
    return sorted(a)

def f20(x):
    return [math.sqrt(i) for i in x if i >= 0]

def f21(a, b):
    return [i for i in a if i == b]

def f22(a, b):
    return [i for i in a if i != b]

def f23(a, b):
    return [i for i in a if i <= b]

def f24(a, b):
    return [i for i in a if i >= b]

def f25(a):
    return [i for i in a if i % 2 == 0]

def f26(a):
    return [i for i in a if i % 2 != 0]

def f27(a):
    return [i for i in a if i % 5 == 0]

def f28(a):
    return [i for i in a if i % 7 == 0]

def f29(a):
    return [i for i in a if i % 11 == 0]

def f30(a, b):
    return [i + b for i in a]

def f31(a, b):
    return [i - b for i in a]

def f32(a, b):
    return [i * b for i in a]

def f33(a, b):
    return [i // b for i in a]

def f34(a, b):
    return [i ** b for i in a]

def f35(a, b):
    return [i % b for i in a]

def f36(a, b):
    return [i & b for i in a]

def f37(a, b):
    return [i | b for i in a]

def f38(a, b):
    return [i ^ b for i in a]

def f39(a, b):
    return [~i for i in a]

def f40(a):
    return [i + 10 for i in a]

def f41(a):
    return [i - 10 for i in a]

def f42(a):
    return [i * 10 for i in a]

def f43(a):
    return [i // 10 for i in a]

def f44(a):
    return [i ** 10 for i in a]

def f45(a):
    return [i % 10 for i in a]

def f46(a):
    return [i & 10 for i in a]

def f47(a):
    return [i | 10 for i in a]

def f48(a):
    return [i ^ 10 for i in a]

def f49(a):
    return [i << 1 for i in a]

def f50(a):
    return [i >> 1 for i in a]

def f51(a):
    return [i & i for i in a]

def f52(a):
    return [i | i for i in a]

def f53(a):
    return [i ^ i for i in a]

def f54(a):
    return [i << 2 for i in a]

def f55(a):
    return [i >> 2 for i in a]

def f56(a):
    return [i + 100 for i in a]

def f57(a):
    return [i - 100 for i in a]

def f58(a):
    return [i * 100 for i in a]

def f59(a):
    return [i // 100 for i in a]

def f60(a):
    return [i ** 100 for i in a]

def f61(a):
    return [i % 100 for i in a]

def f62(a):
    return [i & 100 for i in a]

def f63(a):
    return [i | 100 for i in a]

def f64(a):
    return [i ^ 100 for i in a]

def f65(a):
    return [i << 3 for i in a]

def f66(a):
    return [i >> 3 for i in a]

def f67(a):
    return [i & 200 for i in a]

def f68(a):
    return [i | 200 for i in a]

def f69(a):
    return [i ^ 200 for i in a]

def f70(a):
    return [i << 4 for i in a]

def f71(a):
    return [i >> 4 for i in a]

def f72(a):
    return [i & 400 for i in a]

def f73(a):
    return [i | 400 for i in a]

def f74(a):
    return [i ^ 400 for i in a]

def f75(a):
    return [i + 1 for i in a]

def f76(a):
    return [i - 1 for i in a]

def f77(a):
    return [i * 1 for i in a]

def f78(a):
    return [i // 1 for i in a]

def f79(a):
    return [i ** 1 for i in a]

def f80(a):
    return [i % 1 for i in a]

def f81(a):
    return [i & 1 for i in a]

def f82(a):
    return [i | 1 for i in a]

def f83(a):
    return [i ^ 1 for i in a]

def f84(a):
    return [i << 5 for i in a]

def f85(a):
    return [i >> 5 for i in a]

def f86(a):
    return [i & 500 for i in a]

def f87(a):
    return [i | 500 for i in a]

def f88(a):
    return [i ^ 500 for i in a]

def f89(a):
    return [i + 1000 for i in a]

def f90(a):
    return [i - 1000 for i in a]

def f91(a):
    return [i * 1000 for i in a]

def f92(a):
    return [i // 1000 for i in a]

def f93(a):
    return [i ** 1000 for i in a]

def f94(a):
    return [i % 1000 for i in a]

def f95(a):
    return [i & 1000 for i in a]

def f96(a):
    return [i | 1000 for i in a]

def f97(a):
    return [i ^ 1000 for i in a]

def f98(a):
    return [i << 6 for i in a]

def f99(a):
    return [i >> 6 for i in a]

def f100(a):
    return [i & 10000 for i in a]

def f101(a):
    return [i | 10000 for i in a]

def f102(a):
    return [i ^ 10000 for i in a]

def f103(a):
    return [i << 7 for i in a]

def f104(a):
    return [i >> 7 for i in a]

def f105(a):
    return [i + random.randint(1, 10000) for i in a]

def f106(a):
    return [i - random.randint(1, 10000) for i in a]

def f107(a):
    return [i * random.randint(1, 10000) for i in a]

def f108(a):
    return [i // random.randint(1, 10000) for i in a]

def f109(a):
    return [i ** random.randint(1, 10000) for i in a]

def f110(a):
    return [i % random.randint(1, 10000) for i in a]

def f111(a):
    return [i & random.randint(1, 10000) for i in a]

def f112(a):
    return [i | random.randint(1, 10000) for i in a]

def f113(a):
    return [i ^ random.randint(1, 10000) for i in a]

def f114(a):
    return list(itertools.product(a, repeat=2))

def f115(a):
    return list(itertools.permutations(a))

def f116(a):
    return list(itertools.combinations(a, 2))

def f117(a):
    return list(itertools.combinations_with_replacement(a, 2))

def f118(a):
    return list(itertools.chain.from_iterable(a))

def f119(a):
    return list(itertools.count(1, 1))

def f120(a):
    return [math.sin(i) for i in a]

def f121(a):
    return [math.cos(i) for i in a]

def f122(a):
    return [math.tan(i) for i in a]

def f123(a):
    return [math.log(i) for i in a]

def f124(a):
    return [math.exp(i) for i in a]

def f125(a):
    return [math.fabs(i) for i in a]

def f126(a):
    return [math.floor(i) for i in a]

def f127(a):
    return [math.ceil(i) for i in a]

def f128(a):
    return [math.trunc(i) for i in a]

def f129(a):
    return [math.radians(i) for i in a]

def f130(a):
    return [math.degrees(i) for i in a]

def f131(a):
    return [random.random() for i in a]

def f132(a):
    return [random.randint(1, 100) for i in a]

def f133(a):
    return [random.choice(a) for i in a]

def f134(a):
    return random.shuffle(a)

def f135(a):
    return random.sample(a, 5)

def f136(a):
    return random.choices(a, k=5)

def f137(a):
    return random.uniform(1, 100)

def f138(a):
    return random.gauss(0, 1)

def f139(a):
    return random.betavariate(1, 1)

def f140(a):
    return random.choice([True, False])

def f141(a):
    return time.time()

def f142(a):
    return time.localtime(a)

def f143(a):
    return time.gmtime(a)

def f144(a):
    return time.sleep(a)

def f145(a):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(a))

def f146(a):
    return [i for i in a if i]

def f147(a):
    return [i for i in a if not i]

def f148(a):
    return list(set(a))

def f149(a):
    return list(sorted(set(a)))

def f150(a):
    return list(sorted(set(a), reverse=True))

if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(100)]
    result = f1(arr)
    for i in range(1, 151):
        result = globals()[f'f{i}'](result)
    print(result)
user_list = {}  # Imports an empty dictionary.
messages = {}
print("Welcome, admin. Please select a password:")
admin_password = input()
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

while 1 == 1:   # Creates a recursive loop. Probably a better way to do this.

    print(  #Greeting message.
        "\n"
        "Press 1 to create a new account."
        "\nPress 2 for a current list of users. (Only usable by admin)"
        "\nPress 3 to send and receive messages."
        "\nPress 4 for help."
        "\nPlease enter your choice:\n"
        )

    user_input = input()    # Dictates which menu option to execute.

    if user_input == '1':
        print("\nPlease enter your preferred name:")
        attempted_name = input().lower()    # Disregards case.
        if attempted_name in user_list:     # Checks if name exists
            print("That name is already taken. Please choose again.")
        else:   # If name is unique, adds it to database.
            user_list.update({attempted_name.lower(): 'password'}) # Default password is "password" temporarily.
            print("Welcome to the site, "
                  + attempted_name +
                  "! Please choose a password:"
                  )
            user_list[attempted_name] = input()     # User defines new password.
            messages[attempted_name] = "DEFAULT MESSAGE"

    elif user_input == '2':     # Displays all current users and their passwords.
        print("Please enter admin password:")
        if input() == admin_password:
            print('\n' + str(user_list))
        else:
            print('\nPassword incorrect. Please try again.')

    elif user_input == '3':     # messaging other users, checking messages
        login_name = input("Please enter your user name: ").lower()     # User login
        if login_name in user_list:
            login_password = input("Please enter password for " + login_name + ": ")
            if login_password == user_list[login_name]:
                print("\nCorrect password entered.\nPress 1 to write a message.\nPress 2 to read your message.\n")
                user_option = input()
                if user_option == '1':
                    messaged_user = input("Please enter the name of the person you'd like to message:").lower()
                    if messages[messaged_user] != "DEFAULT MESSAGE":    # If user's message is "Default message", inbox
                        print("User's inbox is full.")                  #   is marked as full
                    else:
                        message = input("Please type your message:")
                        messages[messaged_user] = message
                elif user_option == '2':
                    print('\n' + messages[login_name])
                    mark_read = input("Mark message as read? y/n:")
                    if mark_read == "y":
                        print ("\nMessage marked as 'read'.")
                        messages[login_name] = "DEFAULT MESSAGE"    # If user marks message as read, it returns to
                    elif mark_read == "n":                          #   default, which opens up the inbox for more
                        print ("\nMessage not marked as 'read'.")   #   messages.
                    else:
                        print("\nInvalid option.")
                else:
                    print("\n That is not a valid option.")
            else:
                print("\nPassword not valid.")
        else:
            print("\nInvalid username.")


    else:   # Help message.
        print(
            "This is a simple messaging database. "
            "When creating a username,\nit must be unique, "
            "but the system will automatically\nformat your unique "
            "username to be in all lowercase.\n"
            "Passwords, however, are case-sensitive."
            "Messages can be sent to other users, and users "
            "can check their own messages."
            )
# done
import hashlib, binascii
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--ntlmv1', help='NTLMv1 Hash in responder format', required=True)
parser.add_argument('--hashcat', help='hashcat path, eg: ~/git/hashcat', required=False)
parser.add_argument('--hcutils', help='hashcat-utils path, eg: ~/git/hashcat-utils', required=False)
parser.add_argument('--json', help='if this is set to anything it will output json, eg: --json 1', required=False)
args = parser.parse_args()
# SERVER1$::MOG:7EF3F506F5EA510E00000000000000000000000000000000:1217169BD7BE0270A033899BD440016D3E6DACAF5894D504:ff81dfd6b12c269d
# evilmog::DUSTIN-5AA37877:E343946E455EFC72746CF587C42022982F85252CC731BB25:51A539E6EE061F647CD5D48CE6C686653737C5E1DE26AC4C:1122334455667788
hashsplit = args.ntlmv1.split(':')
challenge = hashsplit[5]
lmresp = hashsplit[3]
ntresp = hashsplit[4]
ct3 = ntresp[32:48]
data = {'ntlmv1': args.ntlmv1, 'user': hashsplit[0], 'domain': hashsplit[2], 'challenge': challenge, 'lmresp': lmresp,
        'ntresp': ntresp, 'ct3': ct3}

if lmresp[20:48] != "0000000000000000000000000000":
    ct1 = ntresp[0:16]
    ct2 = ntresp[16:32]
    ct3 = ntresp[32:48]
    if args.json is None:
        print("Hashfield Split:")
        print(str(hashsplit) + "\n")

        print("Hostname: " + hashsplit[2])
        print("Username: " + hashsplit[0])
        print("Challenge: " + challenge)
        print("LM Response: " + lmresp)
        print("NT Response: " + ntresp)
        print("CT1: " + ct1)
        print("CT2: " + ct2)
        print("CT3: " + ct3 + "\n")

        print("To Calculate final 4 characters of NTLM hash use:")
        if args.hcutils:
            print(args.hcutils + "/ct3_to_ntlm.bin " + ct3 + " " + challenge + "\n")
        else:
            print("./ct3_to_ntlm.bin " + ct3 + " " + challenge + "\n")
        # ./ct3_to_ntlm.bin 2e1e4bf33006ba41 cb8086049ec4736c

        print("To crack with hashcat create a file with the following contents:")
        print(ct1 + ":" + challenge)
        print(ct2 + ":" + challenge + "\n")

        print("echo \"" + ct1 + ":" + challenge + "\">>14000.hash")
        print("echo \"" + ct2 + ":" + challenge + "\">>14000.hash\n")

        print("To crack with hashcat:")
        if args.hashcat:
            print(
                args.hashcat + "/hashcat -m 14000 -a 3 -1 " + args.hashcat + "/charsets/DES_full.charset --hex-charset 14000.hash ?1?1?1?1?1?1?1?1\n")
        else:
            print("./hashcat -m 14000 -a 3 -1 charsets/DES_full.charset --hex-charset 14000.hash ?1?1?1?1?1?1?1?1\n")

if lmresp[20:48] == "0000000000000000000000000000":
    clientchallenge = hashsplit[5]
    combinedchallenge = clientchallenge + lmresp[0:16]

    m = hashlib.md5()
    m.update(binascii.unhexlify(combinedchallenge))
    md5hash = m.hexdigest()
    srvchallenge = md5hash[0:16]
    data['srvchallenge'] = srvchallenge
    ct1 = ntresp[0:16]
    ct2 = ntresp[16:32]

    if args.json == None:
        print(
            "Hash response is ESS, consider using responder with --lm or --disable-ess with a static challenge of 1122334455667788")
        print("[-] Client Challenge: " + clientchallenge)
        print("[-] LMResp[0:16]: " + lmresp[0:16])
        print("[-] Combined Challenge: " + combinedchallenge)
        print("Hashfield Split:")
        print(str(hashsplit) + "\n")
        print("[-] MD5 Hash of Combined Challenge: " + md5hash)
        print("Hostname: " + hashsplit[2])
        print("Username: " + hashsplit[0])
        print("LM Response: " + lmresp)
        print("NT Response: " + ntresp)
        print("SRV Challenge: " + srvchallenge + "\n")

        print("To Calculate final 4 characters of NTLM hash use:")
        # ./ct3_to_ntlm.bin 2e1e4bf33006ba41 cb8086049ec4736c 338d08f8e26de93300000000000000000000000000000000
        if args.hcutils:
            print(args.hcutils + "/ct3_to_ntlm.bin " + ct3 + " " + clientchallenge + " " + lmresp + "\n")
        else:
            print("./ct3_to_ntlm.bin " + ct3 + " " + clientchallenge + " " + lmresp + "\n")

        print("To crack with hashcat create a file with the following contents:")
        print(ct1 + ":" + srvchallenge)
        print(ct2 + ":" + srvchallenge + "\n")
        print("echo \"" + ct1 + ":" + srvchallenge + "\">>14000.hash")
        print("echo \"" + ct2 + ":" + srvchallenge + "\">>14000.hash\n")

        print("To crack with hashcat:")
        if args.hashcat:
            print(
                args.hashcat + "/hashcat -m 14000 -a 3 -1 " + args.hashcat + "/charsets/DES_full.charset --hex-charset 14000.hash ?1?1?1?1?1?1?1?1\n")
        else:
            print("./hashcat -m 14000 -a 3 -1 charsets/DES_full.charset --hex-charset 14000.hash ?1?1?1?1?1?1?1?1\n")


if args.json != None:
    if lmresp[20:48] != "0000000000000000000000000000":
        if args.hcutils:
            data['ct3_crack'] = (args.hcutils + "/ct3_to_ntlm.bin " + ct3 + " " + challenge)
        else:
            data['ct3_crack'] = ("ct3_to_ntlm.bin " + ct3 + " " + challenge)
        data['hash1'] = (ct1 + ":" + challenge)
        data['hash2'] = (ct2 + ":" + challenge)
    if lmresp[20:48] == "0000000000000000000000000000":
        if args.hcutils:
            data['ct3_crack'] = (args.hcutils + "/ct3_to_ntlm.bin " + ct3 + " " + clientchallenge + " " + lmresp)
        else:
            data['ct3_crack'] = ("ct3_to_ntlm.bin " + ct3 + " " + clientchallenge + " " + lmresp)
        data['hash1'] = (ct1 + ":" + srvchallenge)
        data['hash2'] = (ct2 + ":" + srvchallenge)

    # process data
    json_data = json.dumps(data)
    print(json_data)
