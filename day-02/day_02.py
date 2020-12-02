def read_file_to_array(file):
    with open(file, 'r') as file:
        passwords = [line.strip() for line in file]
        return passwords


def validate_password_old_job(passwords):
    valid_passwords = 0
    for line in passwords:
        counts, c, password = line.split()
        at_least, at_most = counts.split("-")
        c = c[0]

        if int(at_least) <= password.count(c) <= int(at_most):
            valid_passwords += 1

    return valid_passwords


def validate_password_toboggan_policy(passwords):
    valid_passwords = 0
    for line in passwords:
        counts, c, password = line.split()
        at_least, at_most = counts.split("-")
        c = c[0]

        if (password[int(at_least)-1] == c) ^ (password[int(at_most)-1] == c):
            valid_passwords += 1

    return valid_passwords


print(validate_password_old_job(read_file_to_array("input.txt")))
print(validate_password_toboggan_policy(read_file_to_array("input.txt")))
