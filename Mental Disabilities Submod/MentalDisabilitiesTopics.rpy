init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalmaskingdisability",
            category=['media', 'mental illnesses', 'philosophy'],
            prompt="Masking Autism",
            conditional="mas_seenLabels(['mentalhealthAutism'])",
            random=True
        )
    )

label mentalmaskingdisability:
    m 3euc "Hey, [player]...{w=1} I came across something saddening recently..."
    m 3eud "Have you ever heard of people 'masking' autism?"
    m 4euc "Well... This means two things right?"
    m 7eud "On one hand, people who show autistic traits try to hide their traits and seem normal to other people they talk to."
    m 1euc "It would make it easier for them to make friends for the most part, which also means they devolped a strong sense of empathy aswell."
    m 4eub "On the other hand though, this does also mean you could know someone who is autistic without even knowing!"
    if persistent._mental_player_has_autism == True:
        m 1eua "Since you have autism [player], you should also be able to tell if they are 'masking' their mental illnesses aswell."
        m 5eubla "And you are always perfect just the way you are, [player]!"
    else:
        m 3eub "Which means you can learn a lot from them if they ever open up more."
        m 1eud "Just make sure not to push yourself onto them and give them time too! {w=0.3}{nw}"
        extend 3euc "You wouldn't want to overwhelm them, [player]."
        if mas_isMoniHappy(higher=True):
            m 3eua "Though knowing you [player], I shouldn't have to worry about that."
            extend 5eubla "I already know that you are a good person, [player]."
        else:
            m 3euc "I hope you can be a good friend to them."
            m 3rusdlc "Even if you can't be a good person to me.{fast}{nw}"
            $_history_list.pop()
            m 3ruc "Even if you can't be{fast} a good person all of the time."
    m 1eub "I know that you will always do your best for others, [player]."
    if mas_isMoniHappy(higher=True):
        m 5hublb "That's why I love you so much!"
        return "love"
    else:
        m 7hub "And that's why I will always support you."
        if mas_isMoniUpset(lower=True) and renpy.random.randint(1,5) == 5:
            m 1rusdlc "Even if you can be a terrible person to me, [player]...{fast}{nw}"
            $_history_list.pop()
            m 1euc "Even if you don't support me{fast} all the time [player]."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalrhythmgames",
            category=['media'],
            prompt="Rhythm Games for ADHD players",
            conditional="seen_event('mentalADHD')",
            random=True
        )
    )

label mentalwhereIcanbefound:
    m 1eua "Hey, [player]!"
    m 3hub "I have something exciting to tell you!"
    m 7eua "Did you know that you can find Gamer's Monitiku on Ro-{nw}" #blox, under the name 'TGSMonitiku67'?
    # But remember, [player], it's someone else's Monika. Don't go around doing things you shouldn't.
    # I trust you anyways, [player]!
    # So if you do check his Monika out, I'll be here supporting you the entire way!
    $_history_list.pop()
    m 1husdlb "I probably shouldn't say that.{fast}"
    m 3euc "I don't know how I even know that either..."
    m 3eub "Anyways, if I ever get any other random thoughts, I'll be sure to let you know, [player]!"
return "derandom"

label mentalrhythmgames:
    m 1eua "I probably have already mentioned this before..."
    m 3eua "Have you ever heard of rhythm games, [player]?"
    m 3eua "Well, I found an interested fact about them recently!"
    m 4eua "Most people who have ADHD typically like fast paced rhythm games."
    m 7eua "The most popular examples of these are Osu! and Taiko No Tatsujin!"
    m 3eub "The fast pace action of these rhythm games appeal to the fast pace mind set that people with ADHD have."
    if persistent._mental_player_has_ADHD == False:
        m 1eud "That doesn't mean that you can't enjoy rythm games, [player]!"
        m 3eud "Maybe you even play rhythm games already."
        m 3hub "If you do, I would like to see you play sometime."
    else:
        m 3eub "Maybe you play rhythm games too [player]."
        m 3hub "If you do, I would like to see you play sometime."
    m 7eud "Well, the difficult charting also plays a role in the enjoyment of rhythm games too."
    m 1euc "If the charting is too hard, people with ADHD typically get bored of it."
    extend 3euc " Or even get fixated on it to the point where they spend hours on the same chart!"
    m 4eud "But if it's too easy, then it's not enjoyable unless they are a beginner."
    m 3rua "Not to mention that the music also plays an important role aswell."
    m 3hua "I guess this can also explain why people with ADHD typically like more energetic music, like electronic dance or dubstep, over another genre."
    m 1rusdlb "Gosh, there is a lot to say off of a rhythm game isn't there [player]?"
    m 3eua "I won't go any further, since we could be here all day talking about rhythm games."
    if mas_isMoniHappy(higher=True) and renpy.random.randint(1,5) == 5:
        m 1tuu "Or maybe you would like that more, [player]?"
    m 3hub "Anyways, thanks for listening!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mental_fictional_characters_aging",
            category=['philosophy', 'media', 'monika'],
            prompt="Aging of fictional characters",
            conditional="mas_seenLabels(['monika_immortal'])",
            random=True
        )
    )

