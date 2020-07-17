def word_count(s):
    # Your code here

    string_list = {}
    lower_string = s.lower()
    ignored_chars = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

    for char in ignored_chars:
        lower_string = lower_string.replace(char, "")

    for word in lower_string.split():
        if word == "":
            continue
        if word not in string_list:
            string_list[word] = 1
        else:
            string_list[word] += 1
    return string_list


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))