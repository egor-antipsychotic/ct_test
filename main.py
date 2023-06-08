def data_input():
    import codecs
    with codecs.open('input_example.txt', 'r', 'utf-8') as read_file:
        raw_timesheet = read_file.read().replace('\r\n', ',').split(sep=',')
    return raw_timesheet


def data_transform(datafile):
    import re
    timesheet = {}
    for i in range(datafile.__len__()):
        name = ''.join(re.findall(r'\w*\D', datafile[i]))[0:-1]  # [0:-1] выполняет исключительно косметическую роль
        hours = re.findall(r'\d+$', datafile[i])
        if name not in timesheet:
            timesheet[name] = {
                'hours': hours[0],
                'total': int(hours[0])
            }
        else:
            timesheet[name]['hours'] += f', {hours[0]}'
            timesheet[name]['total'] += int(hours[0])
    return timesheet


def output_all(mod_data):
    for name in mod_data.items():
        print(f"{name[0]}: {name[1]['hours']}; sum: {name[1]['total']}")


def output_one(mod_data, *names):
    for name in names:
        print(f"{name}: {mod_data[name]['hours']}; sum: {mod_data[name]['total']}")


if __name__ == '__main__':

    # формирование словаря с данными
    transformed_data = data_transform(data_input())

    # вывод статистики по всем работникам
    output_all(transformed_data)

    # опциональный вывод статистики по работнику/работникам
    # output_one(transformed_data, 'Василий', 'Андрей1', 'Андрей 1')