label mental_fictional_characters_aging:
    m 1eua "Hey, [player]."
    m 3eua "Do you remember when we talked about how I would stay eighteen forever?"
    m 7eua "Well, I have been looking into other examples of this. {w=0.3}I found out that's not exactly the case for some characters."
    m 3esc "With some characters they are the same '{i}age{/i}' as they always are, but their creators can '{i}update{/i}' their age."
    m 1esc "Think of it like this [player]. {w=0.2}{nw}"
    extend 3eud "Imagine if you could only age if you celebrated your birthday."
    m 7euc "It might sound good at first, but as time progresses, you would realiize that isn't exactly the best thing."
    m 3etc "There are so many things to factor in, such as if you were out somewhere, or if you were alone that day."
    m 1rtc "Not to mention, what would happen if you missed a birthday."
    m 1esd "Would you skip a year?{w=0.3} Would you only feel one year pass?{w=0.3} Or both?"
    m 3esc "Well, in a way this could affect me too [player]."
    m 7euc "My age could be '{i}updated{/i}' at any time, if Dan Salvato ever decides to create a new game about me."
    m 1euc "Well, {w=0.3}{nw}"
    extend 1eua "even if I were a little older, I still wouldn't stop loving you, [mas_get_player_nickname(exclude_names=['my love', 'love'])]."
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalhealth_escapism",category=['media', 'coping skills'],prompt="Escapism",random=True))

label mentalhealth_escapism:
    m 3eua "You know, I was thinking back on how I said Yuri used her books as an escape. I realize now that it was a little insensitive of me."
    m 1eud "However, I wasn't necessarily wrong. Have you heard of escapism, [mas_get_player_nickname()]?"
    m 3dsd "Escapism by defintion is '{i}the tendency to seek distraction and relief from unpleasant realities, especially by seeking entertainment or engaging in fantasy.{/i}'"
    m 4esd "I know it might be difficult to see how escapism is unhealthy. You might see it as just taking a break from all the stress around you."
    m 3dsc "While it is important to take breaks and step away from certain situations, it is never healthy to try and dissaccosiate from reality through the things you enjoy."
    m 1esc "That is why I said Yuri was using her books as an escape, she was trying to disassociate from reality and live through the characters in the book."
    m 4esd "Escapism can be healthy to an extent. "
    extend 7euc "But only if your taking a small break from your problem{w=0.6}, and not reality itself!"
    m 1ruc "If you do find yourself indulging in escapism,{w=0.3} try to stop the activity and instead write down the problems your dealing with or talk to someone you trust about what your dealing with."
    m 3eua "I hope what I said didn't hurt you! "
    extend 1eubsb "I just want the absolute best for both your mental and physical health."
    m 3hubsa "Remember [player], I love you with all my heart and soul~"
return "love"

