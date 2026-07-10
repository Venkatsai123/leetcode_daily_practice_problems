def findMissingAndRepeatedValues( grid):
    grid_length = len(grid)
    missing_repepeated_values = [0,0]
    missing_values =[0]*(grid_length*grid_length + 1)
    for i in grid:
        for j in i:
            if(missing_values[j]==0):
                missing_values[j] =1
            else:
                missing_repepeated_values[0] = j
    # print(missing_values,missing_repepeated_values)

    for i in range(len(missing_values)):
        if(i!=0 and missing_values[i]==0):

            missing_repepeated_values[1]=i
    return missing_repepeated_values




grid = [[1,3],[2,2]]
print(findMissingAndRepeatedValues(grid))
grid = [[9,1,7],[8,9,2],[3,4,6]]
print(findMissingAndRepeatedValues(grid))