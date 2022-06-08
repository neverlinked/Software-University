usernames_count = int(input())
usernames = set()

for _ in range(usernames_count):
    username = input()
    usernames.add(username)

print('\n'.join(usernames))
