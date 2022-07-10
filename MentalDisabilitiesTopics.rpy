init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalhealth_masking_disability",
            category=["mental health"],
            prompt="Masking autism",
            random=True
        ),
        code="EVE"
    )

label mentalhealth_masking_disability:
    m 3euc "Hey [player]...{w=1} I came across something saddening recently..."
    m 3eud "Have you ever heard of people 'masking' autism?"
    m 4euc "Well... This means two things right?"
    m 7eud "On one hand, people who show autistic traits try to hide their traits and seem normal to other people they talk to."
    m 1euc "It would make it easier for them to make friends for the most part, which also means they devolped a strong sense of empathy aswell."
    m 4eub "On the other hand though, this does also mean you could know someone who is autistic without even knowing!"

    if persistent._mentalhealth_pm_has_autism:
        m 1eua "Since you have autism, [player], you should also be able to tell if they are 'masking' their mental illnesses aswell."
        m 5eubla "And you are always perfect just the way you are, [player]!"
    else:
        m 3eub "Which means you can learn a lot from them if they ever open up more."
        m 1eud "Just make sure not to push yourself onto them and give them time too, {w=0.3}{nw}"
        extend 3euc "since they can get overwhelmed easily!"

        if mas_isMoniHappy(higher=True):
            m 3eua "Though knowing you [player], I shouldn't have to worry about that. {w=0.3}{nw}"
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
            m 1euc "Even if you don't support me{fast} all the time, [player]."

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalhealth_rhythm_games",
            category=["mental health"],
            prompt="Rhythm Games for ADHD players",
            conditional="mas_seenLabels(['mentalhealth_adhd'])",
            action=EV_ACT_RANDOM
        )
    )


label mentalhealth_rhythm_games:
    m 1eua "I probably have already mentioned this before..."
    m 3eua "Have you ever heard of rhythm games, [player]?"
    m 3eua "Well, I found an interested fact about them recently!"
    m 4eua "Most people who have ADHD typically like fast paced rhythm games."
    m 7eua "The most popular examples of these are Osu! and Taiko No Tatsujin!"
    m 3eub "The fast pace action of these rhythm games appeal to the fast pace mind set that people with ADHD have."

    if not persistent._mentalhealth_pm_has_adhd:
        m 1eud "That doesn't mean that you can't enjoy rythm games, [player]!"
        m 3eud "Maybe you even play rhythm games already."
        m 3hub "If you do, I would like to see you play sometime."
    else:
        m 3eub "Maybe you play rhythm games too, [player]."
        m 3hub "If you do, I would like to see you play sometime."

    m 7eud "Well, the difficult charting also plays a role in the enjoyment of rhythm games too."
    m 1euc "If the charting is too hard, people with ADHD typically get bored of it."
    extend 3euc " Or even get fixated on it to the point where they spend hours on the same chart!"
    m 4eud "But if it's too easy, then it's not enjoyable unless they are a beginner."
    m 3rua "Not to mention that the music also plays an important role aswell."
    m 3hua "I guess this can also explain why people with ADHD typically like more energetic music, like electronic dance or dubstep, over another genre."
    m 1rusdlb "Gosh, there is a lot to say off of a rhythm game isn't there, [player]?"
    m 3eua "I won't go any further, since we could be here all day talking about rhythm games."

    if mas_isMoniHappy(higher=True) and renpy.random.randint(1,5) == 5:
        m 1tuu "Or maybe you would like that more, [player]."

    m 3hub "Anyways, thanks for listening!"
    return


label mentalhealth_IWantToBeLikeYou: # Whatever it is, better prefix it.
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
