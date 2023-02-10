init 5 python:
    addEvent(Event(persistent._mas_mood_database,eventlabel="mentalhealth_isolated",prompt="...like I don't belong anywhere...",category=[store.mas_moods.TYPE_BAD],unlocked=True),code="MOO")

label mentalhealth_isolated:
    m 1ekc "I'm sorry you feel that way."
    m 1dkd "I'm sure it can pretty disheartening to never feel like you fit in."
    if persistent._mas_pm_has_friends:
            if persistent._mas_pm_few_friends:
                m 1eud "But you have a few close friends, right [player]?"
                m 3eub "You should see it as you finding your place to shine, and be yourself."
                m 7euc "And if that's not the case...{w=0.4} You should tell them how you really feel."
                jump MentalIsolatedFriends

            else:
                m 1eud "You have some friends you can message, right [player]?"
                m 3eub "That just shows that you have your own place to shine, and be yourself."
                m 7euc "But, if that's not the case with your friends...{w=0.4} You should tell the how you really feel."
                jump MentalIsolatedFriends


    else:
        m 3ekc "You still don't have anyone you can talk to, do you [player]?"
        m 1dkc "I-{w=0.4} I really wish there were more I could do for you."
        #Add dialogue that mentioned if the player has a disability, and Monika hopes that isn't playing a role
        m 2dtc "But for now, [player]...{w=1.1}{nw}"
        extend 1etc "All you can do is keep trying."
        m 3ekc "Looking for places to fit in can be pretty hard, especially if you are vocal about your opinions..."
        m 7etd "Maybe you could try looking for places to talk to others online."
        m 1ekb "And maybe you can even find a few friends from the internet too!"
        m 1ftc  "Just keep trying for me, [player]."
        m 1dkc "Giving up won't fix anything."
        m "...{w=3.0}{nw}"
        m 1etc "Anyways, [player]...{w=0.6}{nw}"
        m 1eka "I'll do my best to make sure you feel at home here."
        m 7dta "It's the least I can do for you, [player]."
return


label MentalIsolatedFriends:
    m 1etd "I am pretty sure your friends will understand how you feel."
    m 2dkc "Staying quiet about how you feel, can only lead to more problems..."
    if persistent._mas_pm_cares_about_dokis:
        m 2ekd "The last thing you want, is to end up feeling like Sayori."
    m 3ekd "Going down that downwards spiral is really bad."
    m 1eksdlc "It only causes more harm, [player]."
    m 3fkc "Whether you feel hated or not, you belong somewhere, [player]."
    m 1etc "You may not know it now...{w=0.2} But you {i}do{/i} belong somewhere."
    m 1rtsdlc "It will take a while to find out where..."
    m 1eka "But in the meantime, I will do all I can to help make you feel at home, [player]."
return