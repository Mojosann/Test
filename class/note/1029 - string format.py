# [String format intro]

name = 'Joe'
number = 7

# data will translate to string and print
# % format (C-like)
test = 'Hello, %s. I am %s years old' % (name, number)

# str- format(py2)
test = 'Hello, {0}. I am {1} years old'.format(name, number)
test = 'Hello, {0}. I am {1} years old'.format(name='Joe', number=7)

# f-format(py3.6)
test = f'Hello, {name}. I am {number} years old'

project = 'twr'
seq = 'sq0000'
sh = 'sh0000'
ver = 5
ext = 'ma'

file_name = '%s_%s_%s_v%03d.%s' % (project, seq, sh, ver, ext)
file_name = '{0}_{1}_{2}_v{3:03d}.{4}'.format(project, seq, sh, ver, ext)
# file_name = f'{project}_{seq}_{sh}_v{ver:03d}.{ext}'
print(file_name)

# ver.Nuke
count = 119
total = 480
percent = '%'
result = float(119/480) *100
text = '%.2f%s [%s/%s]' % (result, percent, count, total)
print(text)

# ver.Houdini
# .2f為小數點後面兩位
text = '{0:.2f}% [{1}/{2}]'.format(result, count, total)
text = '%.2f%% [%s/%s]'.format(result, count, total)
print(text)