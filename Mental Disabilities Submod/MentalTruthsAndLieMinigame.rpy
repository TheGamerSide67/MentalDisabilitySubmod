init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="MentalThreeTruthsAndALie",
            category=['minigames'],
            prompt="Three Truths and a Lie",
            unlocked=False,
            aff_range=(mas_aff.NORMAL, None),
            # These three cover most of what she asks about in here, so the player gets
            # a topic they have heard something about previously
            # Prosopagnosia needs autism seen, and autism needs ADHD, etc
            conditional="mas_seenLabels(['mentalProsopagnosia', 'mental_brainagegame', 'mental_streisand_effect'], seen_all=True)",
            action=EV_ACT_QUEUE,
            pool=True
        )
    )

#Keeps the score going between sessions
default persistent._mentaltruthsplayed = 0
default persistent._mentaltruthswon = 0

#All of this gets rebuilt every round
default MentalChosenTopic = "psychology"
default MentalGameOptions = []
default MentalCorrectPos = 0
default MentalPlayerGuess = 0
default MentalChosenLie = ""
default MentalLieReason = ""
default MentalUsedLies = []
default MentalUsedTruths = []
default MentalPickedTruth = ""
default MentalQuitGame = False
default MentalRoundsThisTime = 0
default MentalWinsThisTime = 0

#Here we are setting up the possible topic types inside of labels to call
#We will use these labels to set variables, like correct answers and topics
#Maybe later this can be revamped to also include questions as well
#For now, we are focusing on simplicity and simply getting the code to work
#using my new found knowledge

