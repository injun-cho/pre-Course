
# cmd 창에서 다음 명령어 입력

## ---------------------------------
## 1. 현재 프로젝트에서 변경사항 추적(버전 관리)를 시작
## ---------------------------------
# 1. git init =  이 명령어를 통해 다음 소스코드에 대한 버전 관리를 하겠다
# 그러면 vs code 의 해당 디렉토리의 영역이 초록색으로 활성화되는 것을 알 수 있다
git init 


# 2. 버전관리를 위한 세팅. 제일 처음 한번만 하면 된다
# 처음 세팅해 놓으면 앞으로 버전 관리할 때 지정한 정보를 사용하게 됨

## ---------------------------------
## 2.1. 개행문자 (NewLine) 설정
## ---------------------------------
## 특정한 문장을 입력하고 나서 엔터를 눌러 줄바꿈 처리를 하듯이, 내부적으로 처리하는 방식이 운영체제마다 다를 수 있기 때문에
## 우리 환경과 조금 다른 환경에서 push 한 코드가 동작할 수 있는 상황을 전제하고 관리해준다는 뜻
## >> 언제든지 우리의 운영체제와 다른 환경에서 프로젝트가 돌아갈 수 있다는 뜻 
## >> auto crlf 라는 게 문제가 없이 돌아갈 수 있도록 자동화해서 운영체제마다 다른 값을 추가/변환해서 관리해준다는 의미

# global 이라는 의미는 전역 옵션이라는 뜻 = 전체 영역에서 사용하겠다 
# -- 의 뜻은 flag 라는 것이며, 세부 옵션을 지정해 준다는 뜻
git config --global core.autocrlf true # 맥OS는 input 으로 입력 

## ---------------------------------
## 2.2. 사용자 정보
## 커밋(버전 생성)을 위한 정보 등록
## ---------------------------------
## git 의 전체 영역에서 쓸 수 있도록 사용자 정보를 등록하는 절차임
## 한가지 주의할 점은 되도록 github 의 유저 정보와 동일하게 해주는 것이 좋겠음
git config --global user.name 'injun-cho' #깃헙 가입한 이름으로 되도록 입력.
git config --global user.email 'injun.cho7@gmail.com' #사용자 매칭 용도로 사용하기 때문에 정확하게 입력

## ---------------------------------
## 2.3. 구성 확인
## ---------------------------------
git config --global --list # 지정한 정보가 잘 등록이 되었는 지 확인

    # 출력값. 종료할 땐 cmd 창에 q 입력
    # core.autocrlf=true
    # user.name=injun-cho
    # user.email=injun.cho7@gmail.com

git status # 

## 이제 버전관리를 위해 파일을 등록을 해줘야 하는데
git add .

## -m 은 버전을 생성하는 건데, 버전의 메시지로 Start Project 를 입력하는 것임
git commit -m 'Start Project'

## commit 을 위해 등록한 버전을 확인해 보려면 git log 을 통해 확인
git log

    # 출력값. commit 의 내역이 잘 등록된 것을 확인할 수 있음
    # commit 6b7fc7d3dd1a9947313e67c7d736fa66a0629224 (HEAD -> master)
    # Author: injun-cho <injun.cho7@gmail.com>
    # Date:   Wed Oct 11 00:26:26 2023 +0900

    #     Start Project

# 이제 깃헙의 원격 주소에 업로드 해줘야 함 
# 깃헙에서 생성한 신규 repository 에 들어가서 원격 주소를 복사해 준다
    # 주소 : https://github.com/injun-cho/pre-Course.git

# 이제 cmd 창에서 원격 저장소를 생성해 줌 
git remote add origin https://github.com/injun-cho/pre-Course.git

# git 명령을 통해 원격 저장소에 우리 프로젝트를 업로드 하려고 하는데 
# 그 업로드 되는 원격 저장소 이름은 origin 이라는 이름이고, 
# master 라는 branch 에 업로드 하겠다 
git push origin master

# 팝업창 로그인을 통하면 잘 업로드가 되는 것을 볼 수 있음


# --------------------------------------

git init

# 모든 파일의 변경 사항을 추적하도록 지정
git add .   

# 변경사항을 추적할 특정 파일({your_file_name})을 지정 >> ex: git add {your_file_name}
# --> 그렇게 되면 stage 상태로 올라가게 됩니다. (글자 색상이 초록색으로 변경) 변경 사항을 추적 중 이라는 의미
git add index.html


# 메시지(-m)와 함께 버전을 생성 
git commit -m '프로젝트 생성' #v1

# 여기서 추가 작업을 하게 되면, 생성/작업한 파일이 빨간색 글씨로 변하게 됨
# 이 때 git add . 하면 더 해줌
git add . 
# --> 이러면 글씨가 빨간색에서 초록색으로 다시 변하게 됨

# 다시 커밋을 해주면서 버전을 만들어 주면 됨
git commit -m 'main.js 추가' #v2

# index.html, main.css 파일을 수정한 경우
# 다시 버전으로 만들고 싶다면
git add .
git commit -m 'index.html 수정' #v3

# 이제 원격 저장소에 우리 프로젝트를 저장하려면
# remote = 외부 환경
# add origin = origin 이라는 별칭을 가진 원격 저장소를 연결. 통상적으로 쓰는 용어이므로 그대로 쓰자
# local <> 원격 저장소(origin) 간 통로가 하나 만들어 진 것임
git remote add origin https://...

# origin 이라는 별칭의 원격 저장소 & master branch 로 버전 내역 전송
git push origin master  



















