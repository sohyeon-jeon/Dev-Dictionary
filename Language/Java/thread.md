# Thread
- 또 다른 실행의 흐름을 형성하는 주체  
- 프로세스 내에서 실행되는 흐름

``` Java
package jumpToJava;

public class Sample {
    public static void main(String[] args) {
       Thread ct=Thread.currentThread();
       String name=ct.getName();
       System.out.println(name);
    }
}
// 출력결과 : main
```

### 스레드 실행
``` Java
package jumpToJava;

public class Sample {
    public static void main(String[] args) {
       Runnable task=()->{ //쓰레드가 실행할 내용
           int n1=10;
           int n2=20;
           String name=Thread.currentThread().getName();
           System.out.println(name+": "+(n1+n2));
        };

       Thread t=new Thread(task);
       t.start(); // 스레드 생성 및 실행
        System.out.println("End " +Thread.currentThread().getName());
    }
}
```
<img src="https://www.notion.so/Java-Thread-f9b868e06a314deda5d01d4c8b58984b?pvs=4#82d7cb82770a490bb64aac438906c62b" width="300" hegiht="300">  

스레드는 main 스레드가 마쳤다고 해서 프로그램이 종료되지 않는다.  
모든 스레드가 소멸되야 프로그램이 종료된다.  
생성된 스레드는 자신이 한 일을 마치면 자동으로 소멸된다.
``` java
package jumpToJava;

public class Sample {
    public static void main(String[] args) {
       Runnable task1=()->{ // 짝수 출력
           try{
               for(int i=0;i<20;i++){
                   if(i%2==0)
                       System.out.print(i+" ");
                   Thread.sleep(100); //0.1초간 잠을 잔다.

               }
           }catch (InterruptedException e){
               e.printStackTrace();
           }
        };

        Runnable task2=()->{ //홀수 출력
            try{
                for(int i=0;i<20;i++){
                    if(i%2==1)
                        System.out.print(i+" ");
                    Thread.sleep(100); //0.1초간 잠을 잔다.

                }
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        };

       Thread t1=new Thread(task1);
       Thread t2=new Thread(task2);

       t1.start(); // 스레드 생성 및 실행
        t2.start();
    }
}
```
<img src="https://www.notion.so/Java-Thread-f9b868e06a314deda5d01d4c8b58984b?pvs=4#6aac5927cece4314be520193339c4be1">

**sleep 함수**를 써서 0.1초씩 지연을 줘서 홀수와 짝수 순서대로 나왔지만,  
스레드와 운영체제 상황에 따라 결과가 달라지기 때문에 이 방법은 잘못된 결과로 이어질 수 있다.  
이제 sleep함수를 빼면,  
 ``` java
 package jumpToJava;

public class Sample {
    public static void main(String[] args) {
       Runnable task1=()->{ // 짝수 출력
               for(int i=0;i<20;i++){
                   if(i%2==0)
                       System.out.print(i+" ");
               }
        };

        Runnable task2=()->{ //홀수 출력
                for(int i=0;i<20;i++) {
                    if (i % 2 == 1)
                        System.out.print(i + " ");
                }
        };

       Thread t1=new Thread(task1);
       Thread t2=new Thread(task2);

       t1.start(); // 스레드 생성 및 실행
       t2.start();
    }
```
<img src="https://www.notion.so/Java-Thread-f9b868e06a314deda5d01d4c8b58984b?pvs=4#50db98d89d6347448be826532bd6531a">  
<img src="https://www.notion.so/Java-Thread-f9b868e06a314deda5d01d4c8b58984b?pvs=4#f196980afb694400bf3e2a6a4323607e">

실행 결과가 뒤죽박죽이다. 각각의 스레드는 `독립적`으로 자신의 일을 수행한다.

