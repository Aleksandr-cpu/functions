calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(str):
    lst = []
    count = len(str)
    lst.append(count)
    lst.append(str.upper())
    lst.append(str.lower())
    result = (lst)
    count_calls()
    return result

def is_contains(string, list_to_search: list):
    result = 0
    for i in list_to_search:
        if i.lower() == string.lower():
            result = 1
    if result == 1:
        count_calls()
        return True
    else:
        count_calls()
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
