def get_data_from_files(list_of_files: list) -> list:
    """Считывает данные из файлов из списка 'list_of_files'.
    Возвращает список, каждый элемент которого - список строк из файла и название файла, как последний элемент списка.
    Список отсортирован по количеству элементов вложенных списков.
    """
    list_of_contents_of_all_files = []    
    for file in list_of_files:
        strings_from_file = []
        with open(file, 'rt', encoding='utf-8') as source:
            for line in source:
                strings_from_file.append(line)
            strings_from_file.append(file)
            list_of_contents_of_all_files.append(strings_from_file)
    list_of_contents_of_all_files.sort()
    return list_of_contents_of_all_files


def write_overall_files_date_to_file(list_of_contents_of_all_files, appointed_file='overall.txt'):
    """Записывает элементы списка, полученного от функции 'get_data_from_files('list_of_files')'.
    Элементы записываются в порядке от последнего к первому.
    """
    with open(appointed_file, 'wt', encoding='utf-8') as file:
        for i in range(len(list_of_contents_of_all_files)-1,-1,-1):
            file.write(f'{list_of_contents_of_all_files[i][-1]}\n{len(list_of_contents_of_all_files[i])-1}\n')
            for k in range(0, len(list_of_contents_of_all_files[i])-1):
                file.write(f'{list_of_contents_of_all_files[i][k]}')
            file.write('\n')


list_of_files = ['1.txt', '2.txt', '3.txt']

write_overall_files_date_to_file(get_data_from_files(list_of_files))