``` java
package jumpToJava;

class Task extends Thread{
    public void run(){ //Thread의 run 메서드 오버라이딩
        int n1=10;
        int n2=20;
        String name=Thread.currentThread().getName();
        System.out.println(name+": "+(n1+n2));
    }
}
public class Sample {
    public static void main(String[] args) {
        Task t1=new Task();
        Task t2=new Task();
        t1.start();
        t2.start();
        System.out.println("End: "+Thread.currentThread().getName());

    }
}
```
<img src="https://www.notion.so/Java-Thread-f9b868e06a314deda5d01d4c8b58984b?pvs=4#43d7f7ccb4d442ff902310187054dcd2">  
  
## 스레드를 생성하는 방법
---
#1  
1. Runnable을 구현한 인스턴스 생성  
2. Thread 인스턴스 생성  
3. start 메서드 호출  

#2  
1. Thread를 상속하는 클래스의 정의와 인스턴스 생성
2. start 메서드 호출
---  

**스레드 메모리 접근 방식 문제점**

두 스레드가 동일한 변수에 접근하여 변수 값을 1씩 증가시키는 연산을 한다고 가정해보면,  
코어가 여러개일때 `동시에변수의 값을 가져가는 상황`이 발생할 수 있다.  
여러 개의 스레드가 동일한 메모리에 접근해도 문제가 발생하지 않도록 `동기화`를 해야 한다.

``` java
package jumpToJava;

class Counter{
    int count=0;
    synchronized public void increment(){
        count++;
    }
    synchronized public void decrement(){
        count--;
    }
    public int getCount() {return count;}
}

public class Sample {
    public static Counter cnt=new Counter();
    public static void main(String[] args) throws InterruptedException {
        Runnable task1=()->{
            for(int i=0;i<1000;i++)
                cnt.increment();
        };

        Runnable task2=()->{
            for(int i=0;i<1000;i++)
                cnt.decrement();
        };

        Thread t1=new Thread(task1);
        Thread t2=new Thread(task2);
        t1.start();
        t2.start();
        t1.join(); // t1이 참조하는 스레드의 종료를 기다림
        t2.join(); // t2이 참조하는 스레드의 종료를 기다림
        System.out.println(cnt.getCount());

    }
} //결과 출력:0
```
Counter 클래스의 메서드에 `synchronized` 선언을 추가하면 동기화가 이루어진다.

### 동기화 블록
``` java
synchronized public void increment(){
        count++;
        System.out.println("count 값 증가~"); //동기화에 불필요한 문장
        //동기화에 불필요한 문장을 실행하는 중에도 다른 스레드의 접근을 막는다. 이 때 동기화블럭을 사용한다.
    }
```
``` java
package jumpToJava;

class Counter{
    int count=0;
    public void increment(){
        synchronized(this) { //동기화 블럭
            count++; //동기화 필요한 문장
        }
    }
    public void decrement(){
        synchronized(this) {
            count--;
        }
    }
    public int getCount() {return count;}
}

public class Sample {
    public static Counter cnt=new Counter();
    public static void main(String[] args) throws InterruptedException {
        Runnable task1=()->{
            for(int i=0;i<1000;i++)
                cnt.increment();
        };

        Runnable task2=()->{
            for(int i=0;i<1000;i++)
                cnt.decrement();
        };

        Thread t1=new Thread(task1);
        Thread t2=new Thread(task2);
        t1.start();
        t2.start();
        t1.join(); // t1이 참조하는 스레드의 종료를 기다림
        t2.join(); // t2이 참조하는 스레드의 종료를 기다림
        System.out.println(cnt.getCount());

    }
} // 0 출력
```
**this** : 이 인스턴스의 다른 동기화 블록과 더불어 동기화하겠다.  
두 동기화 블록은 둘 이상의 스레드에 의해 동시에 실행될 수 없다.

