def print_lol(the_list, indent=False, tabs):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, tabs + 1)
        else:
            if indent:
                for i in range(tabs):
                    print("\t", end'')
            print(each_item)
