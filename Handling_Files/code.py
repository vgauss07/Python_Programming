## Read a Whole File
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)

## Read a file line by line
with open('file.txt', 'r') as file:
    for line in file:
        print(line) 

## To remove the spaces use the strip method
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())

## Writing a File (Overwriting)
with open('file.txt', 'w') as file:
    file.write('Jeffrey, Founder of Ace Dynamics!\n')
    file.write('Successful Mathematician and ML Engineer.')

## Write a file without Overwriting
with open('file.txt', 'a') as file:
    file.write(' Voracioous Learner')