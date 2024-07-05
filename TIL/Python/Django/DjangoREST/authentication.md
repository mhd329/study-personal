# Django 기본 인증 클래스 커스텀.

했던 고민들 :

 

1. 클라이언트가 낡은 액세스토큰을 서버로 던져주었을 때 어떤 반응이 오나 궁금해서 액세스토큰 수명을 1초로 해놓고 주어봤다.
2. 사전에 설정해놓은대로 만료된 토큰은 인증에서 통과하지 못했다.
3. 그런데 인증에 실패하였다는 의미의 응답을 하긴 하는데, 내가 원하는 형태로 하지 않았기 때문에 커스터마이징 하고싶었다
   - 기존에 모든 반환되는 예외들을 error.response.data.message라는 구조로 통일했었는데 반환되는 구조가 달랐고,
   - 사용자들에게 한글 메세지로 알려주고 싶었다.
4. 처음에는 단순히 특정 경우에 대한 예외만 정의해주면 되나 싶어서 try, except문을 사용하여 클래스 view 내부 메서드에서 처리할 수 있겠다 싶었다.
5. 그런데 동작 과정이 내가 생각한것과 조금 달랐다. 어떤 요청을 처리하는 클래스 내부 메서드(def get, def post 등)에서 try, except를 처리하면 되겠다 싶었는데, 요청이 거기로 도달하기도 전에 어딘가에서 먼저 요청을 받고 검증을 한 다음 응답을 하고 있었다
   - 각 메서드 최상단에서 print 시켜봤지만 들어오지 않는 것을 확인했다.
6.  찾아보니 미들웨어가 먼저 실행되면서 미들웨어에서 인증과 허가 과정을 넣어주면 된다고 하길래 미들웨어를 커스텀하여 사용해보았다.
7. 미들웨어를 커스텀하니 내 의도대로 응답이 만들어져서 반환되는 것을 확인하였다. 그러나 클라이언트에서 에러메세지를 확인하니 여전했다.
   - 미들웨어를 거친 다음 다시 하나의 절차가 또 있는 것처럼 보였다.
8. 내가 지금 하려는 일이 무엇인가 생각했다. 인증과 허가에 관련된 부분 중 인증에 관련된 내용을 커스텀하고 싶었다.
   - 그렇다면 settings.py에 뭔가 인증에 관련된 설정을 해주는 부분이 있다고 생각해서 쭉 찾았다.
9. 보다보니 REST_FRAMEWORK에 기본 허가 클래스와 기본 인증 클래스를 설정해준 것이 보였다. djangoRESTframework 처음 설치 적용할 때 REST_FRAMEWORK 라는 설정을 해준 것이 생각났다.
10. 해당 경로(rest_framework_simplejwt/authentication.py)로 들어가서 인증 과정이 어떻게 되어있는지 코드를 확인했다.
    - 인증 과정에는 JWTAuthentication이라는 인증 클래스가 메인으로 있고, 그 클래스 내부에 인증을 담당하는 메서드로 authenticate 메서드가 있었다.
    - 토큰 관련된 부분을 처리하는 내부 메서드로 get_validated_token라는 메서드를 사용하고 있었다.
11. 객체 형태로 반환되는 에러메세지의 구조가 클라이언트 콘솔로 확인한 구조와 일치했다. 그렇다면 이 클래스를 상속받은 커스텀 클래스를 만들고 인증때 내가 커스텀한 메서드를 사용하게끔 하면 되지 않겠나 싶었다.
12. 일단 settings.py에 REST_FRAMEWORK에 기본 허가 클래스와 기본 인증 클래스를 하나씩 지워보면서 클라이언트에서 어떻게 작동하나 확인했다.
13. 기본 인증클래스를 지워버리니 내가 사전에 정의한 예외들이 출력되고 있었다. 기본적으로 인증 및 예외처리 해주는 클래스가 없으니 각 경우에 대해 모두 별도로 처리해줘야 하고 거기에 내가 정의한 방식이 쓰이는 것처럼 보였다.
14. 결국 기본 인증 클래스를 커스텀 하는 것으로 문제가 해결되었다.

---

```python
REST_FRAMEWORK = {
	"DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
	"DEFAULT_AUTHENTICATION_CLASSES": (
		# "rest_framework_simplejwt.authentication.JWTAuthentication",
		"config.authentication.CustomJWTAuthentication",
	),
}
```

------

1. 프로젝트 이름/원하는 파일 이름.py 로 파일을 하나 만듦



![img](https://blog.kakaocdn.net/dn/dcH6Fz/btsjwrRJU7v/T0JL4RRR8tj2Y1gttE0OY1/img.jpg)



2. JWTAuthentication의 authenticate와 get_validated_token을 재정의

```python
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.authentication import (
    JWTAuthentication,
    InvalidToken,
    TokenError,
)


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            print("header is None")
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            print("raw_token is None")
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token

    def get_validated_token(self, raw_token):
        messages = []
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                return AuthToken(raw_token)
            except TokenError as e:
                messages.append(
                    {
                        "token_class": AuthToken.__name__,
                        "token_type": AuthToken.token_type,
                        "message": e.args[0],
                    }
                )
        # 수정이 필요한 부분은 이 부분이었다.
        raise InvalidToken(
            {
                "detail": messages,
                "message": "유효하지 않은 토큰입니다.",
            }
        )
```