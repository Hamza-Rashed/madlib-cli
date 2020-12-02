import re
path = '/home/hamza/Desktop/401/labs/lab3/madlib-cli/textFiles/began.txt'
def read_template(path):
    """
    Create and test a read_template function that takes in a path to text 
    file and returns a stripped string of the file’s contents.
    """
    with open(path) as file:
        content = file.read()
    return content
    
def parse(doc):
    """
    Create and test a parse function that takes in a template string and 
    returns a string with language parts removed and a separate list of those language parts.
    """
    reg_exp_questions = re.findall(r"\{(.*?)\}", doc)
    return reg_exp_questions

def merge(txt,answers_arr):
    """
    Create and test a merge function that takes in a “bare” template and a list of user
    entered language parts, and returns a string with the language parts inserted into the template.
    """
    for str_loop in answers_arr:
        txt = txt.replace("{}",str_loop,1)
    return txt

def write():
    """
    Create write function for write a new info inside a new file called finall.txt
    """
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
