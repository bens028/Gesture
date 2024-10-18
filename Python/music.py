import time

def print_lyrics(lyrics):
    for line in lyrics:
        words = line.split()  
        for word in words:
            
            for char in word:
                print(char, end='', flush=True)  
                time.sleep(0.1) 
            print(' ', end='', flush=True) 
            time.sleep(0.5)
        print() 


lyrics = [
    "Yo, man,",
    "Yo, man,",
    "I just saw this girl,",
    "She looked so good.",
    "I had to get her number.",
    "But I knew, it wasn't me."
]

print_lyrics(lyrics)


