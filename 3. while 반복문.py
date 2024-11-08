while 반복문을 공부해보자!


문장을 반복해서 수행해야 할 경우 while 문을 사용한다. 그래서 while 문을 ‘반복문’이라고도 부른다.

while 문의 기본 구조
while 조건문:
    수행할_문장1
    수행할_문장2
    수행할_문장3
while 문은 조건문이 참인 동안 while 문에 속한 문장들이 반복해서 수행된다.

열 번 찍어 안 넘어가는 나무 없다’라는 속담을 파이썬 프로그램으로 만들면 다음과 같다.
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다.

  위 예에서 while 문의 조건문은 treeHit < 10이다. 즉, treeHit가 10보다 작은 동안 while 문에 포함된 문장들을 계속 수행한다. 
whlie문 안의 문장을 보면 가장 먼저 treeHit = treeHit + 1로 treeHit 값이 계속 1씩 증가한다는 것을 알 수 있다. 
그리고 나무를 treeHit번만큼 찍었다는 것을 알리는 문장을 출력하고 treeHit가 10이 되면 "나무 넘어갑니다.
"라는 문장을 출력한다. 그러고 나면 treeHit < 10 조건문이 거짓이 되므로 while 문을 빠져나가게 된다.

treeHit = treeHit + 1은 프로그래밍을 할 때 매우 자주 사용하는 기법이다. treeHit 값을 1만큼씩 증가시킬 목적으로 사용하며 treeHit += 1처럼 작성해도 된다.

다음은 while 문이 반복되는 과정을 순서대로 정리한 표이다. 이렇게 긴 과정을 소스 코드 단 5줄로 만들 수 있다니 놀랍지 않은가?

treeHit	조건문	조건 판단	수행하는 문장	while문
0	0 < 10	참	나무를 1번 찍었습니다.	반복
1	1 < 10	참	나무를 2번 찍었습니다.	반복
2	2 < 10	참	나무를 3번 찍었습니다.	반복
3	3 < 10	참	나무를 4번 찍었습니다.	반복
4	4 < 10	참	나무를 5번 찍었습니다.	반복
5	5 < 10	참	나무를 6번 찍었습니다.	반복
6	6 < 10	참	나무를 7번 찍었습니다.	반복
7	7 < 10	참	나무를 8번 찍었습니다.	반복
8	8 < 10	참	나무를 9번 찍었습니다.	반복
9	9 < 10	참	나무를 10번 찍었습니다. 나무 넘어갑니다.	반복
10	10 < 10	거짓		종료

while 문 만들기
이번에는 여러 가지 선택지 중 하나를 선택해서 입력받는 예제를 만들어 보자. 먼저 다음과 같이 여러 줄짜리 문자열을 만들자.

prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number: """
이어서 number 변수에 0을 먼저 대입한다. 이렇게 변수를 먼저 설정해 놓지 않으면 다음에 나올 while 문의 조건문인 number != 4에서 변수가 존재하지 않는다는 오류가 발생한다.

number = 0
while number != 4:
    print(prompt)
    number = int(input())
1. Add
2. Del
3. List
4. Quit
Enter number:

while 문을 보면 number가 4가 아닌 동안 prompt를 출력하고 사용자로부터 번호를 입력받는다. 다음 결과 화면처럼 사용자가 값 4를 입력하지 않으면 계속해서 prompt를 출력한다.
여기에서 number = int(input())는 사용자의 숫자 입력을 받아들이는 것이라고만 알아 두자. int나 input 함수에 대한 내용은 뒤에 나오는 내장 함수 부분에서 자세하게 다룬다.

Enter number:
1

1. Add
2. Del
3. List
4. Quit

Enter number:
4
>>>


while 문 강제로 빠져나가기
while 문은 조건문이 참인 동안 계속 while 문 안의 내용을 반복적으로 수행한다. 하지만 강제로 while 문을 빠져나가고 싶을 때가 있다.

예를 들어 커피 자판기를 생각해 보자. 자판기 안에 커피가 충분히 있을 때 동전을 넣으면 커피가 나온다. 그런데 자판기가 제대로 작동하려면 커피가 얼마나 남았는지 항상 검사해야 한다. 
만약 커피가 떨어졌다면 판매를 중단하고 ‘판매 중지’ 문구를 사용자에게 보여 주어야 한다. 이렇게 판매를 강제로 멈추게 하는 것이 바로 break 문이다.

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

money가 300으로 고정되어 있고 while money:에서 조건문인 money는 0이 아니기 때문에 항상 참이다. 따라서 무한히 반복되는 무한 루프를 돌게 된다. 
그리고 while 문의 내용을 한 번 수행할 때마다 coffee = coffee - 1에 의해 coffee의 개수가 1개씩 줄어든다. 만약 coffee가 0이 되면 
if coffee == 0: 문장에서 coffee == 0이 참이 되므로 if 문 다음 문장 "커피가 다 떨어졌습니다. 판매를 중지합니다."가 출력되고 break 문이 호출되어 while 문을 빠져나가게 된다.

하지만 실제 자판기는 위 예처럼 작동하지는 않을 것이다. 다음은 자판기의 실제 작동 과정과 비슷하게 만들어 본 예이다. 다음 예는 조금 복잡하므로 대화형 인터프리터를 사용하지 말고 IDLE 에디터를 사용해서 작성해 보자.
  
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

위 프로그램 소스를 따로 설명하지는 않겠다. 여러분이 소스를 입력하면서 무슨 내용인지 이해할 수 있다면 지금까지 배운 if 문이나 while 문을 이해했다고 보면 된다. 
만약 money = int(input("돈을 넣어 주세요: ")) 문장이 이해되지 않는다면 이 문장은 사용자로부터 값을 입력받는 부분이고 입력받은 숫자를 money 변수에 대입하는 것이라고만 알아 두자.

  while 문의 맨 처음으로 돌아가기
while 문 안의 문장을 수행할 때 입력 조건을 검사해서 조건에 맞지 않으면 while 문을 빠져나간다. 
그런데 프로그래밍을 하다 보면 while 문을 빠져나가지 않고 while 문의 맨 처음(조건문)으로 다시 돌아가게 만들고 싶은 경우가 생기게 된다. 이때 사용하는 것이 바로 continue 문이다.

1부터 10까지의 숫자 중에서 홀수만 출력하는 것을 while 문을 사용해서 작성한다고 생각해 보자. 어떤 방법이 좋을까?

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
1
3
5
7
9

위는 1부터 10까지의 숫자 중 홀수만 출력하는 예이다. a가 10보다 작은 동안 a는 1만큼씩 계속 증가한다. a % 2 == 0(a를 2로 나누었을 때 나머지가 0인 경우)이
참이 되는 경우는 a가 짝수일 때이다. 즉, a가 짝수이면 continue 문을 수행한다. 이 continue 문은 while 문의 맨 처음인 조건문(a < 10)으로 돌아가게 하는 명령어이다.
따라서 위 예에서 a가 짝수이면 print(a) 문장은 수행되지 않을 것이다.

무한 루프
이번에는 무한 루프(endless loop)에 대해 알아보자. 무한 루프란 무한히 반복한다는 의미이다. 우리가 사용하는 일반 프로그램 중에서 무한 루프 개념을 사용하지 않는 프로그램은 거의 없다.
그만큼 자주 사용한다는 뜻이다.

while True: 
    수행할_문장1 
    수행할_문장2
while 문의 조건문이 True이므로 항상 참이 된다. 따라서 while 문 안에 있는 문장들은 무한히 수행될 것이다.

while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
위 문장은 영원히 출력된다. 하지만 이 예처럼 아무 의미 없이 무한 루프를 돌리는 경우는 거의 없을 것이다. [Ctrl+C]를 눌러 빠져나가자.


나의 while 문'
coffee="""
  카페 관리자 모드
  1. 메뉴 보기
  2. 메뉴 추가
  3. 메뉴 삭제
  4. 메뉴 이름 바꾸기
  5. 관리자모드 종료
