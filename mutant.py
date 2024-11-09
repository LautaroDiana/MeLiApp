## Function to check horizontal lines
def get_horizontal(dna):
    output = False
    letters = ['A','T','C','G']
    indexes = []

    for letter in letters:
        mask = []
        result = []
        
        #For a given letter, we build the mask variable, which in every position is a nested lists with 1 in the positions of the letter, 0 when not.      
        for i in range(len(dna)):
            mask.append([1 if element == letter else 0 for element in dna[i]])

        #With that new array, we make a new list called results, where we parse all elements of the lists as strings.
        #Next, we split it any time there's a 0, so we have N lists, but some of them with strings filled with any amount of ones and some empty strings.
        for i in range(len(mask)):
            row_str = [str(element) for element in mask[i]] 
            row_str = ''.join(row_str)
            result.append(row_str.split('0'))

        #The last step is, for every element in our results array, we count the ones strings. 
        #If any element of any nested list in has a length greater or equal than four, that means we have at least four in line in an horizontal line
        for i in range(len(result)):
            for element in result[i]:
                if len(element) >= 4:
                    indexes.append((len(element)))

    if indexes != []:
        output = True

    return output
## Functions to check vertical lines
def transpose(array):
    
    aux = [[] for element in array]
    for i in range(len(aux)):
        for j in range(len(aux)):
            aux[i].append(array[j][i])
            
    array_transp = []
    for row in aux:
        array_transp.append(''.join(row))

    return array_transp

def get_vertical(dna):

    dna_transp = transpose(dna)
    output = get_horizontal(dna_transp)
    
    return output

## Functions to check diagonals

def diagonalize(array):
    new_array = []

    for row in array:
        new_array.append([element for element in row])
    
    n=len(new_array)
    aux = [[] for empty_lists in range(2*n-1)]
    k = 0
    
    for i in range(n):
        for j in range(n):
            k = i + j
            aux[k].append(new_array[i][j])

    output = []
    for row in aux:
        output.append(''.join(row))

    return output

def get_diagonal_one_sided(array):
    letters = ['A']#['A','T','C','G']
    output = False
    aux = diagonalize(array)
    indexes = []
    
    for letter in letters:
        mask = []
        result = []
    
        for row in aux:
            mask.append([1 if element == letter else 0 for element in row])

        for row in mask:
            row_str = ''.join([str(element) for element in row])
            result.append(row_str.split('0'))

        for row in result:
            for element in row:
                if len(element) >= 4:
                    indexes.append(len(element))
    if indexes != []:
        output = True
    return output

def flip_rows(array):
    output = []

    indexes = list(range(len(array)))
    flipped_indexes = indexes[::-1]
    
    for i in flipped_indexes:
        output.append(array[i])
    return output

def get_diagonals(dna):
    output = False

    test_1 = get_diagonal_one_sided(dna)
    test_2 = get_diagonal_one_sided(flip_rows(dna))
    if any([test_1, test_2]):
        output = True

    return output

## Final function is_mutant

def is_mutant(dna):
    output = False
    
    check_hor = get_horizontal(dna)
    check_ver = get_vertical(dna)
    check_diag = get_diagonals(dna)

    if any([check_hor, check_ver, check_diag]):
        output = True
        
    return output