### 쓰레드 풀
: 스레드의 생성과 소멸은 시스템에 부담을 준다.  
그래서 `쓰레드 풀`을 만들고 그 안에 제한된 수의 스레드를 생성해두고 재활용하는 기술을 활용한다.
```java
package jumpToJava;

import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
public class Sample {
    public static void main(String[] args) {
        Runnable task=()->{
            int n1=10;
            int n2=20;
            String name=Thread.currentThread().getName();
            System.out.println(name+": "+(n1+n2));
        };
        ExecutorService exr=Executors.newSingleThreadExecutor(); // 풀 안에 하나의 스레드만 생성하고 유지
        exr.submit(task); //스레드 풀에 작업을 전달

        System.out.println("End: "+Thread.currentThread().getName());
        exr.shutdown(); // 스레드 풀과 그 안에 있는 스레드 소멸
    }
}
```
```java
package jumpToJava;

import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
public class Sample {
    public static void main(String[] args) {
        Runnable task1=()->{
            String name=Thread.currentThread().getName();
            System.out.println(name+": "+(5+7));
        };
        Runnable task2=()->{
            String name=Thread.currentThread().getName();
            System.out.println(name+": "+(7-5));
        };
        ExecutorService exr=Executors.newFixedThreadPool(2);// 풀 안에 전달된 수의 스레드만 생성하고 유지
        exr.submit(task1); //스레드 풀에 작업을 전달
        exr.submit(task2); //스레드 풀에 작업을 전달
        exr.submit(()->{
            String name=Thread.currentThread().getName();
            System.out.println(name+": "+(5*7));
        });
        
        exr.shutdown(); // 스레드 풀과 그 안에 있는 스레드 소멸
    }
}
```
![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1cb7b116-bd50-4b36-80f0-bb65dcb25420/Untitled.png)

`Executors.newFixedThreadPool(2):` 전달인자가 2이므로 스레드가 2개 존재한다.

### Callable & Future

`Runnable`에 위치한 추상 메서드 run의 반환형이 void이기 떄문에 return문을 통해 반환하는것은 불가능하다.  
이 때 반환하기 위해 `Callable`을 사용한다.
```java
package jumpToJava;

import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Sample {
    public static void main(String[] args)
            throws InterruptedException,Exception{

        Callable<Integer> task=()->{
          int sum=0;
          for(int i=0;i<10;i++)
              sum+=i;
          return sum;
        };

        ExecutorService exr= Executors.newSingleThreadExecutor();
        Future<Integer> fur=exr.submit(task);

        Integer r=fur.get(); //스레드의 반환 값 획득
        System.out.println("result:"+r);
        exr.shutdown();

    }
}
```
### ReentrantLock(synchronized 대신)
```java
package jumpToJava;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.ReentrantLock;

class Counter{
    int count=0;
    ReentrantLock criticObj=new ReentrantLock();

    public void increment(){
        criticObj.lock();

        try{
            count++; // 동기화 문장
        }finally {
            criticObj.unlock();
        }
    }

    public void decrement(){
        criticObj.lock();

        try{
            count--; // 동기화 문장
        }finally {
            criticObj.unlock();
        }
    }

    public int getCount() {return count;}
}
public class Sample {
    public static Counter cnt=new Counter();
    public static void main(String[] args) throws InterruptedException{
        Runnable task1=()->{
            for(int i=0;i<1000;i++)
                cnt.increment();
        };
        Runnable task2=()->{
            for(int i=0;i<1000;i++)
                cnt.decrement();
        };

        ExecutorService exr= Executors.newFixedThreadPool(2);
        exr.submit(task1);
        exr.submit(task2);

        exr.shutdown();
        exr.awaitTermination(100, TimeUnit.SECONDS);
        System.out.println(cnt.getCount());
    }
}
```
`exr.awaitTermination(100, TimeUnit.*SECONDS*);`  
스레드 풀에 전달된 작업을 끝내길 100초간 기다린다.  
shutdown 메서드는 스레드 풀에 전달된 작업이 마무리되면 스레드 풀을 폐쇄하라고 명령만 할 뿐 기다려주지 않는다.  
그래서 스레드 풀에 전달된 작업의 최종 결과를 확인하기 위해서 `awaitTermination`을 사용하여 메서드를 빠져나온다.
