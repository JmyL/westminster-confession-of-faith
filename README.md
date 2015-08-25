% Markdown으로 slideshow 만들기
% Sungsik Nam
% 2015-08-17

# 환경셋업

## pandoc 설치

* [Pandoc 홈페이지](http://pandoc.org/installing.html)에서 Windows용 설치파일을 다운로드해서 설치.

![Pandoc Download Page](readme-img/pandoc.png)

## Anaconda 설치

* [Continuum 홈페이지](http://continuum.io/downloads)에서 2.x용 설치파일을 다운로드해서 설치.

![Anaconda Download Page](readme-img/anaconda.png)

## Markdown 문서 편집기 Plug-in 설치
* Eclipse->Help->Eclipse Marketplace...->Markdown 검색->Markdown Test Editor 1.2.0 Install
* doc-git-setting Project 우클릭 -> Test file Encoding -> Other:UTF-8 선택 -> OK Click

## Markdown Doc Build Setting in Eclipse
* doc-git-setting Project 우클릭 -> Builder 선택 -> New -> Program 선택 및 OK -> Location: ${workspace_loc:/doc-git-setting/scripts/build_md_for_reveal.js.bat} 입력 -> Working Directory: ${workspace_loc:/doc-git-setting/scripts} -> Arguments: ../${selected_resource_name} -> OK

## Markdown Doc Build
* ctrl + B 
  ※하지만 따로 세팅하지 않으면 Open된 모든 문서가 Build 됨 주위

* Build Tip
Eclipse key 설정에서 
Build All -> ctrl+B, A
Build Project -> ctrl+B, B
로 설정을 해두면
Ctrl +B, B를 누르면 선택된 Project만 Build 가능
		    

# 문서작성

## 순서

```mermaid
graph TD
	B(프로젝트 복사 & 내려받기)
    B --> C(문서 작성)
    C --> D(mardown file 빌드)
    D --> E(결과물 확인)
    E --> F(Push!)
```

## 프로젝트 복사

* doc-git-setting project에서 "코드 저장소 복사" 클릭하고, eclipse에서 git clone!

![Copy Repository](readme-img/copy-repo.png)


## 문서 작성

```
# Title Slide (level 1)

## Slide (level 2)

* Bullet List 1
* Bullet List 2

## Slide (level 3)
...
```

## mardown file 빌드

* scripts folder에서 아래 내용 실행.
* __`../`에 주의!__

```
build_md_for_reveal.js.bat ../myfile.md 
```

## 결과물 확인

* Chrome으로 release folder에 생성된 html 파일을 열어서 결과물 확인.


## Push!

Yobi에 push!

![push to upstream](readme-img/push.png)



# reveal.js 간단한 소개

## 단축키

* ?: 단축키 보기
* ESC: 전체 맵 보기
* f: Full Screen
* .: Black Screen

## pdf로 저장하려면

* 경로 뒤에 `?print-pdf`를 붙임
* e.g. `.../doc-git-setting/myfile.html?print-pdf`
* ctrl+p로 인쇄메뉴 진입해서 대상을 pdf로 셋팅해서 저장(Chrome에서만 확인됨).


# 글 쓰기 문법

## Markdown

* [Markdown 문법 가이드](http://scriptogr.am/myevan/post/markdown-syntax-guide-for-scriptogram)
* [Markdown 표준문서 번역](https://nolboo.github.io/blog/2013/09/07/john-gruber-markdown)

## Markdown for reveal.js

* [producing slide shows with pandoc](http://pandoc.org/README.html#producing-slide-shows-with-pandoc) 참조.
* 주의사항: __title slide(`#` 한개 붙인 title 아래)에 내용이 들어가면 정상적으로 build되지 않습니다!__

# Diagram & Flowchart 문법

## Flowchart

* [Flowchart 문법](http://knsv.github.io/mermaid/flowchart.html) 참조.

```
graph LR
    A[Square Rect] -- Link text --> B((Circle))
    A --> C(Round Rect)
    B --> D{Rhombus}
    C --> D
```

```mermaid
graph LR
    A[Square Rect] -- Link text --> B((Circle))
    A --> C(Round Rect)
    B --> D{Rhombus}
    C --> D
```

## Sequence Diagram

* [Sequence Diagram 문법](http://knsv.github.io/mermaid/sequenceDiagram.html) 참조.

```
sequenceDiagram
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
```

```mermaid
sequenceDiagram
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
```

## Gant diagram

* [Gant Diagram 문법](http://knsv.github.io/mermaid/gantt.html) 참조.

```
gantt
    title A Gantt Diagram

    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :after a1  , 20d
    section Another
    Task in sec      :2014-01-12  , 12d
    anther task      : 24d
```

```mermaid
gantt
    title A Gantt Diagram

    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :after a1  , 20d
    section Another
    Task in sec      :2014-01-12  , 12d
    anther task      : 24d
```



# 마치며...

## TODO

* Web이랑 local이랑 다르게 보이는 현상 수정.
* title slide 배경, font type, font 크기 등 변경.
* li 등 일반 element에도 word-break 적용.
* 한글 글씨 한개가 줄내림되는 현상 수정.
* image 및 mermaid output 크기를 canvas 크기에 맞게 조절.
