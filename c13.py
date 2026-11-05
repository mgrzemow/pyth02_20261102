import re
regex1 = r'^([\w-]+)==(\d+)\.(\d+)(\.(.+))?$'

# import os
# os.system('pip freeze')
import subprocess
r = subprocess.run('pip freeze', capture_output=True, shell=True, encoding='utf-8')
wydruk = r.stdout.splitlines()
for line in wydruk:
    m = re.match(regex1, line)
    if m is not None:
        print(m.groups())

# napisać funkcję, która wyciąga listę zainstalowanych pakietów w formie słownika:
{
    'django': (3, 2, '13.3'),
    'requests': (3, 2, None),
}