import svgwrite

def gride_2d(data):
    # row
    w = len(data)
    # column
    h = len(data[0])
    

array_2d = [
    [1,2],
    [3,4]
]
dwg = svgwrite.Drawing('test.svg', profile='full',size=(300,300))
x = 0
y = 10
for i in array_2d:
    x+=80
    rect = dwg.rect(
        insert=(x,y),
        size=(50,50),
        fill='red',
        rx=10,
        stroke='black',
        stroke_width=5
        )
    dwg.add(rect)

dwg.save()