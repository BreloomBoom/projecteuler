def process(txt):
    listed = open(txt, "r").read().split("\n")
    matrix = []
    for i in listed:
        matrix.append([int(x) for x in i.split()])

    return matrix

def brute(txt):
    maxi = 1
    matrix = process(txt)
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns-3):
            if maxi < matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]:
                maxi = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]

    for j in range(columns):
        for i in range(rows-3):
            if maxi < matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j]:
                maxi = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j]
    
    for i in range(rows-3):
        for j in range(columns-3):
            if maxi < matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3]:
                maxi = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3]

    for i in range(3, rows):
        for j in range(columns-3):
            if maxi < matrix[i][j] * matrix[i-1][j+1] * matrix[i-2][j+2] * matrix[i-3][j+3]:
                maxi = matrix[i][j] * matrix[i-1][j+1] * matrix[i-2][j+2] * matrix[i-3][j+3]

    return maxi

if __name__ == "__main__":
    maxi = brute("/Users/breloom/Code/projecteuler/11.txt")
    print(f"{maxi}")