# pyspark
- 파이썬에서 rdd가 느린 이유 : 파이썬 객체를 자바 객체로 변환하고 다시 자바 객체를 파이썬 객체로 변환하는 과정에서 오버헤드가 생긴다.  

- outer와 semi join 비교 : 세미 조인은 일치하는 행의 정보만 반환하고, 외부 조인은 완전한 결과 집합을 반환. 

- GROUP BY는 데이터를 그룹화하여 집계를 계산하는데 사용되고, Window 함수는 각 행에 대한 특정 범위 내에서의 집계를 계산하는데 사용됩니다.

- pyspark udf는 row 형식으로 데이터가 전송되고 py4j를 사용하여 jvm에서 실행한다. 그래서 데이터 전송에 따른 오버헤드가 있을 수 있다.  
pyspark pandas udf는 pyspark에서 pandas 데이터프레임으로 변환되어 전달된다. 이후 사용자 정의 함수가 로컬에서 pandas 데이터 프레임에 적용되며 결과가 다시 pyspark dataframe으로 변환되어 반환된다. pandas udf는 각 파티션에서 로컬로 함수를 실행하기 때문에 데이터 이동이 최소화되고 pyspark udf보다 성능이 높을 수 있다. 즉 pyspark udf는 클러스터모드에서 분산 처리하고 pandas udf는 로컬에서 각 파티션을 병렬로 처리한다.




