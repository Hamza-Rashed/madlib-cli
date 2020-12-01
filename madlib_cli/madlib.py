import re
path = '/home/hamza/Desktop/401/labs/lab3/madlib-cli/textFiles/began.txt'
def read_template(path):
    with open(path) as file:
        content = file.read()
    return content
    
def parse(doc):
    reg_exp_questions = re.findall(r"\{(.*?)\}", doc)
    return reg_exp_questions

def merge(txt,answers_arr):
    for str_loop in answers_arr:
        txt = txt.replace("{}",str_loop,1)
    return txt

def write():
    content = read_template(path)
    reg_exp_questions = parse(content)
    answers_arr = []
    for questions in reg_exp_questions:
        all_questions = input(f'Enter your {questions} : ')
        answers_arr.append(all_questions)
    result = merge(reg_exp_questions , answers_arr)
    with open(path, "a") as file_write:
        file_write.write(result)

    print("Lets Fun")
    print(result)

write()