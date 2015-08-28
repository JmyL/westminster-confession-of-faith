: input parameter로 md file 이름을 넣어주어야 함.
@echo off
set input_filename=%1
for /F "tokens=1 delims=1." %%f in ("%1") do set filename=%%f
shift
pandoc -t revealjs --template=../templates/template-revealjs.html --standalone --section-divs --variable theme="white" --variable transition="zoom" %input_filename% -o ..%filename%.html
python postprocess.py ..%filename%.html

:-i list를 하나씩 보여주는 옵션!
:--self-contained 별도 css와 script file 없이 html 하나만 전달하면 되도록 하는 옵션!