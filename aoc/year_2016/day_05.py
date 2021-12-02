import hashlib

key = "cxdnnyjw"


def part1():
    counter = -1

    password = ""

    while True:
        counter += 1
        data = key + str(counter)
        md5 = hashlib.md5()
        md5.update(data.encode('utf-8'))
        digest = md5.digest().hex()
        if digest.startswith("00000"):
            password += digest[5]
            if len(password) == 8:
                return password


def part2():
    counter = -1

    password = [None] * 8

    while True:
        counter += 1
        data = key + str(counter)
        md5 = hashlib.md5()
        md5.update(data.encode('utf-8'))
        digest = md5.digest().hex()
        if digest.startswith("00000"):
            index = digest[5]

            if index not in "01234567":
                continue

            character = digest[6]

            if password[int(index)] is None:
                password[int(index)] = character

                if None not in password:
                    return "".join(password)

#print("Part 1:", part1())
print("Part 2:", part2())