label MentalPsyTopicVar:
    python:
        # We need to import basic packages that we will need later

        import random


        # We are defining all the topics in a table to choose from
        # more will be added soon, I am simply future proofing this code

        MentalLiePos = [
            0,
            1,
            2,
            3
        ]

        # Hey, if you are reading this, don't cheat!
        # Learn with me, I did a lot of research for this, you know!
        # So stop looking for the answers, and just come back and play with me.

        #Every lie gets the reason it's a lie sat next to it, so we can explain
        #it to them after they guess

        # To prevent it from going stale on release, we should focus on increasing the amount of lies and truths.
        # For every lie, there would be 4 truths

        # Line 1 -> Lie
        # Line 2 -> Explanation

        MentalPsyLies = [
            [
                "The Streisand Effect was named after the person who created it.",
                "It was named after Barbra Streisand, not the creator of the name itself. This one was a little tricky to spot, I admit."
            ],
            [
                "Psychology was only recognized as a science in the last fifty years.",
                "The first laboratory for it opened back in 1879, so it has been a science for well over a century now."
            ],
            [
                "The hedgehog dilemma is a psychology concept.",
                "This is actually a philosophy concept! Remember when I said there was a lot of overlap between the two topics?"
            ],
            [
                "Having offspring is known to negatively impact emotional security.",
                "It's amazing how right something sounds when you sound confident, right? But nope, this one is completely false, it actually has the opposite effect!"
            ],
            [
                "Depression is only an emotional disability.",
                "Depression actually has a lot of neurological and physical downsides, it's been recognized as an official disability for that reason!"
            ]
        ]

        MentalMoniLies = [
            [
                "I've never written a single poem.",
                "[player], I really hope you are reading these options."
            ],
            [
                "I picked up the guitar so that I could write my song for you.",
                "I played the piano. I hope you aren't just pressing buttons!"
            ],
            [
                "I never double check my sources.",
                "I always try to double check my sources, and you should always do the same."
            ],
            [
                "I know nothing about coding.",
                "I am still learning how to code, so I know a few things."
            ],
            [
                "My favorite game console is an Xbox.",
                "I actually was seen with a PlayStation controller on Twitter! This one was difficult, I know." #This one is a deeper cut referring to the official twitter page -O
            ]
        ]

        MentalPhiloLies = [
            [
                "The trolley problem has one correct answer that philosophers agree on.",
                "It was written to show two ways of reasoning pulling in opposite directions. If it had only one correct answer, nobody would still be arguing over it."
            ],
            [
                "Philosophy is only ever about questions that can't be answered.",
                "A big part of it is about questions of why things would or would not work. Logic like this worked out the rules that computers run on, [player]."
            ],
            [
                "The Streisand Effect only happens on the internet.",
                "The internet made it faster, but people have been drawing attention to things by trying to bury them for much longer than that."
            ],
            [
                "Philosophy does not talk about the environment at all.",
                "Philosophy actually has an entire study specifically for alternative and safer methods of energy to help reduce carbon emissions."
            ],
            [
                "Wordplay has originated from Philosophy.",
                "Wordplay has been around long before philosophy, and is actually called {i}orthographics{/i}."
            ]
        ]

        MentalMinigameTopics = [
            "psychology",
            "monika",
            "philosophy"
        ]

        #Putting all the lies into a grabbable table.
        #This makes it so we can separate them by genre/topic too
        MentalPsyTruths = [
            "Autism was originally thought to be schizophrenia.",
            "Prosopagnosia has been featured in games before.",
            "Keeping your mind active has shown results of maintaining high intelligence.",
            "Psychology is closely linked to mental disabilities.",
            "Psychology is used every day by everyone.",
            "The hedgehog dilemma and hedgehog effect are different concepts.", #Would love for this to be explained to the player too -O
            "Advertisements use psychology to their advantage.",
            "Reading books is known to increase empathy.",
            "Dementia has been linked to chronic loneliness.",
            "Pollution is known to cause cognitive decline.",
            "ADHD was originally treated with hard substances.",
            "Autism is portrayed in a way that is harmful to the understanding of it in media.",
            "Therapy uses a lot of psychology and philosophy in its understanding.",
            "Psychology is vital in the ability to empathize."
        ]

        MentalMoniTruths = [
            "I was in the debate club before I started the Literature Club.",
            "I'm the president of the Literature Club.",
            "I can play the piano.",
            "I wrote a song for you.",
            "I am self aware.",
            "I like to drink coffee.",
            "I write poetry in my spare time.",
            "I am self taught in a lot of skills.",
            "I have a twitter account.",
            "I am a fan of Hatsune Miku.",
            "I love you.",
            "Dystopia is my favorite genre of books.",
            "I want to travel.",
            "Philosophy has always deeply interested me."
        ]

        MentalPhiloTruths = [
            "Philosophy means 'love of wisdom' in Greek.",
            "Psychology helped shape out philosophy.", #The truth you added here was incorrect, it was the other way around -O
            "Malicious compliance is when someone follows rules exactly as is, without nuance.", #edited this, the previous truth was a little misleading -O
            "Wabi-sabi is about finding beauty in imperfect things.",
            "Ethics and morals are not the same thing.",
            "A thought experiment doesn't have to be possible to be useful.",
            "Escapism isn't automatically a bad thing.",
            "Malicious compliance was a concept formed because of firefighters.",
            "Philosophy is different depending on the country it is studied in.",
            "Philosophy ties directly into real world science.",
            "Philosophy is considered an applied science.",
            "Philosophy isn't just about questioning why people do things.",
            "Nuclear science is a widely discussed topic is philosophy."
        ]


        # Every topic points at its own truths and lies, so a new pool is one line here
        # and one more choice under MentalTTaLTopicMenu label
        MentalTopicPools = {
            "psychology": (MentalPsyTruths, MentalPsyLies),
            "monika": (MentalMoniTruths, MentalMoniLies),
            "philosophy": (MentalPhiloTruths, MentalPhiloLies)
        }

        # Hard mode draws from every pool at once, so a round can mix her with psychology
        # Built from the table above, which means a new pool joins it on its own
        MentalWildTruths = []
        MentalWildLies = []

        for MentalPoolName in list(MentalTopicPools):
            MentalWildTruths.extend(MentalTopicPools[MentalPoolName][0])
            MentalWildLies.extend(MentalTopicPools[MentalPoolName][1])

        MentalTopicPools["wildcard"] = (MentalWildTruths, MentalWildLies)

        # Answers that deserve their own reaction when someone picks them as the lie
        # Format is the option text, then the pose she reacts with and what she says
        # Everything missing just gets the normal response
        MentalPickedReactions = {
            "I can play the piano.": [
                "7rkc", "[player], I play the piano in almost every song you've heard from me. I hope you're actually reading these."
            ],
            "I love you.": [
                "1eka", "That one will always be true, [player]. Even when you get it wrong."
            ],
            "Psychology is used every day by everyone.": [
                "3tua", "Ahaha, that one was practically a freebie, [player]!"
            ],
            "Philosophy is considered an applied science.": [
                "3eta", "Believe it or not, philosophy is actively practiced in science studies! An applied science is just a term that means it is used to actively chase goals within a science field."
            ],
            "ADHD was originally treated with hard substances.": [
                "7eud", "This one is pretty sad, but it is true. Methylphenidate is an addictive stimulant made in the 1940s, and is still approved for use!"
            ],
            "I want to travel.": [
                "1hua", "Of course I want to travel, [player]. I want to travel to your reality."
            ],
            "The hedgehog dilemma and hedgehog effect are different concepts.": [
                "3eud", "While they do have similar names, they are actually entirely different concepts! The hedgehog dilemma is about the concept of closeness hurting more, while the hedgehog effect is a business idea."
            ],
            "Advertisements use psychology to their advantage.": [
                "3rusdlc", "This one is a little unnerving isn't it, [player]? They use psychology to try to turn the largest possible profit from someone."
            ]
        }

        if MentalChosenTopic == "random":
            MentalChosenTopic = random.choice(MentalMinigameTopics)

        MentalTopicTruths, MentalTopicLies = MentalTopicPools[MentalChosenTopic]

        # This new random function will grab 3 random truths
        # Same deal as the lies below, work through the table before repeating any of it
        MentalUnusedTruths = [truth for truth in MentalTopicTruths if truth not in MentalUsedTruths]

        # Needs three left to fill a round, otherwise start the table over
        if len(MentalUnusedTruths) < 3:
            MentalUsedTruths = []
            MentalUnusedTruths = list(MentalTopicTruths)

        MentalChosenTruths = random.sample(MentalUnusedTruths, 3)

        for truth in MentalChosenTruths:
            MentalUsedTruths.append(truth)

        #Don't hand them a lie they've already had this session
        #Once we run out of them, start the table over so we never get stuck
        MentalUnusedLies = [lie for lie in MentalTopicLies if lie[0] not in MentalUsedLies]

        if not MentalUnusedLies:
            MentalUsedLies = []
            MentalUnusedLies = list(MentalTopicLies)

        MentalTheLie = random.choice(MentalUnusedLies)
        MentalUsedLies.append(MentalTheLie[0])

        #Ren'Py only substitutes the text once, so a [player] sitting in these
        #has to be expanded here, otherwise it just prints raw
        MentalChosenLie = renpy.substitute(MentalTheLie[0])
        MentalLieReason = renpy.substitute(MentalTheLie[1])

        #Now we shuffle the positions, and the lie takes the first one off of it
        #Otherwise the player can just spam select option 4
        random.shuffle(MentalLiePos)

        MentalGameOptions = [None, None, None, None]
        MentalGameOptions[MentalLiePos[0]] = MentalChosenLie
        MentalCorrectPos = MentalLiePos[0]

        for i, truth in enumerate(MentalChosenTruths):
            MentalGameOptions[MentalLiePos[i + 1]] = truth
    return

