import os, platform, time
print('\n\x1b[1;37m Checking Update...');time.sleep(0.5)
os.system('git pull')
try:
    import wowx
except IOError:
    os.system('pip install gtts')
def Update():
    exit('\033[1;31m(×) Commands On Update Please Wait For Update ❤ ')
def rmx():
        bit = platform.architecture()[0]
        if bit == '64bit':
            print("\x1b[1;92m Congratulations ! Your Device Support this Tools")

            import wowx
        else:
            exit('\033[1;31m[×] Device Not Support 32bit')
rmx()
