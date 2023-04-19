## [C] call by value
- 인자로 전달되는 변수를 함수의 매개변수에 복사한다.  
이렇게 복사되면 서로 별개의 변수가 되며, 매개변수를 변경해도 원래의 변수에는 영향이 가지 않는다.
``` c
#include <stdio.h>

void swap(int a, int b)
{
	int temp;
	
	temp = a;
	a = b;
	b = temp;
}

int main()
{
	int a, b;
	
	a = 10;
	b = 20;
	
	printf("swap 전 : %d %d\n", a, b);
	
	swap(a, b);
	
	printf("swap 후 : %d %d\n", a, b);
	
	return 0;
}
'''
전 : 10 20
후 : 10 20
-> 변경 안됨.
```

## [C] call by reference
- 함수에 값을 전달하는 대신, 주소를 전달하는 방식이다.  
c언어는 기본적으로 call by value이고, call by reference를 공식적으로 지원하지는 않는다.  
하지만 포인터를 이용해 주소값을 넘겨주어 call by reference를 구현할 수 있다.
``` c
#include <stdio.h>

void swap(int *a, int *b)
{
	int temp;

	temp = *a;
	*a = *b;
	*b = temp;
}

int main()
{
	int a, b;

	a = 10;
	b = 20;

	printf("swap 전 : %d %d\n", a, b);

	swap(&a, &b);

	printf("swap 후 : %d %d\n", a, b);

	return 0;
}
'''
전 : 10 20
후 : 20 10
-> 변경 됨.
'''
```

## [Python] 
- 파이썬은 어떤값을 전달하느냐에 따라 call by value, call by reference가 나눠진다.  
파이썬의 자료형에는 불변(immutable)과 가변(mutable)이 있다.  
불변의 객체를 넘기면 call by value이고, 가변의 객체를 넘기면 call by reference이다.  
그 이유는 파이썬은 모든 것이 객체이기 때문이다.  
int타입의 변수를 함수의 인자로 넘기면 불변 객체이기 때문에, 함수 안에서는 새로운 값을 생성한다.  
가변 객체는 새로운 값을 만들 필요가 없기 때문에 주소값이 복사되어 call by reference로 보인다. 

## [java]
- Java에서는 모든 것이 객체이기 때문에, 함수 호출 시 값이 복사되어 전달되는 Call by value 방식이 적용됩니다. 즉, 함수 인자로 전달된 객체의 값이 복사되어 함수 내부에서 변경되어도 호출한 측에서는 변경되지 않습니다. 따라서, Java에서는 Call by reference 방식이 적용되지 않습니다.

그러나, Java에서는 객체를 참조하는 변수(레퍼런스)가 존재합니다. 이 변수는 객체의 주소를 가리키는 포인터와 유사한 역할을 하며, 이 변수를 함수 인자로 전달하면 객체의 주소값이 복사되어 전달됩니다. 이 때문에 가변 객체의 경우, 객체 내부의 상태를 변경할 수 있으며, 이 변경된 상태는 호출한 측에서도 반영됩니다. 하지만, 이는 Call by reference 방식이 적용되는 것이 아니라, Call by value 방식이 적용되면서 객체의 참조값이 복사되어 전달되는 것입니다.

따라서, Java에서는 모든 경우에 Call by value 방식이 적용되지만, 가변 객체의 경우 객체의 참조값이 복사되어 전달되기 때문에 함수 호출 시에는 Call by reference와 유사한 결과를 볼 수 있습니다.


``` java

import java.util.ArrayList;

public class Sample {
    //call by value
    public static void swap(int a,int b){
        int temp=a;
        a=b;
        b=temp;
    }

//    call by refence처럼 보이는?
    public static void addData(ArrayList array,int num){
        array.add(num);
    }

    public static void main(String args[]) {
        int a=1;
        int b=2;
        swap(a,b);
        System.out.println(a);
        System.out.println(b);

        ArrayList<Integer> arr=new ArrayList<>();
        arr.add(1);

        addData(arr,2);
        System.out.println(arr);
    }
    }
```