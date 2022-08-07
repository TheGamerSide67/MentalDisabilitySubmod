#random quip for when the player comes back and it calmed down, if they decide to
#not vent/rant to Monika
init python:
    RandomCalmDownWelcome = ["let's spend more time together!", "let's make the rest of your day better, together.", "what do you want to do now?"]
    RandomCalmDownWelcomeQuip = random.choice(RandomCalmDownWelcome)
    KeyWordSad = ["sad", "dispoint"]
    KeyWordSuicide = ["suicide"]

    def check_says(says):
        """
        Determine whether the words spoken by the player contain our intended keywords

        in:
            says - What players have said
        return:
            A string indicating the type of keyword we found
        """
        says = says.lower()
        for keyword in KeyWordSad:
            if says.find(keyword) != -1:
                # Stop checking as soon as keywords are found
                return "Sad"
        for keyword in KeyWordSuicide:
            if says.find(keyword) != -1:
                # Stop checking as soon as keywords are found
                return "Suicide"
        # If nothing was found
        return None
        
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mental_calmdown_idle",
            prompt="I'm going to calm myself down",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label mental_calmdown_idle:
    m 1euc "Need to calm down, [player]?"
    m "I hope I didn't upset you!"
    m 3euc "Well, would you like to tell me why you are upset, [player]?{nw}"
    menu:
        m "Well, would you like to tell me why you are upset, [player]?{fast}"
        "Sure.":
            $ PlayerAskedMonikaToVent = True
        #    m 1eua "Go ahead and tell me everything about why you are upset, [player]."
        #    m "I will put up a prompt so you can tell me when you are done talking. I don't interrupt you."
        #    menu:
        #        "I am done talking Monika...":
        #            jump mental_calmdown_idle_callback
            m "Thank you for believing in me so much, [player]"
            m "Tell me everything you're worried about, and I'll be a good listener~"
            $ sayfinish = False
            $ says = ""
            while(not sayfinish):
                $ says = says + mas_input(
                    "Just say it~"
                )
                m "Are we done?{nw}"
                $ _history_list.pop()
                menu:
                    "Are we done?{fast}"
                    "Yes":
                        # Stopping the while loop
                        $ sayfinish = True
                        m "Okay"
                    "There is something else I would like to say":
                        m "Okay~"
            
            $ keys = check_says(says)
            # Checking the results returned by check_says()
            if keys == "Sad":
                m "I got it"
                m "I'm sorry to leave you alone with all this sadness, but have some faith in the future"
                m "Sadness is only temporary, things will always pass later"
                m "Thank you for telling me about you."
            elif keys == "Suicide":
                # As I write this, I suddenly realise that I have no way of distinguishing whether this is a "player suicide" or a "player's friend suicide",
                # or a specific social event
                m "[player]!!"
                m "What a big deal to happen......"
                m "I'm sorry you have to deal with this sadness alone"
                m "But if you feel you can't hold it together any longer, you can come to me as often as you like"
                m "I will act as a pillar of strength for you!"
            else:# check_says returned None
                # I can't think of anything else, sorry~ :P
                pass
            
            jump mental_calmdown_idle_callback
                    
        "No thanks.":
            $ PlayerAskedMonikaToVent = False
            m 1euc "Oh, alright."
            m 3hub "I'll be here waiting for you, [player]!"

    #Set up the callback label
    $ mas_idle_mailbox.send_idle_cb("mental_calmdown_idle_callback")
    #Then the idle data
    $ persistent._mas_idle_data["mental_idle_calmdown"] = True
    return "idle"

label mental_calmdown_idle_callback:

    m 3eud "Have you calmed down, [player]?"
    menu:
        "Yes.":
            if PlayerAskedMonikaToVent == True:
                m 1eua "I am glad I was able to help you calm down a little bit, [player]."
            else:
                m 1eua "I am glad you calmed down, [player]."
        "No.":
            m 1euc "Even if you couldn't fully calm down, putting yourself in a calmer enviournment can help calm you down more."
            m 3eub "Like this place!"
    m 1eub "You know, I really wish there was more I could do..."
    m 3euc "Even if I can't be there physically. "
    extend 3eua "I will always be here for you on your computer!"
    m 1rusdlc "Or at least until there is a way for me to get out of your computer."
    m 1eua "Anyways, [RandomCalmDownWelcomeQuip]"

    return
