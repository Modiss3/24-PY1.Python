# TODO Найдите количество книг, которое можно разместить на дискете

memory_size_Mb = 1.44

memory_size = memory_size_Mb * (1024 ** 2)
pages_num = 100
lines_per_page = 50
symbols_per_line = 25
symbol_size = 4

data_per_book = pages_num * lines_per_page * symbols_per_line * symbol_size

print("Количество книг, помещающихся на дискету:", int(memory_size//data_per_book))
