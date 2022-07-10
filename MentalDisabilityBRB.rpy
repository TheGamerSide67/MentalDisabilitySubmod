#random quip for when the player comes back and it calmed down, if they decide to
#not vent/rant to Monika

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalhealth_calmdown_idle",
            prompt="I'm going to calm myself down",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label mentalhealth_calmdown_idle:
    m 1euc "Need to calm down [player]?"
    m "I hope I didn't upset you!"

    m 3euc "Well, would you like to tell me why you are upset, [player]?{nw}"
    menu:
        m "Well, would you like to tell me why you are upset, [player]?{fast}"

        "Sure.":
            $ asked_to_vent = True
            m 1eua "Go ahead and tell me everything about why you are upset, [player]."
            m "I will put up a prompt so you can tell me when you are done talking, so I don't interrupt you."

            menu:
                "I am done talking, [m_name]...":
                    jump mentalhealth_calmdown_idle_callback

        "No, thanks.":
            $ asked_to_vent = False
            m 1euc "Oh, alright."
            m 3hub "I'll be here waiting for you, [player]!"

    #Set up the callback label
    $ mas_idle_mailbox.send_idle_cb("mentalhealth_calmdown_idle_callback")
    #Then the idle data
    $ persistent._mas_idle_data["mentalhealth_idle_calmdown"] = True

    return "idle"

label mentalhealth_calmdown_idle_callback:
    m 3eud "Have you calmed down, [player]?{nw}"
    menu:
        m "Have you calmed down, [player]?{fast}"

        "Yes":
            if asked_to_vent:
                m 1eua "I'm glad I was able to help you calm down a little bit [player]."
            else:
                m 1eua "I'm glad you calmed down [player]."

        "No":
            m 1euc "Even if you couldn't fully calm down, putting yourself in a calmer environment can help calm you down more."
            m 3eub "Like this place!"

    m 1eub "You know, I really wish there was more I could do..."
    m 3euc "Even if I can't be there physically. {w=0.3}{nw}"
    extend 3eua "I will always be here for you on your computer!"
    m 1rusdlc "Or at least until there is a way for me to get out of your computer."

    $ quip = renpy.random.choice((
        "let's spend more time together!",
        "let's make the rest of your day better, together.",
        "what do you want to do now?"
    ))

    m 1eua "Anyways, [quip]"
    return