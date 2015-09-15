% MELFAS S/W 개발환경
% Sungsik Nam
% 2015-08-28

개요
==========================================================

컨셉
-------------------------------------------------

공짜

. . .

만은 아니고, 무료이면서도 강력한 오픈소스 툴들을 다양하게 활용하고 있습니다 ;)

IDE
-------------------------------------------------

![](img/eclipse.png)

Compiler
-------------------------------------------------

![](img/gnugcc.png)

Build 환경
-------------------------------------------------

MSYS

Glue & Research Language
-------------------------------------------------

![](img/python.jpg)

협업 S/W 개발 플랫폼
-------------------------------------------------

![](img/yobi.png)


설치 진행에 앞서서...
-------------------------------------------------

* Windows 계정(ID)는 영어로 해 주시기 바랍니다. 보통 format된 PC를 받는데, 이 때 한글 이름으로 되어있는 경우 영어로 다시 설치해 주기를 요청해 주세요.
* 모든 설치는 별도로 source용 공간을 partitioning하지 않은 상황에서 진행되어야 합니다. 일반적인 방법으로 개발 진행 시 항상 Git 서버에 소스가 백업되므로 포맷할 때도 불편함이 없습니다.
* 특정 tool 설치 시 환경변수인 HOME 을 수정해서 문제 된 경우가 있었습니다. HOME 변수도 기본 셋팅인 C:\Users\아이디\ 에서 수정하지 말아 주세요.
* 문서대로 따라갔는데 문제가 있다면 ssnam@melfas.com으로 문제 사항을 공유해 주세요 ;)




Eclipse
==========================================================

-------------------------------------------------

