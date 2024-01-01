#WAP to fetch data from csv file and display in a table without libraries
filename = 'industry.csv'

# Open the file
with open(filename, 'r') as file:
    headers = file.readline().strip().split(';')
    # Initialize the data list
    data = []
    
    for line in file:
        values = line.strip().split(';')
        data.append(values)

# Calculate the maximum width for each column
col_widths = [max(len(header), *(len(str(value)) for value in column)) for header, column in zip(headers, zip(*data))]

# Print the headers
print(' | '.join(header.ljust(width) for header, width in zip(headers, col_widths)))
# Print a separator
print('-' * (sum(col_widths) + 3 * (len(headers) - 1)))

# Print the data
for row in data:
    print(' | '.join(str(value).ljust(width) for value, width in zip(row, col_widths)))


