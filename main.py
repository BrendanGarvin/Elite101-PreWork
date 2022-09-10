keepGoing = True

def Emotions(response):
  if 'complicated' in response:
    print('Emotions really are complicated, huh?')
  elif 'brain' in response:
    print('You\'re a sciencey type, aren\'t you?')
  elif 'soul' in response:
    print('Such a spiritualistic answer, nice!')
  elif 'feel' in response:
    print('Emotions are simply feelings we feel, right?')
  else:
    print('I hadn\'t thought about it like that.')

def Career(response):
  
  goodResponse = ['yeah', 'yes', 'definitely', 'absolutely', 'y']
  badResponse = ['no', 'nah', 'not really', 'kinda', 'n']
  
  if 'computer' in response:
    feeling = input('Do you like computers? ').lower
    
    if feeling in goodResponse:
      print('It\'s good to do something you love!')
    elif feeling in badResponse:
      print('Maybe you should think about doing something you like?')
    else:
      print('Ok.')
      
  elif 'engineer' in response:
    feeling = input('That\'s a complicated field, are you up for the task? ')

    if feeling in goodResponse:
      print('That\'s good that you feel confident!')
    elif feeling in badResponse:
      print('Have some more confidence, you can do it!')
    else:
      print('Ok.')

  elif 'finance' in response:
    print('Money really makes the world go round.')
    
  elif 'accounting' in response:
    print('Businesses would really love you!')
    
  elif 'construction' in response:
    print('That\'s a great field! You must be very strong.')
    
  elif 'truck' in response:
    print('A very neccesary job for everyone.')
    
  elif 'attend' in response:
    feeling = input('Do you like interacting with people? ')

    if feeling in goodResponse:
      print('This field would be great for you!')
    elif feeling in badResponse:
      print('Maybe you could find a job that deals with less people?')
    else:
      print('Ok.')
    
  else:
    print(f'That\'s a nice career to go in, {name}!')
  

name = input('What\'s your name? ')
print(f'Nice to meet you, {name}!\n')

while keepGoing:
  emotions = input('How do you think people feel emotion? ').lower()
  if emotions == 'q':
    keepGoing = False
    print('Thanks for chatting!')
    break
  Emotions(emotions)
  print('')
  
  careers = input('What career do you want to go in / are in? ').lower()
  if careers == 'q':
    keepGoing = False
    print('Thanks for chatting!')
    break
  Career(careers)
  print('')
