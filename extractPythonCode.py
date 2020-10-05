"""Extract Python code from inginious text file and export XML files"""
import os
import shutil
import sys
import subprocess


def search_string(file_name, string_to_search):
    """search grade or username in the text file"""
    # Open the file in read only mode
    output_string = "0"
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                output_string = line.split(":")[1]
                output_string = output_string.replace("\'", "")
                break
        read_obj.close()
    return output_string.strip()


def search_code(file_name):
    """search python code in the text file"""
    # Open the file in read only mode
    start_string = "q1:"
    end_string = "test:"
    output_string = ""
    # open text file
    f = open(file_name, 'r')
    line = f.readline()
    while start_string not in line:
        line = f.readline()
    # read next line
    line = f.readline()
    # skip empty line
    while len(line.strip()) == 0:
        line = f.readline()
    # count number of space before method
    num_space = len(line) - len(line.lstrip())
    # read Python code
    while end_string not in line:
        output_string += line[num_space:]
        line = f.readline()
    # close fle
    f.close()
    # return Python code
    return output_string


def create_py(input_file_name, output_dir):
    """find python code and save it to .py file"""
    grade = search_string(input_file_name, "grade")
    username = search_string(input_file_name, "username")
    source_code = search_code(input_file_name)

    output_file_name = ""
    if float(grade) > 50.0:
        output_file_name = output_dir + "/pos/" + username + "_" + grade + ".py"
    else:
        if float(grade) > 0.0:
            output_file_name = output_dir + "/nag/" + username + "_" + grade + ".py"
    if output_file_name != "":
        f = open(output_file_name, "w")
        f.write(source_code)
        f.close()


def find_all(name, path):
    """collect all file names in a directory"""
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


def convert(input_dir, output_dir):
    """convert python code to xml"""
    # create output directory
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)
    os.mkdir(output_dir+"/pos")
    os.mkdir(output_dir + "/nag")

    # create Python file
    files = find_all("submission.test", input_dir)
    for file in files:
        create_py(file, output_dir)

    # export XMLs
    for sub_dirs in os.listdir(output_dir):
        for file in os.listdir(output_dir+"/"+sub_dirs):
            if file.endswith(".py"):
                output_file = output_dir + "/" + sub_dirs + "/" + file
                xml_output_file = output_dir + "/" + sub_dirs + "/" + file[0:len(file)-2] + "xml"
                command = "py2xml " + output_file + " > " + xml_output_file
                # if python code has errors, i.e, syntax error, special characters, etc
                # then delete the equivalent xml file
                re = subprocess.getoutput(command)
                # if the python has error, e.g, syntax error, then delete the correspond xml
                if len(re) > 0:
                    # print(command)
                    # print(re)
                    if os.path.exists(xml_output_file):
                        os.remove(xml_output_file)


""" convert all text files into xml files """
input_path = sys.argv[1]
output_path = sys.argv[2]
convert(input_path, output_path)
