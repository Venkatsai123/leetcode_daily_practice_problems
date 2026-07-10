def generate( numRows):
    pascals_rows = [[1],[1,1],[1,2,1]]
    for i in range(3,numRows+1):
        old_pascals_rows = pascals_rows[i-1]
        new_row = [1]*(i+1)
        for j in range(1,i):
            new_row[j]=old_pascals_rows[j-1]+old_pascals_rows[j]
        pascals_rows.append(new_row)
    print(pascals_rows)
generate(5)