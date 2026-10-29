

print("I love animals!")
print("Let's check out the animals...")
print()
print("The deer looks fine.")


camel = r"""
The camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !      ! !   ; ;
            | ;    ! !      ! !   | ;
            /_I    L_I      L_I   /_I
Look at that!"""

lion = r"""
The lion habitat...
                                           ,w.
                                         ,YWMMw  ,M  ,
                    _.---.._   __..---._.'MMMMMw,wMWmW,
               _.-""        '''           YP"WMMMMMMMMMb,
            .-' __.'                   .'     MMMMW^WMMMM;
         .-'  .-"";'.                 /       :MMM[==MWMW^;
    ,mM^"    .'   /   ;              /        MMMMb_wMW"  @\
   ,MM:.    .'.-'   .M;             /         MMMMMMM^"=. /-,
   WMMm__,-'.'     /mM!           .'          ,dMMMMMMMM[,_ / =_)
   "^MP.-'    ,-' _.--""'   ;  ;           ;MMMMMMMMMMMW^``; |
               /   .'         ;  ;           )  ){ _ '"^W^,   \  :
              /  .'           /  (          /  /   Ww._     '-.  "
             /  Y,            ;   '._=,__{   ;      MMMP""-,  -._.-,
            (--, )            ._ / ) \/"")  ^"       ^-, -;"\:
The lion is roaring!"""

deer = r"""
The deer habitat...
   /|       |\
__\\       //__'
   ||      ||
 \__\     |'__/
   _\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;-'   ---..........--._
     ;;;                        \._
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
Pretty good!"""

goose = r"""
The goose habitat...

                                    _
                                ',-"" "".
                              ,'  ____  .
                            ,'  ,'    .  ._
   (.         _..--.._   ,'  ,'        \    \
  (-.\    .-""        ""'   /          (  d _b
 (._  -"" ,._             (            -(   \
 <_       (  <<            \              -._\
  <`-       (__< <           :
   (__        (_<_<          ;
------------------------------------------------
Beautiful!"""

bat = r"""
The bat habitat...
 _________________             _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /              /---\             \
      /              |     |             \
      >              |     |            <
     / __            |     |             \
           \         \     /            /  
             \       /\   / \         /        
               \    /  \ /    \     /           
                 \ /    v       \ /              
It's doing fine."""

rabbit = r"""
The rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"   |
  Y     _,   |
 /| ;-"~ _  1
/ 1/ ,-"~    \
\//\/      .- \
 Y        /    Y
 1       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
It looks fine!"""

animals = [camel, lion, deer, goose, bat, rabbit]


while True:
    number = input(
        "Please enter the number of the habitat you would like to view: "
    )

    if number == "exit":
        print("See you later!")
        break

    if number.isdigit():
        number = int(number)

        if 1 <= number <= len(animals):
            print(animals[number - 1])
        else:
            print("Please enter a number from 1 to 6.")
    else:
        print("Please enter a number from 1 to 6.")


