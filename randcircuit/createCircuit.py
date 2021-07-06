

from .grid import symbol, value
import tikz as tz

def drawElement(pic, i, j, ip, jp, element):
    if element[symbol] in ['V','I','R']:
        pic.draw((i,j),tz.lineto((ip,jp),op='to [{}, l^={}]'.format(element[symbol],element[value])))
    else:
        pic.draw((i,j),element[symbol],(ip,jp))

def createTikzCircuit(grid,scale=2):
    """
    grid is a rectangular array of circuit elements
    """
    pic = tz.Picture(scale=scale, tempdir='.', cache=False)
    pic.add_preamble(r'\usepackage[american, siunitx]{circuitikz}')

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            uelement = grid[i][j].get('u')
            lelement = grid[i][j].get('l')
            if uelement:
                drawElement(pic, i, j, i+1, j, uelement)
            if lelement:
                drawElement(pic, i, j, i, j+1, lelement)
    return pic

