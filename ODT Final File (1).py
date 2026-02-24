from machine import Pin,PWM
import time
import neopixel
import random

dice = PWM(Pin(18),freq=50) # Naming servo
np = neopixel.NeoPixel(Pin(19),16) # Naming Neopixel
p1=Pin(22,Pin.IN,Pin.PULL_UP) #Naming Player 1 push button
p2=Pin(17,Pin.IN,Pin.PULL_UP) #Naming Player 2 push button
ir1= Pin(27,Pin.IN,Pin.PULL_UP) #Naming ir sensor 1
ir2= Pin(4,Pin.IN,Pin.PULL_UP) #Naming ir sensor 2
Red1=Pin(25,Pin.OUT) #LED1
Red2=Pin(32,Pin.OUT) #LED2
Red3=Pin(33,Pin.OUT) #LED3
Red4=Pin(12,Pin.OUT) #LED4
Red5=Pin(14,Pin.OUT) #LED5
buzz1= Pin(21,Pin.OUT) #buzzer 1

anglez = [35, 65, 95, 120, 95, 65]


'''                    #to fix faulty connections
Red1.on()
Red2.on()
Red3.on()
Red4.on()
Red5.on()
'''
'''8
while True:
    p1_val= p1.value()
    p2_val= p2.value()
    print(p1_val)
    print(p2_val)
    time.sleep(0.2)
    
    
'''
while True:
    p1_val= p1.value()
    p2_val= p2.value()
    r=random.randint(1,4)   #choose a random time for the lights to go out
    
    if p1_val==0 and p2_val==0:  #reset the neopixel to turn all the lights off
        turn = 0
        np[1]=(0,0,0)
        np[2]=(0,0,0)
        np[3]=(0,0,0)
        np[4]=(0,0,0)
        np[5]=(0,0,0)
        np[6]=(0,0,0)
        np[7]=(0,0,0)
        np[8]=(0,0,0)
        np[9]=(0,0,0)
        np[10]=(0,0,0)
        np[11]=(0,0,0)  
        np[12]=(0,0,0)
        np[13]=(0,0,0)
        np[14]=(0,0,0)
        np[15]=(0,0,0)
        np[0]=(0,0,0)
        np.write()
        
        Red1.on()          #the red LEDs turn on one by one from here
        buzz1.on()
        time.sleep(0.2)
        buzz1.off()
        time.sleep(0.8)
        Red2.on()
        buzz1.on()
        time.sleep(0.2)
        buzz1.off()
        time.sleep(0.8)
        Red3.on()
        buzz1.on()
        time.sleep(0.2)
        buzz1.off()
        time.sleep(0.8)
        Red4.on()
        buzz1.on()
        time.sleep(0.2)
        buzz1.off()
        time.sleep(0.8)
        Red5.on()
        buzz1.on()
        time.sleep(0.2)
        buzz1.off()
        time.sleep(r)
        Red1.off()
        Red2.off()
        Red3.off()
        Red4.off()
        Red5.off()

        turn = 0      #resets the variable 'turn' to 0
        p1_val= p1.value()
        p2_val= p2.value() 

        if p1_val == 0 and p2_val == 1:                     #penalises if a false start is occured
            print("P1 pressed early! Chance goes to P2")
            turn = 2

        elif p2_val == 0 and p1_val == 1:
            print("P2 pressed early! Chance goes to P1")
            turn = 1

        if turn == 0:
            while True:
                p1_val= p1.value()
                p2_val= p2.value()
                if p1_val == 0 and p2_val==1:              #if p1 is faster
                    turn = 1
                    print("only Button 1 pressed")
                    while True :

                        np[1]=(255,0,0)
                        np[2]=(255,0,0)
                        np[3]=(255,0,0)
                        np[4]=(255,0,0)
                        np[5]=(255,0,0)
                        np[6]=(255,0,0)
                        np[7]=(255,0,0)
                        np[8]=(255,0,0)
                        np[9]=(255,0,0)
                        np[10]=(255,0,0)
                        np[11]=(255,0,0)  
                        np[12]=(255,0,0)
                        np[13]=(255,0,0)
                        np[14]=(255,0,0)
                        np[15]=(255,0,0)
                        np[0]=(255,0,0)
                        np.write()

                        time.sleep(1.2)
                        np[1]=(0,0,0)
                        np[2]=(0,0,0)
                        np[3]=(0,0,0)
                        np[4]=(0,0,0)
                        np[5]=(0,0,0)
                        np[6]=(0,0,0)
                        np[7]=(0,0,0)
                        np[8]=(0,0,0)
                        np[9]=(0,0,0)
                        np[10]=(0,0,0)
                        np[11]=(0,0,0)  
                        np[12]=(0,0,0)
                        np[13]=(0,0,0)
                        np[14]=(0,0,0)
                        np[15]=(0,0,0)
                        np[0]=(0,0,0)
                        np.write()
                        time.sleep(0.1)
                        break
                        
                    break
                
                elif p2_val == 0 and p1_val== 1:                 #if p2 is faster
                    turn = 2
                    print("only Button 2 pressed")
                    while True :
                        np[1]=(0,0,255)
                        np[2]=(0,0,255)
                        np[3]=(0,0,255)
                        np[4]=(0,0,255)
                        np[5]=(0,0,255)
                        np[6]=(0,0,255)
                        np[7]=(0,0,255)
                        np[8]=(0,0,255)
                        np[9]=(0,0,255)
                        np[10]=(0,0,255)
                        np[11]=(0,0,255)  
                        np[12]=(0,0,255)
                        np[13]=(0,0,255)
                        np[14]=(0,0,255)
                        np[15]=(0,0,255)
                        np[0]=(0,0,255)
                        np.write()

                        time.sleep(1.2)
                        np[1]=(0,0,0)
                        np[2]=(0,0,0)
                        np[3]=(0,0,0)
                        np[4]=(0,0,0)
                        np[5]=(0,0,0)
                        np[6]=(0,0,0)
                        np[7]=(0,0,0)
                        np[8]=(0,0,0)
                        np[9]=(0,0,0)
                        np[10]=(0,0,0)
                        np[11]=(0,0,0)  
                        np[12]=(0,0,0)
                        np[13]=(0,0,0)
                        np[14]=(0,0,0)
                        np[15]=(0,0,0)
                        np[0]=(0,0,0)
                        np.write()
                        time.sleep(0.1)
                        break
    
                    break                   #breaks the while true loop after flashing winning team's colour
                time.sleep(0.01)

        if turn == 1:                 #if p1 wins
            print("TURN 1")
            chance = p1
            
        elif turn == 2:               #if p2 wins
            print("TURN 2")
            chance = p2

        while p1.value() == 0 or p2.value() == 0:
            time.sleep(0.05)

        while True:                 #servo starts here
            for a in anglez:
                dice.duty(a)
                time.sleep(0.4)
                if chance.value() == 0:   #to break the flow of for loop
                    break
            if chance.value() == 0:    #to break the flow of while loop
                    break
                
                
        while True:
            val1 = ir1.value()      #reading ir sensor values
            val2 = ir2.value()
            
            if val1 == 0:           #flashes red light if they win
                np[1]=(255,0,0)
                np[2]=(255,0,0)
                np[3]=(255,0,0)
                np[4]=(255,0,0)
                np[5]=(255,0,0)
                np[6]=(255,0,0)
                np[7]=(255,0,0)
                np[8]=(255,0,0)
                np[9]=(255,0,0)
                np[10]=(255,0,0)
                np[11]=(255,0,0)  
                np[12]=(255,0,0)
                np[13]=(255,0,0)
                np[14]=(255,0,0)
                np[15]=(255,0,0)
                np[0]=(255,0,0)
                np.write()
                buzz1.on()
                time.sleep(0.3)
                buzz1.off()
                np[1]=(0,0,0)
                np[2]=(0,0,0)
                np[3]=(0,0,0)
                np[4]=(0,0,0)
                np[5]=(0,0,0)
                np[6]=(0,0,0)
                np[7]=(0,0,0)
                np[8]=(0,0,0)
                np[9]=(0,0,0)
                np[10]=(0,0,0)
                np[11]=(0,0,0)  
                np[12]=(0,0,0)
                np[13]=(0,0,0)
                np[14]=(0,0,0)
                np[15]=(0,0,0)
                np[0]=(0,0,0)
                np.write()
                time.sleep(0.3)
                np[1]=(255,0,0)
                np[2]=(255,0,0)
                np[3]=(255,0,0)
                np[4]=(255,0,0)
                np[5]=(255,0,0)
                np[6]=(255,0,0)
                np[7]=(255,0,0)
                np[8]=(255,0,0)
                np[9]=(255,0,0)
                np[10]=(255,0,0)
                np[11]=(255,0,0)  
                np[12]=(255,0,0)
                np[13]=(255,0,0)
                np[14]=(255,0,0)
                np[15]=(255,0,0)
                np[0]=(255,0,0)
                np.write()
                buzz1.on()
                time.sleep(0.3)
                buzz1.off()
                np[1]=(0,0,0)
                np[2]=(0,0,0)
                np[3]=(0,0,0)
                np[4]=(0,0,0)
                np[5]=(0,0,0)
                np[6]=(0,0,0)
                np[7]=(0,0,0)
                np[8]=(0,0,0)
                np[9]=(0,0,0)
                np[10]=(0,0,0)
                np[11]=(0,0,0)  
                np[12]=(0,0,0)
                np[13]=(0,0,0)
                np[14]=(0,0,0)
                np[15]=(0,0,0)
                np[0]=(0,0,0)
                np.write()
                
                break
            if val2 == 0:                #flashes blue light if they won
                np[1]=(0,0,255)
                np[2]=(0,0,255)
                np[3]=(0,0,255)
                np[4]=(0,0,255)
                np[5]=(0,0,255)
                np[6]=(0,0,255)
                np[7]=(0,0,255)
                np[8]=(0,0,255)
                np[9]=(0,0,255)
                np[10]=(0,0,255)
                np[11]=(0,0,255)  
                np[12]=(0,0,255)
                np[13]=(0,0,255)
                np[14]=(0,0,255)
                np[15]=(0,0,255)
                np[0]=(0,0,255)
                np.write()
                buzz1.on()
                time.sleep(0.3)
                buzz1.off()
                np[1]=(0,0,0)
                np[2]=(0,0,0)
                np[3]=(0,0,0)
                np[4]=(0,0,0)
                np[5]=(0,0,0)
                np[6]=(0,0,0)
                np[7]=(0,0,0)
                np[8]=(0,0,0)
                np[9]=(0,0,0)
                np[10]=(0,0,0)
                np[11]=(0,0,0)  
                np[12]=(0,0,0)
                np[13]=(0,0,0)
                np[14]=(0,0,0)
                np[15]=(0,0,0)
                np[0]=(0,0,0)
                np.write()
                time.sleep(0.3)
                np[1]=(0,0,255)
                np[2]=(0,0,255)
                np[3]=(0,0,255)
                np[4]=(0,0,255)
                np[5]=(0,0,255)
                np[6]=(0,0,255)
                np[7]=(0,0,255)
                np[8]=(0,0,255)
                np[9]=(0,0,255)
                np[10]=(0,0,255)
                np[11]=(0,0,255)  
                np[12]=(0,0,255)
                np[13]=(0,0,255)
                np[14]=(0,0,255)
                np[15]=(0,0,255)
                np[0]=(0,0,255)
                np.write()
                buzz1.on()
                time.sleep(0.3)
                buzz1.off()
                np[1]=(0,0,0)
                np[2]=(0,0,0)
                np[3]=(0,0,0)
                np[4]=(0,0,0)
                np[5]=(0,0,0)
                np[6]=(0,0,0)
                np[7]=(0,0,0)
                np[8]=(0,0,0)
                np[9]=(0,0,0)
                np[10]=(0,0,0)
                np[11]=(0,0,0)  
                np[12]=(0,0,0)
                np[13]=(0,0,0)
                np[14]=(0,0,0)
                np[15]=(0,0,0)
                np[0]=(0,0,0)
                np.write()
                time.sleep(0.3)
                np[1]=(0,0,255)
                np[2]=(0,0,255)
                np[3]=(0,0,255)
                np[4]=(0,0,255)
                np[5]=(0,0,255)
                np[6]=(0,0,255)
                np[7]=(0,0,255)
                np[8]=(0,0,255)
                np[9]=(0,0,255)
                np[10]=(0,0,255)
                np[11]=(0,0,255)  
                np[12]=(0,0,255)
                np[13]=(0,0,255)
                np[14]=(0,0,255)
                np[15]=(0,0,255)
                np[0]=(0,0,255)
                np.write()
                buzz1.on()
                time.sleep(0.3)
                buzz1.off()
                np[1]=(0,0,0)
                np[2]=(0,0,0)
                np[3]=(0,0,0)
                np[4]=(0,0,0)
                np[5]=(0,0,0)
                np[6]=(0,0,0)
                np[7]=(0,0,0)
                np[8]=(0,0,0)
                np[9]=(0,0,0)
                np[10]=(0,0,0)
                np[11]=(0,0,0)  
                np[12]=(0,0,0)
                np[13]=(0,0,0)
                np[14]=(0,0,0)
                np[15]=(0,0,0)
                np[0]=(0,0,0)
                np.write()
                break
            break                        #breaks the while loop so that the game can be reset easily
            

            
            
                
        
            
                
