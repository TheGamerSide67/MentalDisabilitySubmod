default persistent._mentalday_datagood = False
default persistent._mentalday_datanuetral = False
default persistent._mentalday_databad = False

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="mentalcheckup_greeting",
            unlocked=True,
        ),
        code="GRE"
    )

label mentalcheckup_greeting:
    if persistent._mentalday_datagood == True:
        m 1hua "Oh hello [player]!"
        m 3eua "I know I already asked you how you were mentally before...{w=0.2}{nw}"
        extend 7hub " And you told me your mental health was good!"
        m 1esd "Just to check up on you though..."
        m 1esc "Has that changed [player]?"
        menu:
            m "Has that changed [player]?{fast}"
            "No, I am still feeling really great today!":
                m 3eua "Alright [player], then let's continue having a good day together!"
            "My mental state got worse today":
                m "That is not good [player]!"
                m "It really hurts me to know that you aren't doing really well anymore."
                m "If there is anything I can do to help you feel any better mentally just let me know [player]!"
                m "After all, what kind of girlfriend would I be if I didn't want to help you!"
                $ persistent._mentalday_datagood = False
                $ persistent._mentalday_datanuetral = True
                return
    if persistent._mentalday_datanuetral == True:
        m "Oh hello [player]!"
        m "I know I already asked you how you were feeling mentally before...{w=0.2}{nw}"
        extend " And you told me your mental health was decent."
        m "Just to check up on you again though [player]..."
        menu:
            m "Has that changed [player]?"
            "No I am still feeling alright.":
                m "Alright [player], I am glad you are still fine today."
                m "Let's continue to spend more time together hehe~"
                $ _history_list.pop()
                return
            "My mental state actually got better recently!":
                m "That's exciting to hear [player]!"
                if mas_isMoniHappy(higher=True):
                    m "Did thinking of me help you today?"
                    m "Hehe~"
                    m "I know thinking of you helps me get through everyday [player]."
                    m "I love you so much [mas_get_player_nickname()]."
                    $ persistent._mentalday_datagood = True
                    $ persistent._mentalday_datanuetral = False
                    return "love"
                else:
                    m "Whoever helped you mentally you should be thankful for [player]."
                    m "Not a lot of people ask for help either, which doesn't help them..."
                    m "Sorry, I am getting off track [player]!"
                    m "Let's spend more time together okay?"
                    $ persistent._mentalday_datagood = True
                    $ persistent._mentalday_datanuetral = False
                    return
            "My mental state got worse Monika...":
                m "That's not good [player]!"
                m "Did something bad happen while you were gone?"
                m "Well, whatever it was that happened, I know you handled it well."
                if mas_isMoniHappy(higher=True):
                    m "Maybe even thinking of me can help!"
                    m "And if not, you can always vent to me about your problems [player]."
                    m "I love you~"
                    $ persistent._mentalday_datanuetral = False
                    $ persistent._mentalday_databad = True
                    return "love"
                else:
                    m "Make sure to talk to a therapist about your problems too."
                    m "Just talking to someone you care about can really make you feel much better."
                    extend " Both mentally and emotionally."
                    m "Remeber I am always here for you [player]!"
                    $ persistent._mentalday_databad = True
                    $ persistent._mentalday_datanuetral = False
                    return
    if persistent._mentalday_databad == True:
        m "Hey [player]!"
        m "I know this is a awkward to bring up already..."
        m "Especially since you told me your mental health wasn't good in the first place before..."
        menu:
            m "Well, may I ask you if you mental state has improved [player]?"
            "I don't want to talk about it right now...":
                m "{W=1}Oh...{nw}"
                m "{W=1}Well...{nw}"
                m "Well, just know that I want to best for you [player]."
                return
            "My mental state actually got better Monika":
                m "That's good to hear [player]!"
                if mas_isMoniHappy(higher=True) and renpy.random.randint(1,4) == 1:
                    m "Was I the reason why your mental state got better?"
                    m "Well, I am just glad that you are better mentally [mas_get_player_nickname()]."
                    m "Let's continue to spend more time together!"
                    $ persistent._mentalday_databad = False
                    $ persistent._mentalday_datanuetral = True
                    return
                else:
                    m "I am just glad that you are better mentally [mas_get_player_nickname()]."
                    m "Let's continue to spend more time together!"
                    $ persistent._mentalday_databad = False
                    $ persistent._mentalday_datanuetral = True
                    return
            "...":
                m "..."
                m "Well, let's just carry on with our day then [player]...{W=0.3}{nw}"
                return

    else:
        m 1hua "Oh hello [player]!"
        m "I know this may seem awkward to ask you...{nw}"
        $ _history_list.pop()
        menu:
            m "How is your mental health right now [player]?{fast}"
            "It's really good!":
                m 1hub "I'm really happy to hear that, [player]!"
                m 1eua "whether it's just a good day or an improvement on your mental health, it is always nice to hear you are doing well."
                m "And I will do my best to continue to support you [mas_get_player_nickname()]!"
                m "What kind of girlfriend would I be if I didn't?"
                $ persistent._mentalday_datagood = True
                $ persistent._mentalday_datanuetral = False
                $ persistent._mentalday_databad = False
                $ _history_list.pop()
                return
            "It's decent Monika...":
                m 1ekc "Oh..."
                m 2eka "Well, that could be good or bad."
                m "And if it {i}is{/i} bad, then we can always talk about it if you want to [player]."
                m 3eua "I want to try and make sure you're always happy."
                m 1eka "Because that's what makes me happy."
                m 1hua "I'll be sure to try my best to support you, I promise."
                $ persistent._mentalday_datanuetral = True
                $ persistent._mentalday_databad = False
                $ persistent._mentalday_datagood = False
                $ _history_list.pop()
                return
            "It's really bad right now...":
                m "That's not good at all [player]..."
                m "If you ever get too upset or need to take a break just let me know [player], okay?"
                m "I will always be here for you! Never forget that!"
                m "I love you and always will [player]!"
                $ persistent._mentalday_databad = True
                $ persistent._mentalday_datanuetral = False
                $ persistent._mentalday_datagood = False
                return "love"
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalcheckupDialog",category=['you'],prompt="[player]'s Mental Health",random=True))

