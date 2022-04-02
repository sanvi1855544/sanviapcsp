
def driver():
    matrix = [[1,2,3,],
              [4,5,6],
              [7,8,9] ]

    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))

if __name__ == "__main__":
    driver()