% Git을 이용한 소스 관리방안
% Sungsik Nam
% 2015-08-17

# Development With<br />Yobi & Git

## CVCS란? 

* Centralized Version Control System의 약자입니다.
* 서버에만 repository가 존재합니다.
* SVN이 대표적인 CVCS입니다.

## CVCS는 이제 그만...

> 토발츠는 기존 CVS들을 거의 쓰레기라고 평합니다.
> 그리고 자기가 Distributed의 특성을 가진 CVS를 만들어 보고자 시작한
> 이야기가 아래 영상에 나옵니다. GIT의 철학을 잘 알 수 있습니다.

*출처: [Git의 실제 적용](http://rapapa.net/?p=50)*

## 

* SVN에서 여러 branch로 개발하면서 다른 branch를 checkout 해 보셨어요? 
* 서버에 repository가 있으니 속도가 느려요...
* 원래 있던 브랜치에서 커밋을 아직 안 한 파일이 남아 있어도 다른 branch로 이동이 안 됩니다.
* 이러다보니 대부분 1개 branch로 개발하고, 여러 branch로 개발한다면 branch 갯수만큼 프로젝트를 생성해 놓고 개발하게 됩니다.
* 머지가 매우 어렵습니다. 전체를 파악하고 있는 소수의 사람이 '머지 전문가'가 됩니다! <br />*출처: [버전시스템 유량기 ](https://gist.github.com/benelog/2922437)*


## DVCS란?

* DVCS란 Distrubuted Version Control System의 약자입니다.
* DVCS에서는 repository가 server에만 있는게 아니라 모든 사용자의 local disk에 존재합니다.
* 대표적인 DVCS가 git이죠 ;)


## 이제는 Git!

* DVCS에서는 Server가 박살나도? 괜찮습니다. 내 PC에 있어요 ㅎㅎ 
* 물론 인터넷이 안돼도 상관 없지요. Local에서 열심히 history를 쌓은 후 인터넷이 될 때 한 번에 push하면 됩니다.
* 그러나 그 어떤 것 보다 좋은 점은, local repo이기 때문에 내 마음대로 history를 수정할 수 있다는 점입니다!
* 프로젝트 한 개만 열어놓고, branch 사이에 checkout만 받으면 해당 소스가 working directory에 들어옵니다.


##

* Q : DVCS 와 VCS 가 그렇게 다른가요?
* A : 정말 다르다. 거칠게 비유하자면 VCS 는 사실상 전진 후진 기능밖에 없는 툴이라고 봤을 때 DVCS 는 좌회전 우회전, 점프같은 온갖 기능들이 더 들어있는 툴이라고 봐도 무방하다. git 플러그인 중 하나인 git-flow 의 브랜칭 모델을 한번 보면 충분히 VCS 와의 차이점을 실감할 수 있을 듯 하다.


##

* Q : git의 경우 너무 많은 기능이 있는데 저는 다 쓰지도 않을 것 같은데 그냥 svn 이 편하고 좋아요.
* A : 이런 사람들이야 말로 얼른 git 으로 이주해야 할 사람들이다. 많은 기능들을 다 쓰지도 않을 것 같은게 아니라 svn 이 그런 기능을 지원하지 않아서 못 쓰고 있는 것일 뿐이다. 그리고 svn 보다 git 이 훨씬 편하다. 많은 기능이 머리를 아프게 한다면 그냥 git 을 svn 처럼 써도 된다. 그렇게만 사용하더라도 DVCS 의 장점을 어느정도 누릴 수 있다고 본다.<br />*출처: [왜 DVCS를 써야 하는가](http://dalky.tumblr.com/post/43628647400/%EC%99%9C-dvcs-%EB%A5%BC-%EC%8D%A8%EC%95%BC-%ED%95%98%EB%8A%94%EA%B0%80)*

## 

![](img/svn-to-git-1.png)

##

![](img/svn-to-git-2.png)

## SVN -> Git!

[SVN 능력자를 위한 git 개념 가이드](http://www.slideshare.net/einsub/svn-git-17386752)


## Why Forking Workflow?

> Unlike SVN, Git branches are designed to be a fail-safe mechanism for __integrating code__ and __sharing changes__ between repositories."

* 최고의 강점이 바로 이 점입니다. Branch 사이에 머지할 때 3-way merge를 수행하므로 굉장히 신뢰도있는 merge가 이루어집니다.
* 이를 잘 활용할 수 있도록 하는 workflow가 *Forking Workflow* 입니다.

*출처: [Comparing Workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)*

## Yobi!

- Yobi를 이용해서 [Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)로 개발!
- Github와 동일한 방식으로 구현됨<br />
 (Fork:코드 저장소 복사, pull-request: 코드 주고받기)




# Platform개발그룹

## 플랫폼그룹에서<br /> 주로 작업하는 내용은...

- [알고리듬 개발](#algorithm)
- [각 IC별 Core 개발](#ic-cores)
- [선행솔루션 개발](#researches)

## 알고리듬 개발 {#algorithm}

Q: 어떤 IC로?

. . .

- __가장 활발하게 성능 개선이 진행되고 있는 IC에서__ 개발해야 함.
- Incell은 알고리듬 개발에 투입할 인력 여력이 없으니 배제.
- 현재는 mutual의 경우 mms400-core repo의 __mms-458 branch__에서 가장 활발하게 개발되고 있음.
- Hybrid IC가 mainstream이 되면 500(mms500-core repo, master branch)이 알고리듬 개발 브랜치가 되어야 함.

## 각 IC별 Core 개발 {#ic-cores}

- 각 Core에서 개발한 기능 중 다른 Core에 반영해야 할 내용이 있을 수 있으므로 연결된 tree로 관리하면 추후 머지가 용이함.
- 위에서 정한 __알고리듬 개발 repo를 fork해서 개발!__
- 코어 릴리즈는 release branch 및 tag를 push하는 형태로 이루어집니다.


## 선행솔루션 개발 {#researches}

- 선행솔루션 개발에 이용하는 IC repo를 fork해서 시작. Fork 시 __프로젝트 이름 앞에 `dev_`를 붙이도록.__
- e.g. `dev_latency_improve`
- 선행솔루션 개발에 여러 IC가 사용될 수 있음. 이 때는 다른 IC의 repo를 위에서 생성한 repo에 push해서 개발.

## Project 소유자

- 파트장이 자기 파트에서 이루어지는 모든 프로젝트의 소유자가 됩니다.
- 파트장이 모두 할 수 없지요. 해당 프로젝트에 대해 가장 잘 아는 사람, 그래서 소스 반영 여부를 결정할 사람을 *프로젝트 참여자* 로 추가합니다.
- 소유자 및 참여자는 요청받은 소스를 반영할지 여부를 최종적으로 결정할 수 있습니다.
- 예를들어 박찬진 주임이 진행하는 wet touch를 조영원 주임이, 임민우 주임이 진행하는 밀착감 개선 프로젝트를 정준섭 선임이 리뷰합니다.


## Branch 이름

아래 내용은 권장이지 강제는 아닙니다. 로컬 repo는 기본적으로 자기 마음대로~ 개발하셔도 됩니다. 

- `tuning_`: tuning parameter의 변경사항.
- `core_`: 다른 IC에도 모두 반영되어야 하는 공통의 code change.
- `$(platform)_`: 유사한 몇 개의 프로젝트를 포함하는 특정 'platform'에 해당하는 code change. e.g. mms400, lglargescr
- `dev_`: 새로운 기능 개발.
- `bugfix_`: 버그 수정.




# S/W개발그룹

## S/W개발그룹에서<br /> 주로 하는 작업은...

S/W 개발그룹에서 이 프로젝트를 fork 받으셔서 작성해 주세요^^



# 읽을거리...

----------------------

* [Yobi-Git 사용자 매뉴얼](http://dev.melfas.com:9000/jmyl/doc-development-env/post/3) 참조
* [누구나 쉽게 이해할 수 있는 Git 입문](http://backlogtool.com/git-guide/kr/intro/intro1_1.html)
![](img/doc-git-setting.png)
- [SVN에서 Git으로 갈아타기](https://www.atlassian.com/git/tutorials/migrating-overview)
- [Advanced Git Tutorials](https://www.atlassian.com/git/tutorials/advanced-overview)
