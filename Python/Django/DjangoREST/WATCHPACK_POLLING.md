# Docker 사용 시 로컬에서의 변경사항을 다시 빌드하지 않고 컨테이너 내부에 바로 적용시키기

부재 : "WATCHPACK_POLLING=true" 에 대한 고찰

---

관련 웹 문서 참조 목록 : 

1. https://github.com/facebook/create-react-app/issues/10253
2. https://stackoverflow.com/questions/65359786/hot-reload-stopped-working-after-adjusting-environment-for-work-requirements
3. https://dreaminggore00.tistory.com/18

------

1. 수강중인 도커 강의에서 '로컬에서 업데이트되는 사항을 컨테이너 내부에 바로 적용하는 방법' 으로 volume과 도커 컴포즈를 활용하였다.
2. 기본적으로 로컬에 있는 파일들을 도커 컨테이너 내부로 옮겨 컨테이너 내부에서 돌리는 것인데,
3. 볼륨을 활용하여 **컨테이너 내부에서 로컬에 있는 파일들을 참조하게 만들어서** 로컬에서 변경사항이 생겨도 컨테이너에 바로 반영이 되게 하는 것이었다.
4. 도커 컴포즈를 활용하여 yml파일을 만들고 강의에서 하라는 그대로 했다.
5. 다른 연습용 프로젝트에 적용했던 내용을 그대로 이번 리액트 프로젝트에도 적용하여 실습해봤지만 **이번에는 업데이트가 되지 않고 있었다**.
6. 원인을 찾기가 힘들어서 일단 해결법을 먼저 찾기로 했다.

해결법 : package.json의 start 스크립트를 수정한다.

```
"scripts": {
	...
	"start": "WATCHPACK_POLLING=true react-scripts start",
	...
}
```

---

우선 **"WATCHPACK_POLLING=true"**가 무엇을 의미하는 것이며,

왜? 변경에 대한 감지가 가능해졌는지 찾아보았다.



- 기본적으로 웹팩은 파일 시스템의 변경사항을 감지하기 위해 파일시스템의 이벤트를 사용한다.
- 일부 특수한 환경에서는 감지되지 않을 수 있다.
- 그런 경우에는 polling 방식을 사용하여 감지할 수 있다.



즉, **"WATCHPACK_POLLING=true"**는 웹팩 파일시스템의 변경 감지 방식을 폴링 방식으로 감지하겠다고 설정하는 것이다.



그럼 왜 폴링 방식으로 감지가 되었을까? 폴링 방식이 무엇인지 찾아보았다.



- 폴링은 요약하자면 어떤 상태나 이벤트를 주기적으로 확인하기 위해 반복적으로 검사하는 방식이다.
- 일정 주기를 가지고 반복적으로 검사를 한다.
- 검사 주기를 가지기 때문에 실시간으로 감지하는 것에는 제한이 있을 수 있다.
  - 주기를 짧게 하면 실시간으로 감지하는 것 처럼 보이게 할 수는 있다.
  - 그만큼(주기에 따라) 자원의 소비(CPU 리소스, 네트워크 트래픽)가 많아진다.
- 위 설정의 경우 기본 주기는 100ms라고 한다.



주기마다 한 번씩 검사를 하는 방식이기 때문에 변경이 없는 경우 비효율적인 방식이 될 수 있다.

또한 프로젝트의 규모가 커질 경우 적절한 주기를 설정하지 않으면 상당한 자원의 소모가 있겠다고 생각한다.



- 그렇다면 많은 자원을 소모하지 않으면서 실시간 업데이트를 가능하게 하는 방법도 있을까?



사실 이것은 좋은 방식은 아니라고 한다.

스택 오버플로우의 답변자는 해결책을 제시함과 동시에 하나의 조언도 하고 있었다.

---

> The Dockerfile you have is great for when you want to package your app into a container, ready for deployment. It's not so good for development where you want to have the source outside the container and have the running container react to changes in the source.
>
> What I do is keep the Dockerfile for packaging the app and only build that, when I'm done.

---

말인즉 **개발이 끝나고 배포 준비단계에 있는 앱을 도커 컨테이너에 넣으라는 소리**였다.

소스를 컨테이너 바깥에 두고 변경을 할 때, 실행중인 컨테이너 내부에 있는 것도 같이 실시간으로 반응하게 하는것은 개발에 있어서 별로 좋지 않다고 한다.

어쨌든 **모든 작업이 완료되었을 때 빌드**하라고 한다.



생각해보면 그 말이 맞는 것 같기도 하다. 굳이 자원을 소모해가면서 도커 내부와 로컬을 연결해놓을 필요가 어디 있을까 싶다.