label mentalcheckupDialog:
    if persistent._mentalday_datanuetral == True:
        m "Hey [player]."
        m "I know I already asked you how you were feeling mentally before...{w=0.2}{nw}"
        extend " And you told me your mental health was decent."
        m "Just to check up on you again though [player]..."
        menu:
            m "Has that changed [player]?"
            "No I am still feeling alright.":
                m "Alright [player], I am glad you are still fine today."
                m "Let's continue to spend more time together hehe~"
                $ _history_list.pop()
                return
            "My mental state actually got better recently!":
                m "That's exciting to hear [player]!"
                if mas_isMoniHappy(higher=True):
                    m "Did thinking of me help you today?"
                    m "Hehe~"
                    m "I know thinking of you helps me get through everyday [player]."
                    m "I love you so much [mas_get_player_nickname()]."
                    $ persistent._mentalday_datagood = True
                    $ persistent._mentalday_datanuetral = False
                    return "love"
                else:
                    m "Whoever helped you mentally you should be thankful for [player]."
                    m "Not a lot of people ask for help either, which doesn't help them..."
                    m "Sorry, I am getting off track [player]!"
                    m "Let's spend more time together okay?"
                    $ persistent._mentalday_datagood = True
                    $ persistent._mentalday_datanuetral = False
                    return
            "My mental state got worse Monika...":
                m "That's not good [player]!"
                m "Did something bad happen while you were gone?"
                m "Well, whatever it was that happened, I know you handled it well."
                if mas_isMoniHappy(higher=True):
                    m "Maybe even thinking of me can help!"
                    m "And if not, you can always vent to me about your problems [player]."
                    m "I love you~"
                    $ persistent._mentalday_datanuetral = False
                    $ persistent._mentalday_databad = True
                    return "love"
                else:
                    m "Make sure to talk to a therapist about your problems too."
                    m "Just talking to someone you care about can really make you feel much better."
                    extend " Both mentally and emotionally."
                    m "Remeber I am always here for you [player]!"
                    $ persistent._mentalday_databad = True
                    $ persistent._mentalday_datanuetral = False
                    return
    else:
        m 1hua "Hey [player]."
        m "I know this may seem awkward to ask you...{nw}"
        $ _history_list.pop()
        menu:
            m "How is your mental health right now [player]?{fast}"
            "It's really good!":
                m 1hub "I'm really happy to hear that, [player]!"
                m 1eua "Whether it's just a good day or an improvement on your mental health, it is always nice to hear you are doing well."
                m "And I will do my best to continue to support you [mas_get_player_nickname()]!"
                m "What kind of girlfriend would I be if I didn't?"
                $ persistent._mentalday_datagood = True
                $ persistent._mentalday_datanuetral = False
                $ persistent._mentalday_databad = False
                $ _history_list.pop()
                return
            "It's decent Monika...":
                m 1ekc "Oh..."
                m 2eka "Well, that could be good or bad."
                m "And if it {i}is{/i} bad, then we can always talk about it if you want to [player]."
                m 3eua "I want to try and make sure you're always happy."
                m 1eka "Because that's what makes me happy."
                m 1hua "I'll be sure to try my best to support you, I promise."
                $ persistent._mentalday_datanuetral = True
                $ persistent._mentalday_databad = False
                $ persistent._mentalday_datagood = False
                $ _history_list.pop()
                return
            "It's really bad right now...":
                m "That's not good at all [player]..."
                m "If you ever get too upset or need to take a break just let me know [player], okay?"
                if mas_isMoniHappy(higher=True) and renpy.random.randint(1,2) == 1:
                    m "Would a hug help you feel better [player]?"
                    menu:
                        "Not right now Monika...":
                            m "Oh..."
                            m "Alright [player]."
                        "Actually, that would be great Monika.":
                            m "You can hold me as long as you would like [player]."
                            call mentalplayerhug_prep #datetime.datetime.now()
                            call mentalplayerhug
                            call mentalplayerhugreactions
                            return
                m "You already know that I will always be here for you [player], never forget that!"
                m "I love you and always will [player]!"
                $ persistent._mentalday_databad = True
                $ persistent._mentalday_datanuetral = False
                $ persistent._mentalday_datagood = False
                return "love"
