import random
print()
print("=====================================")
print("| Welcome to Random Story Generator |")
print("|      created by Aditya Singh      |")
print("| of Lovely Professional University |")
print("|          Section: K22FG           |")
print("|         Roll No: RK22FGA07        |")
print("=====================================")
print()
while True:
      n=int(input("Press 1 to generate story and 2 to exit: "))
      print()
      if n == 1:
            Sentence_starter = ['About 300 years ago', ' In the 20 BC','Once upon a time', 'Back in the days']
            character = [' there lived a queen.', ' there was a woman named Ayesha.',' there lived a small girl Adeena.']
            time = [' One day', ' One full-moon night']
            story_plot = [' she was passing by', ' she was going to ']
            place = [' the mountains.', ' the garden.']
            second_character = [' She saw a old man', ' She saw a young boy']
            age = [' who seemed very tired', ' who seemed very poor']
            work = [' searching something.', ' digging a well on roadside.']
            story = [' Within no time she started narrating a story,',
                 ' Suddenly she began with a story,']
            when = [' "A few years ago', ' "Yesterday',
                ' "Last night', ' "A long time ago', ' "On 20th Jan']
            who = [' a rabbit', ' an elephant', ' a mouse', ' a turtle', ' a cat']
            bridge = [' named', ' whose name was']
            name = [' Ali', ' Miriam', ' Daniel', ' Hoouk', ' Starwalker']
            bridge2 = [' who lived in', ' of native']
            residence = [' Barcelona', ' India', ' Germany', ' Venice', ' England']
            bridge3 = [' went to the', ' travelled to the']
            went = [' cinema', ' university', ' seminar', ' school', ' laundry']
            happened = [' and made a lot of friends."', ' and ate a burger."',
                    ' and found a secret key."', ' and solved a mistery."', ' and wrote a book."']
            print(random.choice(Sentence_starter)+random.choice(character) +random.choice(time)+random.choice(story_plot) +random.choice(place)+
                  random.choice(second_character) +random.choice(age)+random.choice(work) + random.choice(story) + random.choice(when) +
                  random.choice(who) + random.choice(bridge) + random.choice(name) + random.choice(bridge2) + random.choice(residence) +
                  random.choice(bridge3) + random.choice(went) + random.choice(happened))
            print()
      elif n==2:
            print("Thank you for using Random Story Generator! Have a nice day.")
            print()
            break
      else:
            print("Invalid Input! Try again.")
            print()
