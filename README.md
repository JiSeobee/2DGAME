# 2DGAME
------------------
## 01.**게임소개**
 **1. GameTitle** 
 
  -**FlightShooting(가제)**
 
 
 
 **2. 참고 한 게임에 대한 정보**

 
   ![DF](https://user-images.githubusercontent.com/70791450/94224092-797b7780-ff2c-11ea-8252-6731b76b5722.jpg) 
   
    [사진1: 드래곤플라이트(DragonFlight)]
   
    -화면하단에 플레이어가 위치(Y축은고정된 위치, X축(좌,우)로만 움직임)하며 플레이어가 움직일 때 마다 총알이 발사
   
    -상단에 출현하는 몬스터들을 공격(몬스터들은 x축은 고정되어 있으나 y축으로 이동하여 점점 내려옴)
    
    -몬스터마다 hp가 존재. 해당 hp가 0이되어야 몬스터가 사라짐.
   
    -적들을 물리치며 앞으로 나아가는데 멀리 갈수록 비행속도가 빨라지며 몬스터도 강해짐.
   
    -몬스터의 공격 혹은 몬스터 및 장애물이 플레이어에 닿으면 게임 종료
 
   
   ![Galaga](https://user-images.githubusercontent.com/70791450/94224283-e4c54980-ff2c-11ea-8730-99f1733a46d1.jpg)      
   
    [사진2: 갤러그]
   
    -드래곤 플라이트의 원조격 게임으로 방법은 동일하다. 
 
 

 **3. 게임목적 및 방법**
    
     1) 기본적인 게임 방법은 참고한 게임들과 동일하게 플레이어는 화면의 좌우로 움직인다.
        (만들 게임에 경우 마우스 포인터를 플레이어가 따라가도록 함)
       
     2) 플레이어는 hp100에서 시작하고, 마우스 포인터를 움직일 때마다 총이 자동으로 발사한다. 
     
     3) 몬스터는 일정 시간마다 출현하며 점점 플레이어쪽으로 내려오며 플레이어는 해당 몬스터를 잡도록한다.
     
     4) 몬스터를 잡으면 총이나 hp포션을 얻게 된다. (총:데미지 및 범위 상승, hp포션:플레이어 hp 회복)
     
     5) 게임이 진행 될수록 점점 몬스터 종류는 다양해지며,
     
     6) 각 몬스터는 종류마다 hp와 플레이어에게 공격하는 데미지가 다르다.
     
     7) 플레이어는 몬스터의 공격을 받거나 혹은 몬스터에 닿거나 장애물에 맞는경우 hp가 감소한다.
     
     8) hp가 0이 되면 게임이 종료되고 버틴 시간 * 몬스터 별 점수를 더한 값으로 score 계산. 
     
     9) 이렇게하여 더 높은 점수를 얻기 위해 플레이를 진행하는 것에 목적을 두고있다.
   
   
 ---------------------  
 ## 02.**Game State(Scene)의 수 및 이름**
 
 Game State 수는 크게 다음과 같이 5개로 구성할 예정이다.(차후 변경이 있을 수 있음)
 
 ### 1) Title Scene
 ### 2) Setting Scene
 ### 3) Main Play Scene
 ### 4) Game over Scene
 ### 5) Result Scene
 
 
 ---------------------
 ## 03.**각 Game State 별 항목**
 
 ### 1) Title Scene
     -먼저 Title Scene 에서는 게임 시작 전 화면을 보여주며 화면에 Setting, Start 객체가 표시된다.
     -마우스를 이용하여 화면상의 Start 버튼 혹은 키보드의 Space bar를 누를 경우에는 Main Play 화면 창으로 화면이 전환된다.
     -마우스를 이용하여 화면상의 Setting 버튼을 누를 경우에는 Setting 화면 창으로 화면이 전환된다.
     -화면 우상단의 X 버튼 혹은 esc 키를 누를 경우 프로그램이 종료 된다. 
  
 ### 2) Setting
     -아직 완벽하게 정한것은 아니지만 이 창에서는 캐릭터 선택 등을 할 수 있다.
     -객체는 크게 Home, character 등이 표시 될 것이다.
     -마우스를 이용하여 Character의 종류를 선택 할 수 있으며 선택한 캐릭터로 플레이가 가능하다.
     -마우스를 이용하여 화면상의 Home 버튼을 누를 경우 다시 초기 Title 화면으로 이동하게 된다.
     
 ### 3) Main Play
     -실제 플레이어가 게임을 진행하게 되는 화면으로 화면에 character, monster, 플레이어 정보 등 객체가 표시된다.
     -만약 플레이 도중 화면 우측 상단에 마우스를 이용하여 home 버튼을 누르면 game over 창으로 가게 된다.
     -기본적인 플레이어의 동작은 마우스의 포인터를 charater가 따라가며 움직일 때마다 총이 발사되어 몬스터를 해치운다.
     -만약 플레이어의 hp가 0이 된 경우 Game over 창으로 전환된다.
 
  ### 4) Game Over
      -이 창은 플레이어가 죽은 경우나 플레이 도중 Home 버튼을 눌렀을 경우 전환되는 화면이다.
      -Game Over 창에서는 자동으로 2초 후에 결과 창으로 넘어가도록 한다.
      
  ### 5)Result
      -이 창에서는 Score, Home, Restart, Quit 으로 구성된다. 
      -Score에 경우 플레이어의 게임 결과 점수가 반영되어 표시된다.
      -마우스를 이용하여 화면상의 Home 버튼을 누를 경우 초기 Title 화면으로 이동한다.
      -마우스를 이용하여 화면상의 Restart 버튼을 누를 경우 Main Play 화면으로 이동한다.
      -마우스를 이용하여 화면상의 Quit 버튼을 누를 경우 프로그램이 종료된다.
      
  ###**위의 State를 다이어그램으로 표현하면 다음과 같다.**
  
  ![GameState](https://user-images.githubusercontent.com/70791450/94235999-7477f180-ff47-11ea-8932-7dbbe77b8ca4.JPG)

     
     
   
 
 ----------------------
 ## 04.필요 기술
 
 
 
 
