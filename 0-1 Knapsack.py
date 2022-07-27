# TC: O((n+1)*(W+1))
# SC: O((n+1)*(W+1))

def knapSack(W, wt, val, n):
    # list comprehension to create a 2-D matrix with size (n+1)*(W+1)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                # Filling the first row and first column as 0
                K[i][w] = 0
            elif wt[i-1] <= w:
                # Filling the rest of the matrix with the formula
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 