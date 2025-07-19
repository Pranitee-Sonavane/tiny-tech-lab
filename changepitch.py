import pyttsx3

engine = pyttsx3.init()

# Pick your favorite voice index from previous test
voice_id = engine.getProperty('voices')[2].id  # Change this index!
engine.setProperty('voice', voice_id)

# Change speed (default ~200, lower = slower, higher = faster)
engine.setProperty('rate', 150)

# Change volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)

engine.say("Hello sleepyhead! This is your sassy driving fairy speaking. You better not be yawning again or I’m honking your brain.")
engine.runAndWait()
