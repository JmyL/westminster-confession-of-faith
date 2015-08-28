#-*- coding: utf-8 -*-
"""build

markdown file을 몇 가지 원하는 format으로 변경해 줍니다.

Arguments: 
	- 1st: output file format, one on html, revealjs, mediawiki.
	- 2nd: input folder name
Example:
	python build.py revealjs git_rules
"""

import subprocess
import sys
import os
import re

if len(sys.argv) < 3:
	print(u"\t이 script는 2개의 인수를 필요로 합니다.\n\tCapacitance matrix file, resistance list file을 입력으로 넣어 주세요.")
	sys.exit()

output_file_format = sys.argv[1]
input_foldername = sys.argv[2]

if output_file_format == 'revealjs':

	md_filename = "./docs/"+input_foldername+"/index.md"
	filename, file_extension = os.path.splitext(md_filename)

	# if not os.path.exists(output_path): os.makedirs(output_path)

	output_filename = filename+'.html'
	
	subprocess.call(
		[
		'pandoc', 
		'-t', 'revealjs', 
		'--template=templates/template-revealjs.html', 
		'--standalone', 
		'--section-divs', 
		'--variable', 'theme="white"', 
		'--variable', 'transition="zoom"',
		md_filename,
		'-o', output_filename
		]
	)

	with open(output_filename, 'r') as f:
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
	with open(output_filename, 'w') as f:
		f.write(str)
elif output_file_format == html:
	# http://mixu.net/markdown-styles/
	pass
elif output_file_format == mediawiki:
	pass
