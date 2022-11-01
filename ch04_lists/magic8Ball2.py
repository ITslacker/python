import random
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
print(messages[random.randint(0, len(messages -1))]) # you'll get a random number between 0 and the value of len(messages) -1. you can add and move strings in messages    
                                                    ## without changing other lines of code