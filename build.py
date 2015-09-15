#-*- coding: utf-8 -*-
"""build

markdown file을 몇 가지 원하는 format으로 변경해 줍니다.

Arguments: 
	- 1st: input folder name
Example:
	python build.py git_rules
build_option.json:
	- format: choose one from html, revealjs, mediawiki.
	- options
		- for reveal.js
			- theme
				- black: Black background, white text, blue links (default theme)
				- white: White background, black text, blue links
				- league: Gray background, white text, blue links (default theme for reveal.js < 3.0.0)
				- beige: Beige background, dark text, brown links
				- sky: Blue background, thin dark text, blue links
				- night: Black background, thick white text, orange links
				- serif: Cappuccino background, gray text, brown links
				- simple: White background, black text, blue links
				- solarized: Cream-colored background, dark green text, blue links
			- transition
				- none/fade/slide/convex/concave/zoom
"""

import subprocess
import sys
import os
import re
import json
from pprint import pprint
	
if len(sys.argv) < 2:
	print(u"\t이 script는 1개의 인수를 필요로 합니다.\n\tCapacitance matrix file, resistance list file을 입력으로 넣어 주세요.")
	sys.exit()

input_foldername = "./docs/"+sys.argv[1]


if not os.path.isdir(input_foldername):
	print(u"\t%s 이름의 폴더가 없습니다." % input_foldername)
	sys.exit()

# print(input_foldername+"/build_option.json")
# options = json.load(input_foldername+"/build_option.json")
# 

with open(input_foldername+"/build_option.json") as f:    
	data = f.read()
	build_option = json.loads(data)

output_file_format = build_option["format"]

if output_file_format == 'reveal.js':

	md_filename = input_foldername+"/index.md"
	filename, file_extension = os.path.splitext(md_filename)

	# if not os.path.exists(output_path): os.makedirs(output_path)

	output_filename = filename+'.html'
	
	subprocess.call(
		'pandoc -t revealjs' + ' ' +
		'--template=templates/template-revealjs.html' + ' ' +
		'--standalone' + ' ' +
		'--section-divs' + ' ' + 
		'--variable theme='+build_option["options"]["theme"] + ' ' + 
		'--variable transition='+build_option["options"]["transition"] + ' ' + 
		md_filename + ' ' +
		'-o' + ' ' + output_filename
	)
	
# 	subprocess.call('pandoc -t revealjs --template=templates/template-revealjs.html --standalone --section-divs --variable theme=beige --variable transition=zoom ./docs/dev_env/index.md -o ./docs/dev_env/index.html')

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

print("Conversion Finished.")
