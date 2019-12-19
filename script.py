import os
import stat
# curr_perm = oct(stat.S_IMODE(os.stat("/tmp/test/test3").st_mode))[2:]
file = "/tmp/test/test3"
curr_perm = stat.S_IMODE(os.stat(file).st_mode)
# print(oct(curr_perm)[2:])


def filemod(x):
    x = str(oct(x)[2:])
    perm = ['?']
    all_perm = {0: "---", 1: "--x", 2: "-w-", 3: "-wx", 4: "r--", 6: "r-x", 6: "rw-", 7: "rwx"}
    if len(x) == 3:
        for i in x:
            if int(i) in all_perm.keys():
                perm += all_perm.get(int(i))
    else:
        # suid = 4000
        # sgid = 2000
        # stic = 1000
        for i in x[1:]:
            if int(i) in all_perm.keys():
                perm += all_perm.get(int(i))
        if x[0] == '1':
            if int(x[3]) % 2 == 0:
                perm[9] = 'T'
            else:
                perm[9] = 't'
        if x[0] == '2':
            if int(x[2]) % 2 == 0:
                perm[6] = 'S'
            else:
                perm[6] = 's'
        if x[0] == '3':
            if int(x[2]) % 2 == 0:
                perm[6] = 'S'
            else:
                perm[6] = 's'
            if int(x[3]) % 2 == 0:
                perm[9] = 'T'
            else:
                perm[9] = 't'
        if x[0] == '4':
            if int(x[1]) % 2 == 0:
                perm[3] = 'S'
            else:
                perm[3] = 's'
        if x[0] == '5':
            if int(x[1]) % 2 == 0:
                perm[3] = 'S'
            else:
                perm[3] = 's'
            if int(x[3]) % 2 == 0:
                perm[9] = 'T'
            else:
                perm[9] = 't'
        if x[0] == '6':
            if int(x[1]) % 2 == 0:
                perm[3] = 'S'
            else:
                perm[3] = 's'
            if int(x[2]) % 2 == 0:
                perm[6] = 'S'
            else:
                perm[6] = 's'
        if x[0] == '7':
            if int(x[1]) % 2 == 0:
                perm[3] = 'S'
            else:
                perm[3] = 's'
            if int(x[2]) % 2 == 0:
                perm[6] = 'S'
            else:
                perm[6] = 's'
            if int(x[3]) % 2 == 0:
                perm[9] = 'T'
            else:
                perm[9] = 't'

    return ''.join(perm)


print(filemod(curr_perm))
