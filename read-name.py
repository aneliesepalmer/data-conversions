with open('name.txt') as my_name:
    full_text = my_name.read()

sentence = "Hello, my name is " + full_text

with open('hello.txt', 'w') as f:
    f.write(sentence)