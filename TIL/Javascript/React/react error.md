# error:0308010C:digital envelope routines::unsupported 해결

npm audit fix --force 이후에 npm start를 하니 아래와 같은 에러코드가 뜨면서 실행이 안됬다.



```
Error: error:0308010C:digital envelope routines::unsupported
    at new Hash (node:internal/crypto/hash:71:19)
    at Object.createHash (node:crypto:133:10)
    at module.exports (F:\GitHub_management\projects\react-todo\node_modules\webpack\lib\util\createHash.js:90:53)
    at NormalModule._initBuildHash (F:\GitHub_management\projects\react-todo\node_modules\webpack\lib\NormalModule.js:386:16)
    at F:\GitHub_management\projects\react-todo\node_modules\webpack\lib\NormalModule.js:418:10
    at F:\GitHub_management\projects\react-todo\node_modules\loader-runner\lib\LoaderRunner.js:367:11
    at F:\GitHub_management\projects\react-todo\node_modules\loader-runner\lib\LoaderRunner.js:233:18
    at context.callback (F:\GitHub_management\projects\react-todo\node_modules\loader-runner\lib\LoaderRunner.js:111:13)
    at F:\GitHub_management\projects\react-todo\node_modules\babel-loader\lib\index.js:51:103 {
  opensslErrorStack: [ 'error:03000086:digital envelope routines::initialization error' ],
  library: 'digital envelope routines',
  code: 'ERR_OSSL_EVP_UNSUPPORTED'
}

Node.js v18.16.0
```



**현재 Node.js 최신 버전을 사용하고 있다는 것을 알 수 있다.**

구글링하여 원인을 찾았다.



참조 : https://velog.io/@abc2752/error-0308010C-digital-envelope-routines-unsupported



원인 요약 :

**Webpack 빌드 프로세스에는** **MD4 알고리즘이 사용**되는데,

**최신 Node.js 버전에서는 MD4 알고리즘이 더 이상 지원되지 않기 때문에** 발생하는 문제였다.

즉, 최신 버전의 Node.js와 기존 Webpack의 버전 간 차이로 인해 발생하는 **호환성 이슈**였던 것이다.

(무턱대고 최첨단 버전을 사용하는게 이래서 안좋다. 가급적 스테이블 버전을 쓰자.)



이와 관련하여 아래와 같은 해결책을 찾았다.



참조 : https://www.datainfinities.com/49/error-0308010C-digital-envelope-routines-unsupported

 

해결책 요약 :

**package.json 파일**에 다음의 **명령어**를 자신의 **개발 환경에 맞게 입력**해주면 된다.



```json
# for macOS, Linux or Windows Git Bash
export NODE_OPTIONS=--openssl-legacy-provider

# for Windows CMD (Command Prompt)
set NODE_OPTIONS=--openssl-legacy-provider

# for Windows PowerShell
$env:NODE_OPTIONS="--openssl-legacy-provider"

# for Docker (in your Dockerfile)
ENV NODE_OPTIONS="--openssl-legacy-provider"
```



나는 윈도우 환경에서 사용중이기 때문에 아래와 같은 상태에서,



```json
"scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    ...
  },
```



이렇게 바꿔서 해결했다.



```json
"scripts": {
    "start": "set NODE_OPTIONS=--openssl-legacy-provider && react-scripts start",
    "build": "set NODE_OPTIONS=--openssl-legacy-provider && react-scripts build",
    ...
  },
```



의문점 :

참고한 공식 문서에서는 해결법으로 아래와 같이 작성하라고 지시하고 있다.



```json
{
  "scripts": {
    "start": "react-scripts start --openssl-legacy-provider",
  }
}
```



1. 그런데 이렇게 작성하면 실행이 안된다.
   - --openssl-legacy-provider 부분을 앞으로 빼면 터미널에서 명령어 인식을 못한다.
2. 그리고 빌드와 관련해서 발생하는 문제인데 왜 start부분만 바꾸라고 지시하고 있는지도 모르겠다.
   - 위 처럼 build부분을 빼고 start만 수정해도 잘 켜지긴 한다.