import pathlib, subprocess

p = pathlib.Path('qwe.txt')
if p.exists():
    p.unlink()

with p.open('a') as f1:
    print('a' * 999, file=f1)
    print('b' * 999, file=f1)
    f1.flush()
    # append to the same file from another process
    subprocess.call("echo ccc >> qwe.txt", shell=True)

with p.open() as f1:
    # we expect 11000
    print(f1.read().index('ccc'))

