
def convert_integer_to_string(phone_number):
    return str(phone_number)

def create_section_one(converted_string):
    section_one = converted_string[0:3]
    return section_one

def create_section_two(converted_string):
    section_two = converted_string[3:6]
    return section_two

def create_section_three(converted_string):
    section_three = converted_string[6:10]
    return section_three

def concatenate_strings(split_one, split_two, split_three):
    final_string = "(" + split_one + ") " + split_two + "-" + split_three
    return final_string

def create_phone_number(integer):
    converted_string = convert_integer_to_string(integer)
    section_one = create_section_one(converted_string)
    section_two = create_section_two(converted_string)
    section_three = create_section_three(converted_string)
    return concatenate_strings(section_one, section_two, section_three)






