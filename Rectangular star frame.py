a=int(input('Columns:'))
b=int(input('Rows:'))
def rectangular_star_frame(cols, rows):
    for i in range(cols):
        for j in range(rows):
            if (i==0) or (i==cols-1) or (j==0) or (j==rows-1):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

# Example usage:
rectangular_star_frame(a, b)
