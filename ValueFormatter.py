import os

def format_values(styletype):

    type_list = ['s','i','il']

    new_file = 'formattedfiles.txt'
    format_type = styletype.strip() 

    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        formatted_file = open(new_file, mode='w')
        control = 0
        line_control = True

        if format_type not in type_list:
            formatted_file.write('Unknown style type, must be either s,i or il. you used "{}" !'.format(format_type))
            return

        with open(os.path.join(__location__,"values.txt"), "r") as raw_file:
            for line in raw_file:

                if bool(line.strip()) == True:

                    if format_type == 'il' and line_control == True:
                        formatted_file.write('(')
                    elif format_type == 'il' and line_control == False:
                        formatted_file.write(',(')

                    if format_type == 's' or format_type == 'il':
                        for word in line.split():
                            if control == 0:
                                formatted_file.write("'{}',".format(word))
                                control += 1
                            elif control == 1:
                                formatted_file.write("'{}'".format(word))
                                control += 1
                            else:
                                formatted_file.write(",'{}'".format(word))

                    elif format_type == 'i':
                        for word in line.split():
                            if control == 0:
                                formatted_file.write("('{})',".format(word))
                                control += 1
                            elif control == 1:
                                formatted_file.write("('{}')".format(word))
                                control += 1
                            else:
                                formatted_file.write(",('{}')".format(word))

                    if format_type == 'il' and line_control == True:
                        formatted_file.write(')')
                        line_control = False
                    elif format_type == 'il' and line_control == False:
                        formatted_file.write(')')

            control = 0
                    
    except OSError as e:
        print(e)

    raw_file.close()
    formatted_file.close()

if __name__ == '__main__': 

    print('s for select i for insert or il for insert per line')
    style_type = input('Enter formatting type: ')

    format_values(style_type.lower()) #s for select i for insert or il for insert per line