read = int(input())

hours = read // 3600

remaining = read - (hours * 3600)

minutes = remaining // 60

seconds = (remaining - minutes * 60)

print(f"{hours}:{minutes}:{seconds}")
