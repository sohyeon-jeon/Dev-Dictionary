# [python] concurrent.futures
파이썬에서는 **동시성**을 처리할 때 threading 과 multiprocessing 패키지를 이용했다.  
파이썬 3.2부터는 **concurrent.futures 라이브러리**가 threading,multiprocessing을 위한 api를 제공한다.  
  
## concurrent.futures 
1. 멀티스레딩/멀티프로세싱 API 통일  
2. Promise 개념 도입  
Executor에 의해 패치된 병렬작업은 Future라는 클래스로 매핑된다.  
- Future는 다음과 같은 작업을 진행할 수 있다.
    + 실행중인 병렬 작업을 취소
    + 실행중여부, 완료 여부의 체크
    + 특정 타임아웃 시간 후의 결과값 확인
    + 완료 콜백을 추가  
    + 동기화 코드를 매우 쉽게 작성할 수 있음

### 병렬 처리 API
+ Executor : 병렬작업을 디스패치하며, 새로운 프로세스나 스레드를 자동으로 관리한다.    
+ Future : 디스패치된 병렬 작업을 API를 통해서 완료 여부를 확인하거나 취소할 수 있다.  
+ 모듈함수 : wait(),as_completed() 함수를 통해 병렬처리 결과를 동기화 할 수 있다.

### Executor
**concurrent.futures**에서 실행기라고 불리는 클래스이다.  
스레드/프로세스를 생성하고 작업을 스케줄링한다.  
ThreadPoolExecutor 혹은 ProcessPoolExecutor를 사용하며 API가 똑같이 생겼다.

### submit
``` python
with ThreadPoolExcutor(max_workers=1) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())
```
submit 함수의 리턴값은 병렬로 실행되는 값을 래핑한 future 클래스 객체가 된다.

### map()
**concurrent.futures.Executor.map()** 은 모든 작업의 처리가 완료되면 변환된 결과가 리스트로 리턴된다.  
즉 모든 요소값에 대해서 내부적으로 Future 객체를 생성하고 모든 future에 대해서 result()가 반환될 때 이 결과를 취합하여 전달한다.

### shutdown()
executor에게 종료 시그널을 보내 더 이상 사용하지 않게 됨을 알린다.  
이 메서드가 호출된 실행기는 아직 시작하지 않은 future을 시작하지 않고 취소하며, 이미 진행중인 작업들이 종료될 때까지 기다린다.

### Future
concurrent.futures.Future 비동기로 호출된 함수 콜이 객체로 캡슐화된 형태이다.  
Executor 클래스 인스턴스의 .submit() 호출에 의해 인스턴스가 만들어진다.  
아직 완료되지 않았거나 완료된 작업을 외부에서 객체로 다룰 수 있다. 
+ cancel() : 작업 취소를 시도한다. 만약 현재 실행중이고 취소가 불가능할 경우 False를 리턴한다. 작업이 취소되었다면 True가 리턴된다.
+ canceled() : 취소가 완료된 작업이면 True를 리턴한다.
+ running(): 실행 중인 경우 True를 리턴한다.
+ done(): 작업이 완료되어고 정상적으로 종료되었다면 True를 리턴한다.
+ result(): 해당 호출의 결과를 리턴한다. 만약 작업이 아직 완료되지 않았다면 최대 타임아웃시간까지 기다린다음, None을 리턴한다.
+ exception(): 해당 호출이 던진 예외를 반환한다. 역시 작업이 완료되지 않았다면 타임아웃 시간까지 기다린다.
+ add_done_callback(): 콜백함수를 Future 객체에 추가한다. 이 함수는 future 객체하나를 인자로 받는 함수이다. 콜백은 취소되거나 종료된 경우에 모두 호출된다.

## 모듈 함수
### wait()
wait() 함수는 특정 타임아웃 시간동안 대기한 다음, 그 시간동안 완료된 작업과 완료되지 않는 작업을 구분하여 두 개의 세트로 된 튜플을 리턴한다.
### as_completed()
as_completed()함수는 future 의 집합을 받아서 기다리면서 하나씩 완료되는 것 순서대로 순회하면서 반복하는 반복자를 생성하는 함수이다.  
executor.map() 은 주어진 연속열의 순서대로 결과를 리스트로 만들지만 .as_completed()에서는 결과의 순서가 반드시 주어진 것이 아니며, 실제로 이터레이터는 결과가 아닌 각각의 future 객체를 리턴한다.

## 스레드 vs 프로세스
- **ThreadPoolExecutor** : I/O 기반 작업에 대해서 대기 시간을 줄이고 리소스 사용 효율을 늘리고 싶을 때  
- **ProcessPoolExecutor** : CPU 부하가 많은 분산처리 작업을 할 때  
CPU 로드가 크게 걸리는 작업인 경우에 파이썬에서는 GIL(Global Interpreter Lock) 제약으로 인해 멀티 스레드로는 CPU 분산 처리 효과를 누릴 수 없다.
    - GIL : 여러 개의 스레드가 파이썬 바이트코드를 한번에 하나만 사용할 수 있게 락을 거는 것이다.  
    하나의 스레드만 파이썬 인터프리터를 제어할 수 있는 뮤텍스이다.

### ProcessPoolExecutor
``` Python
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

def load_url(url,timeout):
    with urllib.request.urlopen(url,timeout=timeout) as conn:
        return conn.read()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url={executor.submit(load_url,url,60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
"""
출력 > 
'http://www.bbc.co.uk/' page is 532387 bytes
'http://europe.wsj.com/' generated an exception: HTTP Error 403: Forbidden
'http://www.cnn.com/' page is 1145397 bytes
'http://www.foxnews.com/' page is 282676 bytes
'http://some-made-up-domain.com/' page is 484 bytes
"""
```
### ProcessPoolExecutor
``` Python
import concurrent.futures
import math
 
PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]
 
def is_prime(n):
    if n % 2 == 0:
        return False
 
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True
 
def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
 
if __name__ == '__main__':
    main()
"""
출력 > 
112272535095293 is prime: True
112582705942171 is prime: True
112272535095293 is prime: True
115280095190773 is prime: True
115797848077099 is prime: True
1099726899285419 is prime: False
"""
```




