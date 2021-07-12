# 뉴편함

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F5cd36d40-30e4-46b1-89b3-261c9efd3db6%2F_2021-03-04__8.50.01.png?table=block&id=403e59bc-7568-42c1-a6a9-1831bb36c59d&spaceId=a07b9679-e55c-4b34-ad51-a4e7fac6c83a&width=6440&userId=&cache=v2)

## 설명

메일링서비스 춘추전국시대로써 정작 어떤 메일링서비스가 있는지 찾아보기는 쉽지가 않습니다.

"모든 뉴스레터 서비스를 한눈에 모아 볼수있게끔 만들어보면 어떨까?"하는 생각에 프로젝트를 진행하게 되었습니다.

종합반과 플러스 강의의 커리큘럼속에 있는 기능들을 사용해 원하는 기능들을 구현할 수있게 초점을 맞추며 기본적인 CURD(추가,업데이트,리스트,삭제)를 만들기위해 노력했습니다.

## 서비스설명

- 진자2 템플릿 엔진을 이용한 화면구현
- 랜덤새로고침
- 회원가입과 JWT토큰을 사용한 로그인, 로그아웃
- 검색기능
검색키워드가 없을시 차단,비어있는 채로 검색시 차단
- 뉴스레터별로 코멘트 저장 및 보기, 좋아요, 싫어요 기능을 회원각자 저장할수있게 끔 만들어줌
- 비로그인시 차단(유효성체크)
- 새로운 뉴스레터 저장(추가)
    나홀로메모장에서 배운 것을 활용해 크롤링등의 기능을 만듦

## 기술스택
- 파이썬
- mongoDB
- aws


## 서비스설명

- 진자2 템플릿 엔진을 이용한 화면구현
- 랜덤새로고침
- 회원가입과 JWT토큰을 사용한 로그인, 로그아웃
- 검색기능
검색키워드가 없을시 차단,비어있는 채로 검색시 차단
- 뉴스레터별로 코멘트 저장 및 보기, 좋아요, 싫어요 기능을 회원각자 저장할수있게 끔 만들어줌
- 비로그인시 차단(유효성체크)
- 새로운 뉴스레터 저장(추가)

    나홀로메모장에서 배운 것을 활용해 크롤링등의 기능을 만듦

## Q&A

- **회원의 뉴스레터 칼럼 속  코멘트와, 좋아요, 숨김기능을 어떻게 만들었나요?**

     추가시 몽고디비 명령어안 push를 사용

    ```python
    #좋아요
    db.user.update_one({"email": payload['email']}, {"$push": {"like": title_receive}})

    ```

    삭제시 몽고디비 명령어안 pull을 사용

    ```python
    #안좋아요
    db.user.update_one({"email": payload['email']}, {"$pull": {"like": title_receive}})
    ```

    딕셔너리 형태로 들어간것을 확인할수있다(5elements)

    ![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F4ef2b786-10ed-4b03-8342-0033e6ec2729%2F_2021-03-05__9.50.04.png?table=block&id=f8247699-78cf-462d-89ae-619f7c714cce&spaceId=a07b9679-e55c-4b34-ad51-a4e7fac6c83a&width=2540&userId=&cache=v2)

    ![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbf464e82-1f18-4c7b-afd9-cc4fb187636d%2FKakaoTalk_Photo_2021-03-05-09-51-45.png?table=block&id=f81867a1-81ca-452d-9122-6b12cecf247b&spaceId=a07b9679-e55c-4b34-ad51-a4e7fac6c83a&width=1890&userId=&cache=v2)

- **검색어를 완전히 치지않고 검색어 출력을 했는데 어떻게 하셨나요?**

    jinja2템플릿엔진으로 목록출력을 해주었기 때문에 ajax를 사용할 수가없어서 ajax는 사용하지 않았습니다.

    if문에 includes를 사용해 검색키워드만 검색을 할수있습니다

    ```python
    if (letter.includes(newsletterVal)) {
    ```

- **랜덤 새로고침 기능의 구현방법은 어떻게 되나요?**

    ![](https://images.velog.io/images/chocho/post/8395ff06-1369-468e-8bbf-f9481198ef9a/KakaoTalk_Photo_2021-03-10-07-38-35.gif)

    db에서 섞어서 가져오는법.

    db에서 그대로 가져와 앞단에서 섞어서 출력해주는 두가지 방법이 있을텐데, 저희는 후자를 사용하였고. 몽고db의 명령어 find대신 aggregate를 사용하고 sample속성을 사용해 구현했습니다.

    ```python
    newsletters = list(db.newsletters.aggregate([{'$sample': {'size': 8}}, {'$project': {'_id': False}}]))
    ```


### 회원가입
![](https://images.velog.io/images/chocho/post/7457a998-c2a5-4b61-aa4a-204db778b3ab/KakaoTalk_Photo_2021-03-10-07-38-31.gif)

### 전체적
![](https://images.velog.io/images/chocho/post/7457a998-c2a5-4b61-aa4a-204db778b3ab/KakaoTalk_Photo_2021-03-10-07-38-31.gif)

# 데모영상(yes설명)

<a href="https://youtu.be/OGOOvSASANE" >유튜브 영상👌으로 보실 수 있습니다.</a>


---

[작성자의 노션](https://www.notion.so/6fd086d87ec54a1fa3a106d901e9b04d#119a564cdd5843a2a03d2bc0ac3103ca)