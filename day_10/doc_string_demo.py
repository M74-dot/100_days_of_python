def format_name(f_name, l_name):
    """ take first name and last name and 
    return its title case version """
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

f_name = input('Enter your first name: ')
l_name = input('Enter your last name: ')
name = format_name(f_name, l_name)
print(f"Formatted name is {name}")
