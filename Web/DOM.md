### DOM(문서 객체 모델) 
- 웹 페이지(HTML,XML)의 콘텐츠를 계층적인 구조(트리 구조)로 표현하며, 이를 프로그래밍 언어가 해당 문서에 접근하여 조작할 수 있도록 API 제공한다.
- 브라우저는 HTML을 파싱하여 DOM을 생성하고, 이를 사용하여 웹 페이지를 조작하고 업데이트 한다.
- HTML은 웹 페이지를 설계하고 작성하는 언어이고, DOM은 웹 페이지를 동적으로 조작하고 변경하는데 사용하는 프로그래밍 인터페이스이다.
- DOM은 뷰 포트에 무엇을 렌더링 할지 결정되기 위해 사용한다. 페이지의 콘텐츠 구조 그리고 자바스크립트에 의해 수정되기 위해 사용한다.

### HTML DOM과 REACT DOM
- HTML DOM은 웹 페이지를 동적으로 변경하기 위한 웹 표준이고, REACT DOM은 JS 라이브러리인 REACT를 사용하여 만들어진 가상 DOM이다.
- HTML DOM은 브라우저가 웹 페이지를 로드하고, 이를 해석하여 생성하는 객체 모델이다. HTML DOM은 브라우저에서 기본적으로 제공하는 객체 모델이기 때문에, 별도 라이브러리나 프레임워크 없이 사용할 수 있습니다.
- REACT DOM은 REACT 라이브러리를 사용하여 만들어진 가상 DOM입니다. REACT DOM은 실제 DOM과 동기화되어, REACT 컴포넌트에서 변경된 부분만 업데이트하고 렌더링합니다.
- 따라서, HTML DOM은 기본적인 웹 페이지 조작에 적합하고, React DOM은 React를 사용하여 성능을 최적화하고, 재사용 가능한 UI 컴포넌트를 만들 때 유용합니다.

# REACT 동작원리
REACT는 상태나 속성이 변경되면, 해당 컴포넌트의 render()함수를 호출하여 새로운 UI를 생성한다. 이 새로운 UI는 REACT 가상 DOM에 반영된다.  
**이전 가상 DOM과 현재 가상 DOM을 비교**하여, 변경된 요소만을 파악하여 **실제 DOM에 반영**한다.  
불필요한 DOM 조작을 최소화하고, 웹 어플리케이션 성능을 향상시킨다.


