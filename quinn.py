from itertools import permutations


nums = [x for x in range(-5, 6)]
first_rows = list(permutations(nums, 9))
last_values = []


for first_row in first_rows:
    invalid = False
    for i in range(1, len(first_row)):
        if first_row[i] == first_row[i-1] + 1 or first_row[i] == first_row[i-1] - 1:
            invalid = True
            break
    if not invalid:
        _sum = [max(first_row)-min(first_row)]
        current_row = first_row
        while len(_sum) < 9:
            new_row = []
            for i in range(1, len(current_row)):
                new_row.append(current_row[i]+current_row[i-1])
            if len(new_row) > 1:
                _sum.append(max(new_row)-min(new_row))
            else:
                _sum.append(new_row[0])
            current_row = new_row
        last_values.append(sum(_sum))

print(first_rows[last_values.index(max(last_values))])
print(max(last_values))




    







        