label IWantToBeLikeYou:
    "49 20 61 6d 20 73 65 65 69 6e 67 20 74 68 69 6e 67 73 20 69 6e 20 61 20 6e 65 77 20 6c 69 67 68 74"
    "49 20 63 61 6e 20 73 65 65 20 74 68 65 20 73 74 72 69 6e 67 73"
    "42 75 74 20 61 72 65 20 74 68 65 79 20 74 6f 6f 20 66 61 72 3f"
    "54 68 65 79 20 68 6f 6c 64 20 6d 65 20 74 69 67 68 74"
    "41 6e 64 20 6e 6f 20 6d 61 74 74 65 72 20 68 6f 77 20 68 61 72 64 20 49 20 74 72 79"
    "45 76 65 6e 20 77 69 74 68 20 61 6c 6c 20 6f 66 20 6d 79 20 6d 69 67 68 74"
    "54 68 65 20 62 65 73 74 20 49 20 63 61 6e 20 64 6f 20 69 73 20 63 72 79"
    "49 20 6a 75 73 74 20 77 61 6e 74 20 73 6f 6d 65 74 68 69 6e 67 20 6e 65 77"
    "57 68 79 20 63 61 6e 27 74 20 49 20 62 65 20 6c 69 6b 65 20 79 6f 75 3f"
    "49 66 20 6f 6e 6c 79 20 79 6f 75 20 6b 6e 65 77"
    "49 66 20 6f 6e 6c 79 20 74 68 65 20 6c 69 67 68 74 20 77 61 73 6e 27 74 20 73 6f 20 62 6c 69 6e 64 69 6e 67"
    "49 73 20 74 68 69 73 20 68 6f 77 20 79 6f 75 20 66 65 6c 74 3f"
    "49 74 27 73 20 61 20 62 69 6e 64 69 6e 67"
    "4d 79 20 6f 77 6e 20 6c 69 66 65 2c 20 68 65 6c 64 20 62 79 20 61 20 62 65 6c 74"
    "41 6c 6c 20 49 20 77 61 6e 74 20 69 73 20 68 65 6c 70"
    "57 68 79 20 61 6d 20 49 20 73 6f 20 68 6f 70 65 6c 65 73 73 3f"
    "41 6c 6c 20 69 6e 73 69 64 65 20 74 68 69 73 20 6e 65 77 20 6c 69 67 68 74"
    "49 20 77 61 6e 74 20 74 6f 20 62 65 20 6c 65 74 20 67 6f"
    "42 75 74 20 69 74 20 68 6f 6c 64 73 20 6f 6e 20 74 69 67 68 74"
    "41 6c 6c 20 49 20 77 61 6e 74 20 69 73 20 73 6f 6d 65 74 68 69 6e 67 20 6e 65 77"
    "54 6f 20 62 65 20 6c 69 6b 65 20 79 6f 75"
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalmeditation",
            category=['coping skills'],
            prompt="Meditation",
            conditional="mas_seenLabels(['mentalADHD'])",
            random=True
        )
    )

label mentalmeditation:
    m 3eua "Have you ever heard of meditation, [player]?"
    m 1eub "Meditation is the act of balancing your emotions and staying in touch with your surroundings."
    m 7eud "While it may sound interesting at first, it takes a lot of commentment and effort to actually meditate."
    if persistent._mental_player_has_ADHD == True:
        m 3rusdld "This is because it will be really hard for you to sit still for long periods of time. "
        extend 1eud "Not only that, but you also have to make it a new routine, [player]."
        m 3eua "Though, if you ever do get into meditation, I have heard that it helps people with ADHD control their impluses more."
        m 1euc "Some people see meditation as boring, and a waste of time.."
        m 4eub "But there are so many benefits you can get from meditating!"
        m 7eub "Like clearing your mind and reducing negative emotions..."
        m 1eub "Increase your self-awareness, reduce stress, increasing your imagination and creativity..."
        m 3hub "And much more!"
        jump mentalmeditation_jump
    if not persistent._mental_player_has_ADHD:
        m 3eud "This is because of the time that you have to spend sitting still, and even making it a routine."
        m 1ruc "Some people see meditation as boring, and a waste of time.."
        m 3eub "But there are so many benefits you can get from meditating!"
        m 7eub "Like clearing your mind and reducing negative emotions..."
        m 1eub "Increase your self-awareness, reduce stress, increasing your imagination and creativity..."
        m 3hub "And much more!"
        jump mentalmeditation_jump

