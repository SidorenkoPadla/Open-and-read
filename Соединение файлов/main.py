def combining(list_of_file):
    list_of_file = list_of_file.split()
    print(list_of_file)
    dict_file = {}
    for file in list_of_file:
        with open(file,'rt', encoding= 'utf-8') as file_o:
            count_file = [row.rstrip() for row in file_o]
            dict_file[len(count_file)] = file
        file_o.close()
    numbers = sorted(dict_file.keys())

    for number in numbers:
        with open(dict_file.get(number), 'r', encoding= 'utf-8') as firstfile, open('txt4', 'a', encoding= 'utf-8') as secondfile:
            secondfile.write(dict_file.get(number))
            secondfile.write('\n')
            secondfile.write(str(number))
            secondfile.write('\n')
            for line in firstfile:
                secondfile.write(line)
            secondfile.write('\n')
            secondfile.write('\n')
        firstfile.close()
        secondfile.close()
    print(open('txt4'))

combining('txt1 txt2 txt3')
