# set_cookie 메서드로 토큰 설정했는데 개발자도구 application의 쿠키에는 저장되지 않는 현상

해결하는데 엄청 오래 걸렸다.



크롬의 새 버전 samesite 이슈, SSL 인증서와 https, Django-React cors 이슈 등 많은 것들을 구글링 했다.

가장 뒤통수가 얼얼했던 부분은 set_cookie에 samesite="none" 설정이었다.



잘못된 예시 :

```python
res.set_cookie(
	"access", access, httponly=True, secure=True, samesite=None
)
res.set_cookie(
	"refresh", refresh, httponly=True, secure=True, samesite=None
)
```

위와 같이 samesite=None 설정을 했음에도 불구하고, 힌트메세지는 내가 samesite 설정을 하지 않았기 때문에 SameSite='Lax'로 자동으로 설정되었다고 알려주고 있었다.



한참을 헤매다 set_cookie 메서드를 직접 들여다보았다...

```python
def set_cookie(self, key, value='', max_age=None, expires=None, path='/',
				domain=None, secure=False, httponly=False, samesite=None):
```

위와 같이 기본 None으로 설정되어 있고,

```python
if samesite:
	if samesite.lower() not in ('lax', 'none', 'strict'):
		raise ValueError('samesite must be "lax", "none", or "strict".')
    self.cookies[key]['samesite'] = samesite
```

무려 문자열로 받고 있었다...



올바른 예시 :

```python
res.set_cookie(
	"access", access, httponly=True, secure=True, samesite="none"
)
res.set_cookie(
	"refresh", refresh, httponly=True, secure=True, samesite="none"
)
```

