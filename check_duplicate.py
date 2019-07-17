import os

count = 0
count_seen = 0


def list_pwd():
    path = os.chdir("C:\\projects\\deploy")
    ls = os.listdir(path)
    for l in ls:
        print(l)


list_pwd()

file = input("\nEnter file name: ")

with open(file, "r+") as f:
    seen = set()
    d = f.readlines()
    f.seek(0)
    for line in d:
        line_lower = line.lower()
        count += 1
        if line_lower in seen:
            print(line)
            count_seen += 1
        else:
            f.write(line)
            seen.add(line_lower)
    f.truncate()
f.close()

print('Count: ' + str(count))
print('Duplicates: ' + str(count_seen))
files = count - count_seen
print('Files: ' + str(files))
