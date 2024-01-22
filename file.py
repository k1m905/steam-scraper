import csv

def save(fileName, games):
    file = open(f'{fileName}.csv','w', newline='')
    writer = csv.writer(file)
    writer.writerow([
    'Title', 
    'Discount Rate', 
    'Original Price [C$]', 
    'Final Price [C$]',
    'Link'
    ])

    for game in games:
        writer.writerow(game.values())
    file.close()