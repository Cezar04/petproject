def create_header(input):
    header = []
    if type(input) == dict:   
        for details in input:
            formatted_header = details.replace("_", " ").capitalize()
            if formatted_header not in header:
                header.append(formatted_header)
    return header
