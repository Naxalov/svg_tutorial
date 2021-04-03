import svgwrite

def gride_2d(data):
    # row
    row = len(data)
    # column
    column = len(data[0])
    scale = 50
    row*=scale
    column*=scale
    rect_size = (scale-scale*0.1,scale-scale*0.1)

    dwg = svgwrite.Drawing('test.svg', profile='full',size=(column,row))
    # Rectangle group
    rect_g = dwg.add(dwg.g(id='rect'))
    txt_g = dwg.add(dwg.g(id='txt'))
    for y,row in enumerate(data):
        print(row)
        for x,column in enumerate(row):
            rect=dwg.rect(
                insert=(x*scale,y*scale),
                size=rect_size,
                fill='#e63946',
                # rx=10,
                stroke='black',
                # stroke_width=5
                )
            txt = dwg.text(
                f'{column}', 
                insert=(x*scale+scale//2,y*scale+scale//2),
                font_size=10, 
                fill='#1d3557'
                )
            rect_g.add(rect)
            txt_g.add(txt)
    dwg.save()
    return True






array_2d = [
    ['ID',0,1,2,3],
    [0,7,5,3,8],
    [1,7,5,3,8]
    # [3,4],
]

gride_2d(array_2d)
