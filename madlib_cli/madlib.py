import re




def read_template(path):
    """
    Reads and returns the contents of a file located at the specified path.

    Args:
        path (str): The path to the file to be read.

    Returns:
        str: The contents of the file, with leading and trailing white space removed.
    """
    with open(path, 'r') as f:
        return f.read().strip()
    

def parse_template(template):

    """
    Parses a template string and returns a tuple consisting of the stripped template string and a tuple of its placeholders.

    Args:
        template (str): The template string to be parsed.

    Returns:
        tuple: A tuple containing the stripped template string and a tuple of its placeholders.
    """
    
    regex = re.compile(r"{(.+?)}")
    
    parts = regex.findall(template)
    
    stripped_template = regex.sub('{}', template)
    
    return stripped_template, tuple(parts)


    

def merge(template, words):
     """
    Merges a given template string with a list of words and returns the resulting string.

    Args:
        template (str): The template string to be merged.
        words (list): A list of words to be inserted into the template.

    Returns:
        str: The merged string, with the placeholders in the template replaced by the corresponding words.
    """
     return template.format(*words)
    

def madlib():
    """
    Prompts the user to enter words for a madlib template and returns the resulting story.

    Returns:
        str: The completed madlib story string.
    """
    path = "./assets/madlib.txt"
    template = read_template(path)
    stripped_template, parts = parse_template(template)
    words = []
    for part in parts:
        word = input(f"Please enter a {part}: ")
        words.append(word)
    return merge(stripped_template, words)



def write_madlib(madlib):
    """
    Writes the given madlib string to a file located at a specified path.

    Args:
        madlib (str): The madlib string to be written to the file.
    """
    path = "./assets/madlibWriteResult.txt"
    with open(path, 'w') as f:
        f.write(madlib)

if __name__ == "__main__":
    print("Welcome to the Madlib generator! This program will ask you to enter various words, and then use them to create a funny story.")
    result = madlib()
    print(result)
    write_madlib(result)

