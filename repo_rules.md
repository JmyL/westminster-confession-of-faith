% Repo 관리방안
% Sungsik Nam
% 2015-08-17

# Development With<br />Yobi & Git

## Centralized Workflow?

* Centralized Version Control System(e.g. SVN)을 활용한 버전관리 방법.
* 서버에 push하려는데 다른 사람이 먼저 push한 내용이 있다면? 내려받아서 merge & resolve한 후, 단일 history로 서버에 업데이트.
* Repository에는 branch 없이 단일 stream이 기록됨.

## Why Forking Workflow?

> "First, it gives every developer their own local copy of the entire project. This isolated environment __lets each developer work independently__ of all other changes to a project—they can add commits to their local repository and __completely forget about upstream developments__ until it's convenient for them."

------------------

> Second, it gives you access to Git’s robust branching and merging model. Unlike SVN, Git branches are designed to be a fail-safe mechanism for __integrating code__ and __sharing changes__ between repositories."

출처: [Comparing Workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)

## Yobi!

- Git을 사용하면서도 centralized workflow로 개발하면 distributed version control system(이하 DVCS)의 장점을 활용하지 못함.
- Yobi를 이용해서 [Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)로 개발!
- Github와 동일한 방식으로 구현됨<br />
 (Fork:코드 저장소 복사, pull-request: 코드 주고받기)

## 관련 글

* [doc-git-setting project](http://dev.melfas.com:9000/platform_g/doc-git-setting/posts) 참조

![](img/doc-git-setting.PNG)




# S/W개발그룹

## S/W개발그룹에서<br /> 주로 하는 작업은...

- 모델 튜닝
- 모델 별 방어코드 개발
- 코어에 반영해야하는 알고리듬 개발 - 특히 S/W 2파트!<br />
(마지막 항목의 경우, platform 개발그룹과 동일한 방법으로 개발하면 됩니다.)


## With Review

개발에 여러사람이 참여하거나 관리자가 리뷰하는 경우,

- Core repo를 __sw_maintainer group 소유로__ fork해서 model repo 생성.
- __개발자는__ 해당 model repo를 개별적으로 fork해서 __비공개 프로젝트를 만든 후 개발.__ 추가 참여자도 마찬가지.
- 개인 비공개 project에는 자유롭게 push할 수 있음.
- __모든 기능은 branch를 생성해서__ 개발하고, 완료되면 push하여 '코드 주고받기'를 통해 sw_maintainer group 소유의 repo에 반영 요청.
- Maintainer가 리뷰하고, comment한 내용이 모두 수정된 시점에 반영.

## Without Review

혼자서 개발하고 관리자로부터 리뷰받지 않는 경우,

- Core repo를 개별적으로 fork해서 __비공개 프로젝트를 만든 후 개발.__
- 개인 비공개 project에는 자유롭게 push할 수 있음.






# Platform개발그룹

## 플랫폼그룹에서<br /> 주로 작업하는 내용은...

- [알고리듬 개발](#algorithm)
- [각 IC별 Core 개발](#ic-cores)
- [선행솔루션 개발](#researches)

<div class="notes">
노트 테스트 ;)
</div>

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
- __Release되지 않은 commit을 개발에 이용하지 않도록 각별히 주의가 필요합니다!__(버전 관리가 되지 않아서 지원이 어려움)


## 선행솔루션 개발 {#researches}

- 선행솔루션 개발에 이용하는 IC repo를 fork해서 시작. Fork 시 __프로젝트 이름 앞에 `dev_`를 붙이도록.__
- e.g. `dev_latency_improve`
- 선행솔루션 개발에 여러 IC가 사용될 수 있음. 이 때는 다른 IC의 repo를 위에서 생성한 repo에 push해서 개발.

## Project 소유자

- platform_maintainer group을 만들어서 각 파트장들을 구성원으로 포함시켜 두었음.
- platform_maintainer 소유로 project를 만들고 그룹공개로 설정해서 __파트장들이 코드의 반영 여부를 최종 승인할 수 있도록__ 했음.
- 다른 platform member들은 참여자로 추가됨. 추가되어있지 않으면 요청 버튼을 눌러서 요청!
- __Core repo의 경우 S/W 개발에서 release branch를 확인해야 하므로 모두 참여자로 추가.__ 역시 추가되어있지 않으면 요청 버튼을 눌러서 요청!

## Branch 이름

아래 내용은 권장이지 강제는 아닙니다. 로컬 repo는 기본적으로 자기 마음대로~ 개발하셔도 됩니다. 

- `tuning_`: tuning parameter의 변경사항.
- `core_`: 다른 IC에도 모두 반영되어야 하는 공통의 code change.
- `$(platform)_`: 유사한 몇 개의 프로젝트를 포함하는 특정 'platform'에 해당하는 code change. e.g. mms400, lglargescr
- `dev_`: 새로운 기능 개발.
- `bugfix_`: 버그 수정.


# 읽을거리...

----------------------

- [SVN에서 Git으로 갈아타기](https://www.atlassian.com/git/tutorials/migrating-overview)
- [Advanced Git Tutorials](https://www.atlassian.com/git/tutorials/advanced-overview)
