def Square(s):
    if(s == "square"):
        return True
    return False

def Red(c):
    if(c == "red"):
        return True
    return False

def tarski(shapes, colors):
    row = len(shapes)
    col = len(shapes[0])
    for i in range(row):
        for j in range(col):
            if(Square(shapes[i][j]) and (not Red(colors[i][j]))):
                return False
    return True

shapes = [['circle'  , 'circle', 'circle'],
          ['triangle', 'circle', 'square'],
          ['triangle', 'square', 'circle']]
colors = [['blue', 'red' , 'gray'],
          ['red' , 'gray', 'red' ],
          ['blue', 'red' , 'blue']]
print(tarski(shapes, colors))

shapes = [['square', 'square'],
          ['circle', 'circle']]
colors = [['red' , 'blue'],
          ['gray', 'red' ]]
print(tarski(shapes, colors))

colors = [['blue', 'red' , 'red' , 'gray', 'red' ],
          ['blue', 'red' , 'gray', 'blue', 'blue'],
          ['blue', 'gray', 'gray', 'red' , 'red' ],
          ['red' , 'red' , 'red' , 'blue', 'gray'],
          ['blue', 'gray', 'blue', 'gray', 'blue']]
shapes = [['square', 'triangle', 'circle'  , 'square', 'circle'  ],
          ['circle', 'circle'  , 'triangle', 'circle', 'circle'  ],
          ['square', 'circle'  , 'circle'  , 'circle', 'triangle'],
          ['circle', 'square'  , 'triangle', 'circle', 'circle'  ],
          ['square', 'square'  , 'triangle', 'circle', 'triangle']]
print(tarski(shapes, colors))
