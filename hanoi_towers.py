def tower_of_hanoi(n,fromrod,torod,auxrod):
    if n==1:
        return "move disk 1 from ",fromrod,"to" , torod
    tower_of_hanoi(n-1,fromrod,auxrod,torod)
    print("move disk",n,"from",fromrod,"to",torod)
    tower_of_hanoi(n-1,auxrod,torod,fromrod)


tower_of_hanoi(4,1,2,3)