def data_input():
    import codecs
    with codecs.open('input_example.txt', 'r', 'utf-8') as read_file:
        raw_timesheet = read_file.read().replace('\r\n', ',').split(sep=',')
    return raw_timesheet


def data_transform(datafile):
    import re
    timesheet = {}
    for i in range(datafile.__len__()):
        name = ''.join(re.findall(r'\w*\D', datafile[i]))[:-1]
        hours = re.findall(r'\d+$', datafile[i])
        if name not in timesheet:
            timesheet[name] = hours
        else:
            timesheet[name] += hours
    return timesheet


def output_all(mod_data):
    final_data = ''
    for name, hours in mod_data.items():
        lc = [int(i) for i in hours]
        final_data += f"{name}: {str(lc)[1:-1]}; sum: {sum(lc)}\n"
    return final_data


def output_some(mod_data, *names):
    final_data = ''
    for name in names:
        lc = [int(i) for i in mod_data[name]]
        final_data += f"{name}: {str(lc)[1:-1]}; sum: {sum(lc)}\n"
    return final_data


if __name__ == '__main__':
    # формирование словаря с данными
    transformed_data = data_transform(data_input())

    # вывод статистики по всем работникам
    print(output_all(transformed_data))

    # опциональный вывод статистики по работнику/работникам
    print(output_some(transformed_data, 'Василий'))
