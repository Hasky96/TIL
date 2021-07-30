# GIT

>Git은 분산버전관리 시스템이다.
>
>코드의 버전이랑 이력을 관리할 수 있다.

### 기본설정

* 윈도우에서 git을 활용하기 위해 git bash를 설치한다.
* 처음 설치 후, 컴퓨터 한테 계정 정보를 입력해야한다.

```bash
$ git config --global user.email '메일주소'
$ got config --global user.name '유저명'
```

* 설정 확인

```bash
$git config --global -l
```

### 로컬 저장소 지정

#### 저장소 초기화

```bash
SSAFY@Haseok MINGW64 ~/Desktop/startcamp/day03

$git init

SSAFY@Haseok MINGW64 ~/Desktop/startcamp/day03 (master)

```

* .git 이라는 숨김파일이 하나 생성된다. -> git과 관련된 모든 정보가 저장된다.
* git  bash에 (master) 라는 문구가 나타난다. -> master 브랜치 라는 뜻

>주의사항
>
>* git으로 관리하고 있는 폴더내에 다시 git init 금지
>* git init 할때 master 떠있으면 절대 git init 금지

### add

* 작업공간의 변경사항 및 수정사항을 git으로 관리하기 위해서 staging area 로 옮기는 것이 필요하다.

```bash
$git add filename
$git add . #current folder 
$git add day01/ #specific folder
```

### commit

* commit은 내 수정사항들, 변경사항들을 확정짓는 명령어.
* create a snapshot
* commit을 작성할때는 반드시, 메시지를 작성해야한다.
* 그 메시지는 어떤 수정 사항이 있었는지 확실하게 작성한다.

```bash
$git commit -m "message"
```

* 커밋 후, status

```bash
$git status
On branch master
nothing to commit, working tree clean
```

* 커밋 후, 커밋 목록들을 확인하기 위해서는

```bash
$ git log
$ git log --oneline
```



## 원격 저장소 (Remote repository)

### 기본설정 (github)

1. 로컬 git 저장소가 있어야 한다.
2. repository 생성해야 한다.
3. repository branch 변경 해줘야 한다. 
   1. main -> master

### 원격 저장소 주소 추가

```bash
$ git remote add <name> <url>
$ git remote add origin url
# origin 이라는 이름으로 저장소 추가// url -> git hub에 있다.
```

### 원격 저장소 목록

```bash
$ git remote -v
# 삭제 remove
$ git remote rm origin
```

### push

* 원격 저장소 업로드 

```bash
$git push -u origin master
```

### pull

* 원격 저장소의 변경사항만 받아옴 ( 업데이트 )

```bash
$ git pull origin master
```

### clone

* 원격 저장소 전체를 복제

```bash
 $ git clone 저장소URL
```

> 주의사항
>
> clone 받은 프로젝트는 이미 git init이 되어있는 상태다.
>
> remote도 추가되어 있는 상태