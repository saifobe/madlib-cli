import re




def read_template(path):
    with open(path, 'r') as f:
        return f.read().strip()
    

def parse_template(template):
    
    regex = re.compile(r"{(.+?)}")
    
    parts = regex.findall(template)
    
    stripped_template = regex.sub('{}', template)
    
    return stripped_template, tuple(parts)


    

def merge(template, words):
    return template.format(*words)
    

def madlib():
    path = "./assets/madlib.txt"
    template = read_template(path)
    stripped_template, parts = parse_template(template)
    words = []
    for part in parts:
        word = input(f"Please enter a {part}: ")
        words.append(word)
    return merge(stripped_template, words)

def write_madlib(madlib):
    path = "./assets/madlibWriteResult.txt"
    with open(path, 'w') as f:
        f.write(madlib)

if __name__ == "__main__":
    print("Welcome to the Madlib generator! This program will ask you to enter various words, and then use them to create a funny story.")
    result = madlib()
    print(result)
    write_madlib(result)

