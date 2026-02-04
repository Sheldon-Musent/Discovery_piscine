#!/usr/bin/env python3

Table_of_num = 0

while Table_of_num <= 10:
    multi_how_many_times = 0
    the_line = f"Table_of {Table_of_num}:"
    while multi_how_many_times <= 10:
        the_line += f" {Table_of_num * multi_how_many_times}"
        multi_how_many_times += 1
    print(the_line)
    Table_of_num += 1