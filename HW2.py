#!/usr/bin/env python3

""" David Utomi HW2 Code File"""
"""Student ID: 1960657"""

"""To run the program, uncomment the function call"""
"""for each problem at the end of the code file"""

import hashlib

users_dict = {}
users_salt = {}
salt_n_pass = {}

# Users file
with open("users", "r") as file:
    for line in file:
        (key,val) = line.strip().split(",")
        users_dict[key] = val

# Password_information
with open("password_dictionary","r") as p:
    passwords = list(p.read().split())


# Users salted
with open("users_salted","r") as s:
    for line in s:
        (key,salt,salted) = line.strip().split(",")
        users_salt[key] = salted
        salt_n_pass[salt] = salted


def Problem2_1_1():
    print("Problem 2.1.1\n")
    user_1 = list(users_dict.values())[1]
    for password in passwords:
        hashed = hashlib.sha256(bytes(password,'utf-8')).hexdigest()
        if hashed == user_1:
            print("First User: " + list(users_dict.keys())[1])
            print("Password: " + password)

            break



def Problem2_1_2():
    print("Problem 2.1.2")
    for user in users_dict.values():
        for password in passwords:
            hashed = hashlib.sha256(bytes(password,'utf-8')).hexdigest()
            if hashed == user:
                print(list(users_dict.keys())[list(users_dict.values()).index(user)])
                print("Password: " + password)
                print("\n\n")
            else:
                continue


hash_vals = {}

for password in passwords:
    hashed = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
    hash_vals[hashed] = password

def Problem2_2_4():
    print("\nProblem 2.2.4\n")

    for user in users_dict.values():

        if user in hash_vals.keys():
            print(list(users_dict.keys())[list(users_dict.values()).index(user)])
            print("Password: " + hash_vals[user])
            print("\n\n")
        else:
            continue

def Problem2_3():
    print("Problem 2.3.5\n")
    for i in range(1,len(users_dict.values())):
        if list(users_dict.values())[i] in list(users_dict.values())[i+1:]:
            repeated_hash = list(users_dict.values())[i]
            print(list(users_dict.values())[i] + " appears more than once")
            break


    users = []
    print("The two users with same hash values (same passwords are):\n")
    for k in range(1,len(users_dict.values())):
        if list(users_dict.values())[k] == repeated_hash:
            users.append(list(users_dict.keys())[k])
            print(list(users_dict.keys())[k])
            print(list(users_dict.values())[k])
            print("\n")

    salted_hash = {}
    print("Same two users, this time with different salted hash values: \n")

    for j in range(1,len(users_salt.values())):
        if list(users_salt.keys())[j] in users:
            print(list(users_salt.keys())[j])
            print(list(users_salt.values())[j])
            salted_hash[list(salt_n_pass.keys())[j]] = list(salt_n_pass.values())[j]
            print("\n")



    print("\nProblem 2.3.6")
    print("The corresponding passwords are:")
    print("\nHashed password:")


    if repeated_hash in hash_vals.keys():
        user_pass = hash_vals[repeated_hash]


    for name in users:
        print(name)
        print("Password: " + user_pass + "\n")

    print("\nVerifying Salted hashes:  if h(password + salt) == salted_hash\n")

    for j in range(len(salted_hash.values())):
        if hashlib.sha256(bytes(list(salted_hash.keys())[j] + user_pass,'utf-8')).hexdigest() == list(salted_hash.values())[j]:
            print(users[j])
            print("The hash values in users salted are correct: h(password + salt) == salted_hash == {}".format(list(salted_hash.values())[j]) +"\n")





#Problem2_1_1()
#Problem2_1_2() #It takes several hours/days to execute
#Problem2_2_4()
#Problem2_3()

