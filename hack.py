# Import the following modules
import random
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

# List of coding hacks, computer science facts, and shortcuts
facts = [
    "The first 1GB hard drive, released in 1980, weighed over 500 pounds and cost $40,000.",
    "The original name of Windows was Interface Manager.",
    "There are over 700 different programming languages.",
    "The term 'bug' was popularized in software engineering after a real moth was found in a relay of the Harvard Mark II computer in 1947.",
    "Programmer and inventor Hedy Lamarr also co-invented an early form of spread spectrum communication technology.",
    "Python is named after the British comedy series Monty Python's Flying Circus.",
    "Bill Gates' first program was a tic-tac-toe game.",
    "The QWERTY keyboard layout was designed to prevent typewriter jams.",
    "Every minute, 510,000 comments are posted on Facebook.",
    "The first computer programmer was Ada Lovelace in the 19th century.",
    "In 1956, 5 megabytes (MB) of data weighed a ton.",
    "The first-ever webcam watched a coffee pot at the University of Cambridge.",
    "The first website ever created is still online and is about the World Wide Web project.",
    "There are around 2 billion lines of code in Google’s codebase.",
    "The ‘@’ symbol was chosen for email addresses by Ray Tomlinson in 1971.",
    "Java was initially called Oak.",
    "The first known computer virus was called Creeper, created in 1971.",
    "In Morse code, 'SOS' was chosen because it is easy to transmit and recognize.",
    "If you type ‘Do a barrel roll’ into Google, the page will spin.",
    "You can play the dinosaur game on Google Chrome when you're offline by pressing spacebar.",
    "CAPTCHA stands for Completely Automated Public Turing test to tell Computers and Humans Apart.",
    "The Firefox logo isn’t a fox; it’s a red panda.",
    "The first email was sent by Ray Tomlinson to himself in 1971.",
    "The first computer mouse was made of wood.",
    "The first video game ever created was called Pong.",
    "PHP originally stood for Personal Home Page.",
    "The first domain name ever registered was symbolics.com.",
    "The word 'robot' comes from a Czech word that means 'forced labor'.",
    "Amazon was almost named Cadabra.",
    "The Apple II is the longest-running computer line ever, produced from 1977 to 1993.",
    "MySpace lost all its user data from 2003-2015 due to a server migration.",
    "Facebook’s blue color scheme is due to Mark Zuckerberg’s red-green color blindness.",
    "The first computer game, Spacewar!, was created in 1962.",
    "The world's first computer programmer was a woman, Ada Lovelace.",
    "Email existed before the World Wide Web.",
    "The most common password in the world is '123456'.",
    "Linux runs on all of the world’s top 500 supercomputers.",
    "The first version of Windows was released in 1985.",
    "The first programming language was called Assembly language.",
    "The first electronic computer, ENIAC, was the size of a large room and consumed as much power as several hundred modern PCs.",
    "Google was originally called Backrub.",
    "Approximately 90 percentage of the world's currency exists only on computers.",
    "In 2012, over 17 billion devices connected to the Internet.",
    "The most expensive domain name ever sold was carinsurance.com for nearly $50 million.",
    "One in eight marriages in the U.S. last year began online.",
    "Every minute, 300 hours of video are uploaded to YouTube.",
    "The first ever computer virus was a self-replicating program called 'The Creeper'.",
    "In 2010, a 75-year-old woman accidentally cut off Internet access to Armenia.",
    "The original Space Invaders arcade game caused a coin shortage in Japan.",
    "The first word ever spoken on the internet was 'lo'.",
    "In 1958, the inventor of the integrated circuit, Jack Kilby, was awarded the Nobel Prize in Physics.",
    "The first computer game ever created was called 'Tennis for Two'.",
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "In 1999, PayPal was voted one of the worst business ideas of the year.",
    "In 2004, a gaming enthusiast legally changed his name to 'Mr. Playstation'.",
    "The first banner ad on the internet was in 1994, and it had a 44% click-through rate.",
    "The Amazon logo represents a smile from A to Z.",
    "In Japan, letting a sumo wrestler make your baby cry is considered good luck.",
    "The first-ever domain name registered was 'symbolics.com' in 1985.",
    "The word 'algorithm' is derived from the name of the Persian mathematician Al-Khwarizmi.",
    "More than 2 billion people use Facebook every month.",
    "The term 'spam' is derived from a Monty Python skit.",
    "If you searched for 'askew' on Google, the page would tilt slightly.",
    "China has treatment camps for Internet addicts.",
    "The first computer programmer was a woman named Ada Lovelace, in the 1800s.",
    "The term 'cookie' in computing comes from the term 'magic cookie' used in Unix systems.",
    "The original name for JavaScript was Mocha.",
    "The creator of the iPod first offered the idea to Philips and RealNetworks, but they passed on it.",
    "Google's first doodle was a Burning Man symbol in 1998.",
    "The very first Apple logo featured Isaac Newton sitting under a tree.",
    "The first website to use 'cookies' was Netscape.",
    "The most common programming language in use today is JavaScript.",
    "The '@' symbol was chosen for email because it is rarely used in computing, and it separates the user from the host.",
    "The first email sent from space was sent by the crew of the space shuttle Atlantis in 1991.",
    "Apple's first logo featured Isaac Newton under an apple tree.",
    "The first computer virus was called 'Creeper'.",
    "Bluetooth technology was named after a 10th-century king, Harald Bluetooth.",
    "The first webcam watched a coffee pot at Cambridge University.",
    "The founder of Atari also started the Chuck E. Cheese chain.",
    "A 'jiffy' is an actual unit of time: 1/100th of a second.",
    "There are approximately 3.5 billion Google searches per day.",
    "The first web browser was called WorldWideWeb, later renamed Nexus.",
    "Doug Engelbart invented the computer mouse in 1964.",
    "If you type 'Google in 1998' in the Google search bar, you will see how it looked back then.",
    "In 2012, Apple sold 340,000 iPhones per day.",
    "Mark Zuckerberg, Facebook's CEO, suffers from red-green color blindness and sees the color blue best.",
    "The first programming language for kids was LOGO, created in 1967.",
    "About 70percentage  of all the malware in the world is targeted at Android devices.",
    "The average computer user blinks seven times a minute, less than half the normal rate of 20.",
    "Bill Gates' house was designed using a Macintosh computer.",
    "In Japan, more paper is used to print manga than toilet paper.",
    "The original Xbox contained edited sound files from the horror game Doom 3.",
    "The first ever YouTube video was uploaded on April 23, 2005, and it's titled 'Me at the zoo'.",
    "The first Apple computer, built by Steve Jobs and Steve Wozniak, was sold for $666.66.",
    "Nintendo was founded in 1889 as a playing card company.",
    "A computer as powerful as the human brain would be able to do about 38 thousand trillion operations per second and hold about 3,584 terabytes of memory.",
    "The first ever VCR, made in 1956, was the size of a piano.",
    "In 1994, a person from India sent the first e-mail.",
    "The name 'Wi-Fi' doesn’t actually mean anything. It’s a play on the word 'Hi-Fi'.",
    "Samsung is 38 years and 1 month older than Apple."
]


def get_random_fact(_):
    # Clear the screen
    clear()

    put_html("<p align='center'><h2><img src='https://miro.medium.com/v2/resize:fit:1200/1*daSIu2EPopPTN_CDmTrVIA.jpeg' width='7%'> Coding Facts Generator</h2></p>")

    # Select a random fact from the list
    random_fact = random.choice(facts)

    # Display the fact in blue color and large font
    style(put_text(random_fact), 'color:blue; font-size: 30px')
    put_buttons(
        [dict(label='More Facts', value='outline-success', color='outline-success')], onclick=get_random_fact)

# Driver Function
if __name__ == '__main__':
    # Put a heading "Coding Hack Generator"
    put_html("<p align='center'><h2><img src='https://miro.medium.com/v2/resize:fit:1200/1*daSIu2EPopPTN_CDmTrVIA.jpeg' width='7%'> Coding Facts Generator</h2></p>")

    # Put a Click me button
    put_buttons(
        [dict(label='More Facts', value='outline-success', color='outline-success')], onclick=get_random_fact)

    # Hold the session for a long time
    hold()
