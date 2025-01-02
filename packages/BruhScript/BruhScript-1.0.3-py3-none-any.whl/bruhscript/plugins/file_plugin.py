def file_write(filename, content, variables):
    with open(filename, "w") as file:
        file.write(content)
    return {"status": "success"}

def file_read(filename, variables):
    with open(filename, "r") as file:
        content = file.read()
    return {"file_content": content}