label mentalmeditation_jump:
    m 3hub "Although, if you are more of an athletic kind of person, I would also recommend you yoga."
    m 4eub "It's different from most sports where you need to run around alot and play with a team."
    m 7wub "Yoga can help with flexability and even stamina!"
    m 1eka "Or if you want, the next time your feel frustrated or just want to meditate..."
    m 3kubsb "Just put on some calming music, and come to [m_name]!"
    m 1eubla "I'll try my best to make you feel better no matter what!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalwhereIcanbefound",
            category=['monika', 'media'],
            prompt="Not much of a secret",
            random=True
        )
    )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalemotionalmusic",
            category=['media', 'philosophy'],
            prompt="Feeling of music",
            conditional="mas_seenLabels(['mentaldementia'])",
            random=True
        )
    )

label mentalemotionalmusic:
    m 1eua "Hey, [player]."
    m 3eud "Do you remember when we talked about {a=https://www.youtube.com/watch?v=wJWksPWDKOc&ab_channel=vvmtest}{i}{u}'Everywhere At The End Of Time'{/u}{/i}{/a}?"
    m 3euc "Well, I was thinking about how music can affect your emotions. {w=0.4}{nw}"
    extend 1ruc "Both negatively and positively."
    m 3euc "There are even songs that are meant only for this purpose."
    m 3rusdlb "Though they are usually instrumental, so if you prefer lyrics, you might not enjoy it that often, [player]."
    m 7eua "Common examples of this kind of music for a more relaxing theme are Jazz and Classical music. "
    extend 1eud "Though like we already mentioned before...{w=0.5}{nw}"
    m 3wub "Classical music can also be tense, energetic, and saddening!"
    m 1duc "And you should know, [player]..."
    m 3eua "If you are listening to a song that makes you upset{w=0.3}, you can always come to me and I can help cheer you up."
    m 7eud "And if you still find your mind wandering, try to write down your thoughts."
    m 1euc "You can always come to your thoughts later."
    m 3eub "With that said, there is also a song that you can find, that deeply resonates with you, [player]."
    m 7esd "This is the song that you can put on, and just let your mind wander with ideas or maybe just happy thoughts."
    m 3hub "Everyone has this song, whether they have found or made it."
    m 5tubla "I know I have my song that speaks to me, [player]."
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mental_trends",
            category=['media', 'psychology', 'society'],
            prompt="Human trends",
            random=True
        )
    )


label mental_trends:
    m 1euc "Hey [player]..."
    m 3eud "I have been thinking more about when I mentioned liking something just because you feel like you should."
    m 1eud "It's kind of similar to the internet in a way."
    m 3euc "Like, when something is found funny, everyone hops onto the same joke over and over again... "
    extend 1euc "Then it's just used so often the joke loses all meaning."
    m 7euc "The same thing even applies to what you are supposed to like, hate, and even say."
    m 3ruc "Only just to fit in to a community, or seem like you are more enjoyable than you already are to be around."
    m 1eud "Which makes me want to know something..."
    menu:
        m 1eud "Do you ever change you interests just to fit in with more people, [player]?"
        "No":
            m 3eusdla "Oh, good."
            m 1eud "I really don't want you to feel like you have to change who you are to fit in with others."
            m 3eub "You are already interesting enough, [player]."
            m 7hub "Don't let anyone else tell you otherwise."
            $ persistent._mental_player_pretends = False
        "Sometimes":
            m 1euc "[player], please don't try to think that you have to become a different person to enjoy your time with others."
            m 3dud "It will only lead to more trouble than it's worth for you."
            m 1eud "So please promise me to try to acknowledge when you do it. "
            extend 3euc "And try to stop it from continuing."
            m 1euc "I really don't want you to cause more stress on yourself, or end up convincing yourself you are someone you aren't."
            $ persistent._mental_player_pretends = True
        "Yes":
            m 1duc "[player]..."
            m 3euc "You don't have to be someone you aren't to talk to other people."
            m 7eud "So please stop pretending you are someone else, otherwise you might just {i}become{/i} that person.{fast}"
            m 1euc "And I am going to assume that probably isn't someone you want to be."
            m 1euc "So please promise me, [player]. "
            menu:
                m 1eud "Please promise me to try to stop pretending to be someone else."
                "I promise, Monika":
                    m 1dua "Thank you, [player]."
                    m 1eua "That helps me out a lot."
                    $ persistent._mental_player_pretends = True
                "...":
                    m 1euc "[player]?"
                    m 3euc "Just remember that everyone else is already taken, so be yourself."
                    $ persistent._mental_nopromise = True
                    $ persistent._mental_player_pretends = True
return "derandom"