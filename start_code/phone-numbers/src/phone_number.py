
def change_int_to_new_string(phone_number):
    phone_number_string = str(phone_number)
    first_3_chars = phone_number_string[:3]
    next_3_chars = phone_number_string[3:6]
    last_4_chars = phone_number_string[6:10]
    
    final_string = "(" + first_3_chars + ") " + next_3_chars + "-" + last_4_chars
    return final_string








