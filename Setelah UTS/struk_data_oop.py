class robot():
    nama = None 
    versi = None
    umur = None
    address = None
    address2 = None
    
robot1 = robot()
robot2 = robot()
robot3 = robot()
# robot4 = robot()
# robot5 = robot()
# robot6 = robot()
# robot7 = robot()

robot1.nama = "sherly"
robot1.model = "fighter"
robot1.versi = "1.0"
robot1.address = robot2
robot1.address2 = robot3

robot2.nama = "robert"
robot2.model = "Marksman"
robot2.versi = "1.1"

robot3.nama = "Ishaa"
robot3.model = "Mage"
robot3.versi = "1.2"

# robot4.nama = "Schzaw"
# robot4.model = "Sniper"
# robot4.versi = "1.3"    
# robot4.address = robot5

# robot5.nama = "Alex"
# robot5.model = "Tank"
# robot5.versi = "1.4"
# robot5.address = robot6

# robot6.nama = "Chloe"
# robot6.model = "Healer"
# robot6.versi = "1.5"
# robot6.address = robot7

# robot7.nama = "Claire"
# robot7.model = "Spy"
# robot7.versi = "1.6"

ptr = robot1

while ptr:
    print(ptr.nama)
    print(ptr.model)
    print(ptr.versi)
    print()
    ptr = ptr.address, ptr.address2