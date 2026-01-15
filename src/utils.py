def print_dict_as_table(dictionary, title="Table"):
    """
    Prints any dictionary in a neat table-like format.

    """
    print(f"\n=== {title} ===")
    for key, value in dictionary.items():
        print(f"{key:<20} : {value}")
    print("====================\n")