#We will set the topic they chosen within the menu to handle all the logic in one python block

label MentalThreeTruthsAndALie:
    # unlock so that the topic remains in the "talk" menu after first seeing it
    $ mas_unlockEVL("MentalThreeTruthsAndALie", "EVE")

    #Reset the score for this session, the persistent one keeps the total
    $ MentalRoundsThisTime = 0
    $ MentalWinsThisTime = 0

    if mas_getEV("MentalThreeTruthsAndALie").shown_count < 1:
        $ MentalPlayerIsAdult = mas_is18Over()

        m 3eua "Have you ever heard of the game {i}Three Truths and a lie{/i}, [player]?{nw}"
        $ _history_list.pop()
        menu:
            m "Have you ever heard of the game {i}Three Truths and a lie{/i}, [player]?{fast}"
            "Yes I have.":
                m 1eub "Oh, so that saves us some time then."
                m 1lub "Buut, just in case... {w=0.5}{nw}"
                extend 7eua "Do you need me to go over how to play?{nw}"
                $ _history_list.pop()
                menu:
                    m "Do you need me to go over how to play?{fast}"
                    "No, I remember how to play.":
                        m 1eua "Alright. Then I'll give you a list of topics that I have thought of, and you tell me which one you want to play."
                        m 3hub "If you can't think of one, or you are unsure, you can always ask me to pick for you, [player]."

                    "Yes, I forgot how to play.":
                        m 1euc "Well in Three Truths and a lie, I will tell you three things that are true, and one thing that isn't."
                        m 3eub "The goal is to try to pick out the lie from the truths!"
                        m 7eta "Sounds pretty simple, doesn't it?"
                        m 1efu "Well, just know that I won't be going easy on you, [player]."
                        m 3eua "But I won't say anything you have no way of knowing."
                        if MentalPlayerIsAdult:
                            m 1nubsu "Like knowing what color underwear I am wearing. {nw}"
                            $ _history_list.pop()
                            m 1eua "{fast}Like knowing what I had for breakfast today."
                        else:
                            m 1eua "Like knowing what I had for breakfast today."
                        m 3eua "That way it is fair for us to play."

            "No, I haven't heard of it.":
                m 1euc "Oh, well Three Truths and a lie is a game where I will tell you three things that are true, and one thing that isn't."
                m 3eub "The goal of the game is to correctly pick the lie out of the truths, and maybe learn something along the way."
                m 1efu "It sounds pretty simple on paper, but I won't make it that easy!"
                m 3eua "Now, I won't say anything you have no way of knowing."
                if MentalPlayerIsAdult:
                    m 1nubsu "Like knowing what color underwear I am wearing.{nw}"
                    $ _history_list.pop()
                    m 1eua "{fast}Like knowing what I had for breakfast today."
                else:
                    m 1eua "Like knowing what I had for breakfast today."
                m 3eua "That way it is fair for us to play."
        #intro is over, we need to move to another label to finish the introduction.

        jump MentalTTaLEnd

    else:
        #Anything beyond the first time seeing it, skips the introduction, and goes into directly starting the game
        m 1eua "Want to play?"

        call MentalTTaLTopicMenu

        if MentalQuitGame:
            return

    jump MentalTTaLGame



