import svgwrite

array_2d = [1,2,3,4]
dwg = svgwrite.Drawing('test.svg', profile='full',size=(300,300))

dwg.add(dwg.line((50, 0), (100, 100), stroke=svgwrite.rgb(10, 10, 16, '%')))

dwg.add(dwg.text(
    'Test', 
    insert=(100, 100), 
    fill='red',
    # style = "font-size:20px"
    font_size="60px"
    
    ))
dwg.save()