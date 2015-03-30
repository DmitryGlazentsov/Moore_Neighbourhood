#решал методом "в лоб"
    #cуть решения в том, что поле я разделял на области и
    #описывал решение для каждой конкретной области возможных значений row и col
    #какая область описывается вы можете узнать из условия самого ифа
   
   if row==0 and col==0: #мы находимся на пересечении первой строки и первого столбца (левом верхний угол)
        return grid[row][col+1]+grid[row+1][col]+grid[row+1][col+1]
        
    if row==0 and col==len(grid[0])-1:#мы находимся на пересечении первой строки и последнего столбца (верхний правый  угол)
        return grid[row][col-1]+grid[row+1][col]+grid[row+1][col-1]
    
    if row==len(grid)-1 and col==0:# мы находимся на пересечении нижней строки и левого столбца (нижний левый угол)
        return grid[row-1][col]+grid[row-1][col+1]+grid[row][col+1]
        
    if row==len(grid)-1 and col==len(grid[0])-1:# мы находимся в нижней строке, в последнем столбце (правый нижний угол)
        return grid[row][col-1]+grid[row-1][col]+grid[row-1][col-1]
        
    if row>0 and row<len(grid)-1 and col==0:# по левой стенке в первом(нулевом) столбце со второй(row =1)строки по предпоследнюю(не захватываем угол)
        resultup = grid[row-1][col]+grid[row-1][col+1]
        resultcenter = grid[row][col+1]
        resultlow = grid[row+1][col]+grid[row+1][col+1]
        result = resultup+ resultcenter+resultlow
        return result
    if row==0 and col>0 and col<len(grid[0])-1:# по верхней стенке в первой(grid[0]) строке со второго столбца по предпоследний.
        resultup = grid[row][col-1]+grid[row][col+1]
        resultlow = grid[row+1][col-1]+grid[row+1][col]+grid[row+1][col+1]
        result = resultup+resultlow
        return result
    if row>0 and row<len(grid)-1 and col==len(grid[0])-1:# по дальней правой стенке со второй строки по предпоследнюю в последнем столбце
        resultup = grid[row-1][col-1]+grid[row-1][col]
        resultcenter = grid[row][col-1]
        resultlow = grid[row+1][col-1]+grid[row+1][col]
        result = resultup+ resultcenter+resultlow
        return result
    if row==len(grid)-1 and col>0 and col<len(grid[0])-1:# по нижней стенке(нижняя строка) со второго стобца по предпоследний
        resultup = grid[row][col-1]+grid[row][col+1]
        resultlow = grid[row-1][col-1]+grid[row-1][col]+grid[row-1][col+1]
        result = resultup+resultlow
        return result
    else:#самая середина (то есть со всех сторон есть отступ 1 строка и 1 столбец)
        resultup=grid[row-1][col-1]+grid[row-1][col]+grid[row-1][col+1]
        resultcenter = grid[row][col-1]+grid[row][col+1]
        resultlow = grid[row+1][col-1]+grid[row+1][col]+grid[row+1][col+1]
        result = resultup+resultcenter+resultlow
        return result
