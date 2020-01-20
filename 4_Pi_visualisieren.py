import turtle as tu

lines = 100_000

with open("4a_Pi_MillionDigits.txt", "r") as f:
    pi = f.read()

tu.mode('logo')
tu.tracer(False)
tu.screensize(3000,3000,'black')
tu.colormode(255)

for n in range(lines):
    color=int(n/(lines/255))
    tu.pencolor(255,255-color,color)    
    zahl = int(pi[n])
    if zahl % 2 == 0:
        tu.setheading((zahl))
    else:
        tu.setheading((zahl+180))    
    tu.forward(3)
    if n % 1000 == 0:
        tu.update()
        print(n)

tu.getcanvas().postscript(file='PI_Bild.ps')
tu.done()
print("Ready.")
