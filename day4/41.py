def count_word(file_name, word):
    with open(file_name, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    
    directions = [
        (0, 1),  
        (0, -1), 
        (1, 0),  
        (-1, 0),  
        (1, 1),  
        (-1, -1), 
        (1, -1), 
        (-1, 1),  
    ]
    
    count = 0

    def word_exists(r, c, dr, dc):
        for i in range(word_length):
            n_row, n_col = r + i * dr, c + i * dc
            if n_row < 0 or n_row >= rows or n_col < 0 or n_col >= cols or grid[n_row][n_col] != word[i]:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if word_exists(r, c, dr, dc):
                    count += 1

    return count


file_name = "input.txt"

result = count_word(file_name, "XMAS")
print(result)