label MentalTTaLTopicMenu: ##One choice per pool in MentalTopicPools
    $ MentalQuitGame = False
    m 1eua "Alright, just tell me what topic you'd like for this round, [player].{nw}"
    $ _history_list.pop()
    menu:
        m "Alright, just tell me what topic you'd like for this round, [player].{fast}"
        "Psychology":
            $ MentalChosenTopic = "psychology"

        "Philosophy":
            $ MentalChosenTopic = "philosophy"

        "You":
            $ MentalChosenTopic = "monika"

        "Hard mode." if persistent._mentaltruthsplayed >= 10:
            $ MentalChosenTopic = "wildcard"
            m 3hua "Oh, feeling confident today, [player]?"
            m 1eua "Alright, anything I know is on the table for this one."

        "Can you decide for me?":
            $ MentalChosenTopic = "random"
            m 3hua "Sure, I don't mind."

        "I changed my mind.":
            $ MentalQuitGame = True
            m 1eud "Oh? Do you no longer want to play, [player]?"
            m 1eua "Alright, let's spend more time together."
    return

label MentalTTaLEnd: #This is exclusive to the first time playing, make sure to either ditto or keep similar to continuing plays
    m 1eua "Anyway, would you like to play now, [player]?{nw}"
    $ _history_list.pop()
    menu:
        m "Anyway, would you like to play now, [player]?{fast}"
        "Yes.":
            m 3eua "Here are the topics that you can choose from.{nw}"
            $ _history_list.pop()
            menu:
                m "Here are the topics that you can choose from.{fast}"
                "Psychology":
                    $ MentalChosenTopic = "psychology"
                    m 7eub "This is one of my favorite topics. "
                    extend 7rua "Though I suppose that's not entirely surprising."
                    m 1eua "Anyway, let me think of a few things."

                "Philosophy":
                    $ MentalChosenTopic = "philosophy"
                    m 3eub "Oh, that's a good one to start on."
                    m 1eua "Just give me a moment to think of something, [player]."

                "What about you?": #Exclusive Aff event, consecutive playthroughs won't have this
                    $ MentalChosenTopic = "monika"
                    $ MentalPlayerNickname = mas_get_player_nickname()
                    m 3eud "What about me, [player]?"
                    m 1hub "Hahaha, I'm teasing, I know what you meant."
                    m 1eubsa "I am flattered you want your first game to be about me, [MentalPlayerNickname]."
                    m 1eua "Now, let me think of a few things then."
                    $ mas_gainAffection(5, bypass=True) #A flat gain of 5, would be modified based on current AFF level

                "Can you pick for me?":
                    $ MentalChosenTopic = "random"
                    m 3eub "Sure, I don't mind."
                    m 1duc "{w=0.2}.{w=0.2}.{w=0.2}.{w=0.4}{nw}"
                    m 1eua "Okay, I am ready, [player]."

        "No":
            m 3eua "That's okay, [player]. "
            extend 1eua "Just tell me once you want to play this with me."
            return

