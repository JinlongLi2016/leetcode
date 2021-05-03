import os


prefix = 'leetcode'
lines = []
sep = '/'
def prcessdir(d):
	global lines
	for f in os.listdir(d):
		if f.endswith('.md'):
			lines += ('* [' + f.split('.')[0].replace(' ', '') + '](' + sep + prefix + sep+ d + sep + f.replace(' ', '%20') + ')'),

for f in os.listdir():
    if os.path.isdir(f) and not f.startswith('.'):
       prcessdir(f)
    print(lines)
with open('README.md', mode='w', encoding='utf-8') as wf:
	lines.sort()
	wf.write('\n'.join(lines))

with open('_sidebar.md', mode='w', encoding='utf-8') as wf:
	wf.write('\n'.join(lines))