"""
mm=['치킨','피자','떡볶이']
while True:
   print(coffee)
   a = int(input("사용하고싶은 기능의 숫자를 입력해주세요."))
   
   if a == 1:
        for i in range(len(mm)):
            print(f"{i}.",mm[i])
            
   elif a == 2:
           for i in range(len(mm)):
           print(f"{i}.",mm[i])
           
           a = input("추가하시려는 메뉴를 선택해주세요.")
           mm.append(a)
           
           for i in range(len(mm)):       
           print(f"{i}.",mm[i])
   elif a == 3:
           for i in range(len(mm)):
           print(f"{i}.",mm[i])
           
           a = int(input("삭제하려는 메뉴의 숫자를 입력해주세요."))
           mm.remove(mm[a])
           
           for i in range(len(mm)):
           print(f"{i}.",mm[i])

   elif a == 4:
           for i in range(len(mm)):
           print(f"{i}.",mm[i])
           
           a = int(input("바꾸려는 메뉴의 숫자를 입력해주세요."))
           b = input("이름을 작성해주세요.")
           mm[a] = b
           
           for i in range(len(mm)):
           print(f"{i}.",mm[i])
   
   elif a == 5:
           print("관리자 모드를 종료하겠습니다.")
           break
   else:
      print("번호를 다시 선택해주세요.")
    
==========================================================================

숫자 맞추기
# 숫자 맞추기
import random

start = int(input("게임을 원하시면 1번 원하시지 않는다면 2번을 선택해주세요."))
score = 0
count = 0
if start == 1:
    print("-"*20)
    print("게임을 시작하겠습니다")
    print("-"*20)
    print("숫자 예측 게임에 오신걸 환영합니다!")
    print("이 게임은 1~3의 숫자를 예측해서, 그 숫자와 같은 숫자를 고르시면 이기는 게임입니다!")
    while True:
        You = int(input("1~3의 숫자를 입력해주세요!"))
        random_AI = random.randint(1,3)
        if You < 4:
            if You == random_AI:
                print("축하합니다!","같은 숫자를 맞추셨습니다!","스코어 +1")
                score += 1
                count += 1
            else:
                print("ㅜㅜ 같은 숫자가 아닙니다...! 스코어 - 1")
                score -= 1
                count += 1
            select = input("게임을 계속하시겠습니까?  [Yes / no]")
            if select == "Yes" or select == "yes":
                print(f"현재 점수 {score}점!")
                print("-"*20)
            elif select == "no":
                print(f"{count}번의 플레이! 총점 {score}점! 수고하셨습니다!")
                break
            else:
                print("yes 또는 no를 다음에는 선택해주세요!")
                print("게임 한판더!")
        else:
            print("숫자를 다시 선택해주세요!")
elif start == 2:
    print("게임을 종료하겠습니다.")

else:
    print("번호를 다시 입력해주세요.")

    










