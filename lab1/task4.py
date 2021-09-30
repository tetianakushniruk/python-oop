def max_weight(capacity, weights):
    # making matrix of weights where cols = capacity and rows = len of weights
    # filling it with zeros
    matrix = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
    for i in range(1, len(weights)+1):
        for j in range(1, capacity+1):
            if weights[i-1] <= j:
                matrix[i][j] = max(weights[i-1] + matrix[i-1][j-weights[i-1]], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[-1][-1]


if __name__ == '__main__':
    W = int(input('Capacity: '))
    # making list of integers from input string
    list_of_weights = list(map(int, input('List of weights: ').split()))
    print(max_weight(W, list_of_weights))
