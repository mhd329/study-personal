# Promise?

1. 자바스크립트는 비동기 처리를 위해 콜백 함수를 사용한다.

   - 남발하게 되면 콜백 지옥에 빠지게 된다.
   - 프로미스를 사용함으로써 다음과 같이 복잡성을 해소할 수 있다.
     1. 비동기 처리 시점을 명확하게 표현할 수 있다.
     2. 연속된 비동기 처리 작업을 수정, 삭제, 추가하기 편하고 유연하다.
     3. 비동기 작업 상태를 쉽게 확인할 수 있다.
     4. 코드의 유지 보수성이 증가한다.

2. Promise는 어떤 작업의 결과값이 아니다.

   - 하지만 결과값 처럼 취급할 수 있다.
     - 말 그대로 결과값을 보장하겠다는 약속이다.
   - 비동기 결과로 만들어지는 Promise 변수 그 자체는 비동기 코드 호출과 동시에 받을 수 있다.
     - Promise를 받는 코드는 동기적인 코드이다.
   - 실제로 우리가 받을 것이라고 예상하고 있는 값은 실제로는 받지 못한 상태이지만, 그 값을 받겠다는 Promise 객체를 가지고 마치 받은 것 처럼 쓰면 된다.
     - 마지막 단계에 값을 잘 처리해서 쓰면 된다.

3. Promise method chaining

   ```
   fetch('http://example.com/api')
       .then((response) => {
       	return response.json();
       }).then((data) => {
       	console.log("fulfilled");
       	console.log(data);
       }).catch((error) => {
       	console.log("rejected");
           console.log(error);
   	});
   ```

   - fetch 함수는 결과로 Promise 객체를 반환한다.
   - 위와 같이 Promise 콜백 함수에서 반환된 값은 다음으로 연결된 콜백 함수의 인자값이 된다.
   - Promise 메서드 안쪽 콜백의 실행결과에 따라 Promise는 둘 중 하나의 상태로 귀결된다.
     - fulfilled: 비동기 처리가 성공적으로 진행되었다는 뜻이다.
     - rejected: 비동기 처리가 실패했다는 뜻이다.

---

참조 : https://velog.io/@vraimentres/promise-1

부분 참조 : https://yoo11052.tistory.com/155