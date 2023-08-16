from turtle import*

color('green','red')
pencolor('black')
pen('green')
pensize(7)
begin_fill()

while True:
            forward(200)
            left(250)
            if abs(pos()) < 8:
                break

end_fill()

done()