* [JRE](http://www.google.com/search?q=java+jre) 설치.
* [Eclipse](http://www.google.com/search?q=Eclipse+CDT+Download) 에서 'Eclipse package'를 OS에 맞추어 다운로드 받은 후 적당한 위치에 압축해제. Mars 버전 좋습니다! Markdown 편집도 되고, gitflow도 통합되어있고... ;)
* Mars 버전 CDT에 버그가 있네요!(2015-09-08) CDT 8.7 버전에서 C99 문법을 사용한 C file에서 syntax highlight가 정상동작하지 않습니다. <small><code>http://download.eclipse.org/tools/cdt/builds/master/nightly</code></small>에서 C99 관련 내용 및 CDT를 8.8 이후로 업데이트 받으면 해결됩니다.
* Checkout이 안되는 버그가 있네요..
`http://download.eclipse.org/egit/updates`에서 최신 egit download하면 해결됩니다. 다음부터는 SR2부터 써야겠습니다! 

Eclipse GNU Arm Plugin
-------------------------------------------------

* [Eclipse GNU Arm Plugin](http://www.google.com/search?q=Eclipse+GNU+ARM+Plugin+Install) 에서 다운로드.
* 링크의 설명에 따라 install. 큰 변화가 없다면 아래 방법과 동일할 겁니다.
* Eclipse 실행 -> Help -> Install New Software 를 클릭한 뒤 add 클릭.
* Name에 GNU ARM Eclipse Plugin, Location에 http://gnuarmeclipse.sourceforge.net/updates 를 입력한 뒤 OK.


멜파스 표준설정 적용
-------------------------------------------------

* <a href="./files/melfas-20150831.epf" download>Eclipse Preference</a> Update
	* File -> Import -> General -> Preference 에서 다운로드 한 파일 선택 후 Next -> Import all
* [Font(나눔고딕코딩)](http://www.google.com/search?q=나눔고딕코딩+다운로드)


코드 뷰티파이어 
-------------------------------------------------

* Code의 indentation 등을 사내 표준에 맞게 수정해 주는 도구입니다.
* [Code beautifier](./files/AStyle-2.04-windows.zip) 다운로드.
* 압축파일 아래 `\AStyle\bin\`의 `AStyle.exe`를 `C:\MinGW\msys\1.0\bin\AStyle.exe`로 복사.
* 다음 페이지와 같이 Eclipse 설정!

-------------------------------------------------

* Eclipse의 (Run -> External Tools -> External Tools Configuration)external tools configuration에서 아래와 같이 새로운 tool 등록.
	* Location: `C:\MinGW\msys\1.0\bin\AStyle.exe`
	* Working Directory: `${workspace_loc:/${project_name}}`
	* Arguments: `--style=allman -r -n -Z -Q *.c *.h`
	* Build tab에서 자동 빌드(Build before launch) 체크 해제.
	* Refresh tab에서 실행 후 file refresh하도록 설정(Refresh resources upon completion) 체크.
	* Apply!
* 이제 선택한 프로젝트의 소스파일을 CTRL+SHIFT+F로 소스 코드를 beautifying할 수 있습니다.


Git Setting
-------------------------------------------------

* <a href="./files/.gitconfig" download>.gitconfig</a>, <a href="./files/.global_ignore" download>.global_ignore</a> 파일 다운로드.
* 해당 파일을 `C:\Users\아이디\` 폴더에 copy.
* .gitconfig 파일 안에 있는 이름, 이메일을 gerrit 셋팅과 동일하게 설정.
Eclipse에서 Window - Preference - Git - Configuration 에서 user email & name 수정.


Compiler
==========================================================

-------------------------------------------------

* 프로젝트마다 다른 버전의 compiler를 쓰고 있으므로 참여하고 있는 프로젝트가 사용하고 있는 버전의 컴파일러를 설치해 주셔야 합니다. 이는 이클립스에서 Project Properties -> C/C++ Build -> Environment -> PATH 에서 GNU Tools ARM Embedded 관련 경로이름을 통해 확인할 수 있습니다. **이 PATH를 임의로 수정하시라는 의미가 아닙니다. 주의!**


Cortex-M series Compiler
-------------------------------------------------

* [GNU Tools for ARM Embedded Processors](http://www.google.com/search?q=GNU+Tools+for+ARM+Embedded+Processors+Download) 다운로드.
* __4.9-2014-q4-major__ 버전에서 Cortex-M3 코어에서 strict-volatile-bitfields 옵션이 제대로 동작 하지 않는 문제가 해결되었으므로 주의 바랍니다.
* 설치 경로에서 __"Program Files" 경로는 지워 주셔야__ 합니다.
	* e.g. `C:\Program Files\GNU Tools ARM Embedded\4.8 2014q2` -> `C:\GNU Tools ARM Embedded\4.8 2014q2`

Arm Linux-App용 Compiler
-------------------------------------------------

* Set에서 구동할 debug app 개발을 위해 설치합니다.
* [arm linuxhf compiler](http://www.google.com/search?q=gcc-linaro-arm-linux-gnueabihf+win32) 다운로드.
* `gcc-linaro-arm-linux-gnueabihf-..._win32.exe` 이름의 파일을 다운로드합니다. 유사한 이름의 파일이 많으니 주의바랍니다.
* 설치 경로에서 "Program Files" 경로는 지워 주셔야 합니다. 예를 들어, C:\Linaro\gcc-linaro-arm-linux-gnueabihf-4.8-2013.10 과 같이 설치합니다.


PC App용 Compiler 및 Build 환경 {#build_env}
-------------------------------------------------

* [MinGW Installer](http://www.google.com/search?q=mingw-get-setup.exe)에서 mingw-get-setup.exe 다운로드.
* mingw-developer-toolkit와 msys-base, mingw32-base, mingw32-gcc-g++를 체크.
* 상단메뉴에 Installation - Apply Changes를 클릭하면 설치.


H/W 드라이버 설치
==========================================================

Fx2 Board
----------------------------------

* I2C Emulation 장비입니다. USB 개발환경에서는 필요하지 않습니다.
* [Device Driver](./files/FX2_USB_Driver_v348_20120430_withCert64Cy.7z) 다운로드.
* (Windows 8은 다음 페이지의 설치 시 주의사항 참조.)
* 장치관리자에서 인식이 안된 장치를 우클릭하고 '드라이버 업데이트' 클릭.
* '컴퓨터에서 드라이버 소프트웨어 찾아보기' 클릭
* '찾아보기' 클릭 후, 압축을 해제한 폴더의 컴퓨터 os에 맞는 폴더를 선택(windows 8은 windows 7 폴더의 드라이버 선택)

----------------------------------

Windows 8에서는 디지털서명이 없는 드라이버 적용을 위해 다음과 같은 준비작업이 필요합니다.

* Windows + i를 누르고 '전원'버튼 클릭.
* shift키를 누른 상태에서 '다시시작' 클릭.
* '문제해결' 클릭
* '고급옵션' 클릭
* '시작설정'에 들어가서 '다시시작' 클릭하면 재부팅됨.
* 선택 창에서 7 또는 F7을 눌러서 '드리아버서명적용사용안함' 선택.

기타 개발환경
----------------------------------

* wiki에 관련 페이지를 생성하겠습니다.


읽을거리...
==========================================================

---------------------------------------------

* [Top 10 Eclipse Mars Features](http://eclipsesource.com/blogs/2015/06/24/top-10-eclipse-mars-features/)
* [Eclipse Plug-in 개발](http://cafe.naver.com/eclipseplugin.cafe?iframe_url=/ArticleRead.nhn%3Farticleid=17)
* [Eclipse Article](http://www.javajigi.net/display/IDE/Eclipse)
* [GEF의 이해 - 1부](http://eclipse.or.kr/wiki/%ED%8A%B9%EC%A7%91%EA%B8%B0%EC%82%AC:GEF%EC%9D%98_%EC%9D%B4%ED%95%B4_1%EB%B6%80)