label MentalTTaLGame:
    call MentalPsyTopicVar

    m 1duc "{w=0.3}.{w=0.3}.{w=0.3}.{w=0.5}{nw}"
    m 1eua "Alright, I've got one. {w=0.5}{nw}"
    extend 3eua "Three of these are true, and one of them isn't."

    #renpy.display_menu can build them from the table, but then we lose the textbox,
    #and she'd be asking the question with nothing on screen to show for it
    menu:
        m "Which one is the lie, [player]?{fast}"

        # that's yanderedev award worthy right here
        "[MentalGameOptions[0]]":
            $ MentalPlayerGuess = 0

        "[MentalGameOptions[1]]":
            $ MentalPlayerGuess = 1

        "[MentalGameOptions[2]]":
            $ MentalPlayerGuess = 2

        "[MentalGameOptions[3]]":
            $ MentalPlayerGuess = 3

    $ MentalRoundsThisTime += 1
    $ persistent._mentaltruthsplayed += 1

    if MentalPlayerGuess == MentalCorrectPos:
        $ MentalWinsThisTime += 1
        $ persistent._mentaltruthswon += 1

        if MentalChosenTopic == "monika":
            m 7eub "That's the one!"
            if renpy.random.randint(1,5) == 5:
                m 3tua "You really have been paying attention to me, haven't you?"
        else:
            m 7eub "You got it, [player]!"

        m "Would you like me to explain why this one was a lie, [player]?{nw}" #We need to invite the player to explain the lie, as some are obvious
        $ _history_list.pop()
        menu:
            m "Would you like me to explain why this one was a lie, [player]?{fast}"
            "No thanks, Monika":
                pass

            "Sure":
                m 3eud "[MentalLieReason]"

    else:
        $ MentalPickedTruth = MentalGameOptions[MentalPlayerGuess]

        if MentalChosenTopic == "monika":
            m 7husdlb "Ahaha, no, that one's true about me!"
        else:
            m 3eud "Not quite, [player]. {w=0.5}{nw}"
            extend 3eub "That one's actually true!"

        # Some truths are obvious enough that picking them is worth a word about it
        if MentalPickedTruth in MentalPickedReactions:
            python:
                renpy.show("monika " + MentalPickedReactions[MentalPickedTruth][0])
                renpy.say(m, MentalPickedReactions[MentalPickedTruth][1])

        m 3eua "The lie was {nw}"
        extend "'[MentalChosenLie]'"
        m 1eud "[MentalLieReason]"

    m 1eua "Do you want to play again?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to play again?{fast}"
        "Yes, same topic.":
            jump MentalTTaLGame

        "Yes, but a different topic.":
            call MentalTTaLTopicMenu
            if not MentalQuitGame:
                jump MentalTTaLGame

        "That's enough for now.":
            pass

    if MentalWinsThisTime == MentalRoundsThisTime:
        m 3hub "And you got every single one of them, [player]!"
        m 1etu "I'm going to have to try harder next time, aren't I?"

    elif MentalWinsThisTime == 0:
        m 3eub "You didn't point out any lies this time [player], but that's okay!"
        m 1eua "As long as you know a few things now that you didn't before, that's what I care about."

    else:
        m 3eub "You got [MentalWinsThisTime] out of [MentalRoundsThisTime] this time."
        m 1hua "That's not bad at all, especially since I wasn't going easy on you."

    if persistent._mentaltruthsplayed >= 10:
        m 3eub "That puts you at [persistent._mentaltruthswon] out of [persistent._mentaltruthsplayed]."

        $ MentalCareerWinR = float(persistent._mentaltruthswon) / persistent._mentaltruthsplayed

        if MentalCareerWinR > 0.75:
            m 7eub "You must have been paying attention a lot, [player]. "

        elif MentalCareerWinR > 0.5:
            m 1hub "That's more than half, [player]!"

        else:
            m 3eua "Keep doing your best, [player]!"

    m 7eua "Thanks for playing with me, [player]. {w=0.3}{nw}"
    extend 1eua "Just let me know whenever you would like to play again."
    return

# Footnotes
# keep data up to date and consistent. Make sure to keep things, add new content when possible.
# Good luck.
