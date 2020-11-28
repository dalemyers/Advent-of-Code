import hashlib

key = "yzbqklnj"

counter = -1

part1_found = False

while True:
    counter += 1
    data = key + str(counter)
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    digest = md5.digest().hex()
    if not part1_found and digest.startswith("00000"):
        part1_found = True
        print("Part 1:", counter)
    if digest.startswith("000000"):
        print("Part 2:", counter)
        break
