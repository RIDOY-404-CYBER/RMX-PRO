import os,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    print('\033[1;32m[•] Congrats! Your Device Support This Tools')
    os.system('xdg-open https://facebook.com/groups/770617227293870/')
    import PUB4
else:
    exit('\033[38;196m[×] Sorry Device Not Support')