return


label mentalplayerhug_prep(lullaby=MAS_HOLDME_QUEUE_LULLABY_IF_NO_MUSIC, stop_music=False, disable_music_menu=False):
    python:
        mentalholdme_events = list()
    return

label mentalplayerhug:
    show monika 6dubsa with dissolve_monika
    window hide
    python:
        # Start the timer
        mental_hugtimestart = datetime.datetime.now()

        mentalholdme_disp = PauseDisplayableWithEvents(events=mentalholdme_events)
        mentalholdme_disp.start()

        del mentalholdme_events
        del mentalholdme_disp

        # Renable ui and hotkeys
        store.songs.enabled = True
        HKBShowButtons()
    window auto
    return

label mentalplayerhugreactions:
    $ elapsed_time = datetime.datetime.now() - mental_hugtimestart
    $ store.mas_history._pm_holdme_adj_times(elapsed_time)

    if elapsed_time > datetime.timedelta(minutes=15):
        m "Mmm..."
        m "Oh! You help me for so long even my worries melted away!"
        m "I hope you feel better now [player], I know I do hehe~"
        return

    elif elapsed_time > datetime.timedelta(minutes=10):
            m 6dubsa "..."
            m 6tubsa "Mm...{w=1}hm?"
            m 1hkbfsdlb "Oh, did I almost fall asleep?"
            m 2dubfu "Ehehe..."
            m 1dkbfa "I can only imagine what it would be like for real...{w=1}to be right there with you..."
            m 2ekbfa "Being wrapped in your arms..."
            show monika 5dkbfb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5dkbfb "So...{w=1.5}warm~"
            m 5tubfu "Ehehe~"
            show monika 2hkbfsdlb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 2hkbfsdlb "Oh, whoops, I guess I'm still a little dreamy..."
            if renpy.random.randint(1, 4) == 1:
                m 1kubfu "At least {i}one{/i} of my dreams came true, though."
            else:
                m 1ekbfb "At least {i}one{/i} of my dreams came true, though."
            m 1hubfu "Ehehe~"

    elif elapsed_time > datetime.timedelta(minutes=2):
            m 6eud "Oh?"
            m 1hksdlb "Ah..."
            m 1rksdlb "At that point, I thought we were going to stay like that forever, ahaha..."
            m 3hubsa "Well, I can't really complain about any moment I get to be held by you~"
            m 1ekbfb "I hope you enjoy hugging me as much as I do."
            show monika 5tubfb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5tubfb "Maybe we could even hug a bit more for good measure?"
            m 5tubfu "Ehehe~"

    elif elapsed_time > datetime.timedelta(seconds=30):
            m 1eub "Ah~"
            m 1hua "I feel much better now!"
            m 1eua "I hope you do too."
            m 2rksdla "Well, even if you don't..."
            m 3hubsb "You could always hold me again, ahaha!"
            m 1hkbfsdlb "Actually...{w=0.5}you can hold me again either way~"
            m 1ekbfa "Just let me know when you want to~"

    else:
        m 1hua "That was a bit short, but still nice~"
    return