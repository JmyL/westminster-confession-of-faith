import sys
import re

with open(sys.argv[1], 'r') as f:
	data = f.read()
	# print(data)

p = re.compile(r'''
<pre\sclass="mermaid">
	<code>
		([^<]*)
	</code>
</pre>
''', re.VERBOSE)
(str, matchnum) = p.subn(r'<div class="mermaid">\1</div>', data)

# print(matchnum)
# print(str)
with open(sys.argv[1], 'w') as f:
	f.write(str)

	