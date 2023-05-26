default persistent._mentalhealth_last_checkup = None
define persistent._nextmentalcheckup = datetime.date.today()
default persistent._lastmentalcheckup = None
define persistent._mentalcheckupdeadline = datetime.timedelta(days=30) + datetime.date.today()


label mentalcheckupscript:
    $ persistent._lastmentalcheckup = datetime.date.today()
    $ persistent._nextmentalcheckup = datetime.timedelta(days=7) + persistent._lastmentalcheckup
    $ persistent._mentalcheckupdeadline = persistent._lastmentalcheckup + datetime.timedelta(days=30)
    $ mas_getEV("mentalhealthcheckupdialoguefinal").start_date = persistent._nextmentalcheckup
    $ mas_getEV("mentalhealthcheckupdialoguefinal").end_date = persistent._mentalcheckupdeadline
    $ mas_getEV("mentalhealthcheckupdialoguefinal").action = EV_ACT_QUEUE

return

init python in mentalhealth:
    CHECKUP_GOOD = "good"
    CHECKUP_NEUTRAL = "neutral"
    CHECKUP_BAD = "bad"


init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="mentalcheckup_greeting",
            category=["you", "mental health"],
            prompt="[player]'s Mental Health",
        ),
        code="GRE"
    )

label mentalcheckup_greeting:
    if persistent._mentalhealth_last_checkup == store.mentalhealth.CHECKUP_GOOD:
        m 1hua "Oh hello, [player]!"
        m 3eua "I know I already asked you how you were mentally before... {w=0.2}{nw}"
        extend 7hub "And you told me your mental health was good!"
        m 1esd "Just to check up on you though..."
        call mentalcheckupscript
        m 1esc "Has that changed, [player]?"
        menu:
            m "Has that changed, [player]?{fast}"
            "No, I am still feeling really great today!":
                m 3eua "Alright [player], then let's continue having a good day together!"
                return
            "My mental state got worse today.":
                m 1ekc "That's not good, [player]!"
                m "It really hurts me to know that you aren't doing well anymore."
                m 3euc "If there is anything I can do to help you feel any better mentally, just let me know."
                m 3eua "After all, what kind of girlfriend would I be if I didn't want to help you, [player]!"
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                return
    elif persistent._mentalhealth_last_checkup == store.mentalhealth.CHECKUP_NEUTRAL:
        m 1hua "Oh hello, [player]!"
        m 3eua "I know I already asked you how you were feeling mentally before... {w=0.2}{nw}"
        extend 1eua "And you told me your mental health was decent."
        m 1esc "Just to check up on you again though [player]..."
        call mentalcheckupscript
        menu:
            m "Has that changed, [player]?{fast}"
            "No I am still feeling alright.":
                m 1eua "Alright [player], I am glad you are still fine today."
                m 3eua "Let's continue to spend more time together!"
                return
            "My mental state actually got better recently!":
                m 3hsa "That's exciting to hear, [player]!"
                if mas_isMoniHappy(higher=True):
                    m 3euu "Did thinking of me help you today?"
                    m 1hua "Hehe~"
                    m 5eubla "I know thinking of you helps me get through everyday, [player]."
                    m "I love you so much, [mas_get_player_nickname()]."
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                    return "love"
                else:
                    m 3eud "Whoever helped you mentally, you should be thankful for their help, [player]."
                    m 3euc "Not a lot of people ask for help either, which doesn't help them..."
                    m 3husdlb "Sorry, I am getting off track [player]!"
                    m 3eua "Let's spend more time together, okay?"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                    return
            "My mental state got worse Monika...":
                m 1ekc "That's not good, [player]!"
                m 3ekc "Did something bad happen while you were gone?"
                m 1euc "Well, whatever it was that happened, I know you handled it well."
                if mas_isMoniHappy(higher=True):
                    m 3hub "Maybe even thinking of me can help!"
                    m 3eua "And if not, you can always vent to me about your problems, [player]."
                    m 1eua "I love you~"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                    return "love"
                else:
                    m 3euc "Make sure to talk to a therapist about your problems too."
                    m 1euc "Just talking to someone you care about can really make you feel much better. "
                    extend 3eud "Both mentally and emotionally."
                    m 1eub "Remember, I am always here for you, [player]!"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                    return
    elif persistent._mentalhealth_last_checkup == store.mentalhealth.CHECKUP_BAD:
        m 3eub "Hey, [player]!"
        m 1euc "I know this is a awkward to bring up already..."
        m 3ekd "Especially since you told me your mental health wasn't good in the first place before..."
        m "Well, may I ask you if your mental state has improved, [player]?"
        call mentalcheckupscript
        menu:
            m "Well, may I ask you if your mental state has improved, [player]?{fast}"
            "I don't want to talk about it right now...":
                m 1dkc "{W=1}Oh... {nw}"
                m "{w=1}Well... {nw}"
                m 1euc "Well, just know that I want to best for you, [player]."
                return
            "My mental state actually got better Monika!":
                m 3eua "That's good to hear, [player]!"
                if mas_isMoniHappy(higher=True) and renpy.random.randint(1,4) == 1:
                    m 3tuu "Was I the reason why your mental state got better?{nw}"
                    $_history_list.pop()
                    m 1eua "Well, I am just glad that you are better mentally, [mas_get_player_nickname()]."
                    m 3eua "Let's continue to spend more time together!"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                    return
                else:
                    m 1eua "I am just glad that you are better mentally, [mas_get_player_nickname()]."
                    m 3eua "Let's continue to spend more time together!"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                    return
            "...":
                m 1dkc "..."
                m 3eua "Well, let's just carry on with our day then, [player]..."
                return

    else:
        m 1hua "Oh hello, [player]!"
        m "I know this may seem awkward to ask you..."
        call mentalcheckupscript
        $ _history_list.pop()
        menu:
            m "How is your mental health right now [player]?{fast}"
            "It's really good!":
                m 1hub "I'm really happy to hear that, [player]!"
                m 1eua "whether it's just a good day or an improvement on your mental health, it is always nice to hear you are doing well."
                m 3hub "And I will do my best to continue to support you, [mas_get_player_nickname()]!"
                m 5eua "What kind of girlfriend would I be if I didn't?"
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                $ _history_list.pop()
                return
            "It's decent Monika...":
                m 1euc "Oh..."
                m 3euc "Well, that could be good or bad."
                m 4eud "And if it {i}is{/i} bad, then we can always talk about it if you want to, [player]."
                m 3eua "I want to try and make sure you're always happy."
                extend 1eka "Because that's what makes me happy."
                m 1hua "I'll be sure to try my best to support you, I promise."
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                $ _history_list.pop()
                return
            "It's really bad right now...":
                m 1euc "That's not good at all, [player]..."
                m 3eud "If you ever get too upset or need to take a break just let me know, [player]. {w=.06}Okay?"
                m 1eua "I will always be here for you! Never forget that!"
                m 1eubsa "I love you and always will, [player]!"
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                return
return



init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalhealthcheckupdialoguefinal",
            category=["you", "mental health"],
            prompt="[player]'s Mental Health",
            action=EV_ACT_QUEUE,
            start_date=persistent._nextmentalcheckup,
            end_date=persistent._mentalcheckupdeadline
            )
        )

label mentalhealthcheckupdialoguefinal:
    if persistent._mentalhealth_last_checkup == store.mentalhealth.CHECKUP_GOOD:
        m 1hua "Hey, [player]."
        m 3eua "I know I already asked you how you were mentally before... {w=0.2}{nw}"
        extend 7hub "And you told me your mental health was good!"
        m 1esd "Just to check up on you though..."
        call mentalcheckupscript
        m 1esc "Has that changed, [player]?"
        menu:
            m "Has that changed, [player]?{fast}"
            "No, I am still feeling really great today!":
                m 3eua "Alright [player], then let's continue having a good day together!"
                return "derandom"
            "My mental state got worse today.":
                m 1ekc "That's not good, [player]!"
                m "It really hurts me to know that you aren't doing as well anymore."
                m 3euc "If there is anything I can do to help you feel any better mentally just let me know, [player]!"
                m 3eua "After all, what kind of girlfriend would I be if I didn't want to help you!"
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                return "derandom"
    elif persistent._mentalhealth_last_checkup == store.mentalhealth.CHECKUP_NEUTRAL:
        m 1hua "Hey, [player]..."
        m 3eua "I know I already asked you how you were feeling mentally before... {w=0.2}{nw}"
        extend 1eua "And you told me your mental health was decent."
        m 1esc "Just to check up on you again though, [player]..."
        call mentalcheckupscript
        menu:
            m "Has that changed, [player]?"
            "No I am still feeling alright.":
                m 1eua "Alright [player], I am glad you are still fine today."
                m 3eua "Let's continue to spend more time together! Hehe~"
                return "derandom"
            "My mental state actually got better recently!":
                m 3hsa "That's exciting to hear [player]!"
                if mas_isMoniHappy(higher=True):
                    m 3tuu "Did thinking of me help you today?"
                    m 3hub "Hehe~"
                    m 5hublb "I know thinking of you helps me get through everyday, [player]."
                    m 5eubfa "I love you so much, [mas_get_player_nickname()]."
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                    return "love|derandom"
                else:
                    m 4esd "Whoever helped you mentally, you should be thankful for, [player]."
                    m 7euc "Not a lot of people ask for help either, which doesn't help them..."
                    m 3rusdlb "Sorry, I am getting off track, [player]!"
                    m 3eua "Let's spend more time together. {w=0.6}Okay?"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                    return "derandom"
            "My mental state got worse Monika...":
                m 1euc "That's not good, [player]!"
                m 3eud "Did something bad happen while you were gone?"
                m 1euc "Well, whatever it was that happened, I know you handled it well."
                if mas_isMoniHappy(higher=True):
                    m 7kuu "Maybe even thinking of me can help!"
                    m 3eua "And if not, you can always vent to me about your problems, [player]."
                    m 5eubla "I love you~"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                    return "love|derandom"
                else:
                    m 3euc "Make sure to talk to a therapist about your problems too."
                    m 4eud "Just talking to someone you care about, can really make you feel much better. {w=0.3}"
                    extend "Both mentally and emotionally."
                    m 7euc "Remember, I am always here for you, [player]!"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                    return "derandom"
    else:
        m 1hua "Hey, [player]."
        m "I know this may seem awkward to ask you..."
        m "How is your mental health right now, [player]?"
        call mentalcheckupscript
        $ _history_list.pop()
        menu:
            m "How is your mental health right now, [player]?{fast}"
            "It's really good!":
                m 1hub "I'm really happy to hear that, [player]!"
                m 1eua "Whether it's just a good day or an improvement on your mental health, it is always nice to hear you are doing well."
                m 3hub "And I will do my best to continue to support you, [mas_get_player_nickname()]!"
                m 5eua "What kind of girlfriend would I be if I didn't?"
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_GOOD
                $ _history_list.pop()
                return "derandom"
            "It's decent Monika...":
                m 1ekc "Oh..."
                m 2eka "Well, that could be good or bad."
                m "And if it {i}is{/i} bad, then we can always talk about it if you want to, [player]."
                m 3eua "I want to try and make sure you're always happy. "
                extend 1eka "Because that's what makes me happy."
                m 1hua "I'll be sure to try my best to support you, I promise."
                $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_NEUTRAL
                $ _history_list.pop()
                return "derandom"
            "It's really bad right now...":
                m 1euc "That's not good at all, [player]..."
                m 3euc "If you ever get too upset or need to take a break just let me know, [player], okay?"
                if mas_isMoniHappy(higher=True) and renpy.random.randint(1,3) == 1:
                    m 7eua "Would a hug help you feel better, [player]?"
                    menu:
                        "Not right now Monika...":
                            m 1euc "Oh..."
                            m 1eua "Alright, [player]."
                        "Actually, that would be great Monika.":
                            m 3eua "You can hold me as long as you like, [player]."
                            call monika_holdme_prep(lullaby=MAS_HOLDME_NO_LULLABY, stop_music=True, disable_music_menu=True)
                            call monika_holdme_start
                            call mentalplayerhugreactions
                    m 7eua "You already know that I will always be here for you, [player], never forget that!"
                    m 5eubsa "I love you and always will, [player]!"
                    $ persistent._mentalhealth_last_checkup = store.mentalhealth.CHECKUP_BAD
                    return "love|derandom"
return "derandom"


label mentalplayerhugreactions:
    $ elapsed_time = datetime.datetime.now() - mental_hugtimestart
    $ store.mas_history._pm_holdme_adj_times(elapsed_time)

    if elapsed_time > datetime.timedelta(minutes=10):
        m 6dubsa "Mmm..."
        m 6eubfa "Oh! You held me for so long even my worries melted away!"
        m 5eubfa "I hope you feel better now [player]. {w=0.3}{nw}"
        extend "I know I do hehe~"
        return

    elif elapsed_time > datetime.timedelta(minutes=2):
            m 6wubso "Oh?"
            m 6eubfa "You held me for so long, I was starting to melt away too!"
            m 5eubfa "I'm really glad you wanted to hold me, [player]."
            m 7hubsa "You already know I always want you to be at your best. {w=0.3}{nw}"
            extend 1ekbfb "So I hope you feel much better now, [player]."
            show monika 5tubfb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5tubfb "Maybe we could even hug a bit more for good measure?"
            m 5tubfu "Ehehe~"

    elif elapsed_time > datetime.timedelta(seconds=30):
            m 1eub "Ah~"
            m 1hua "I feel much better now!"
            m 1eua "I hope you do too."
            m 2rksdla "Well, even if you don't..."
            m 3hubsb "You could always hold me again, ahaha!"
            m 1hkbfsdlb "Actually...{w=0.5} you can hold me again either way~"
            m 1ekbfa "Just let me know when you want to~"

    else:
        m 1hua "That was a bit short, but still nice~"
        m 1eua "Let's spend more time together, okay [player]?"
return

    # forced greetings after an appointment
init -1 python in mas_greetings:
    import store
    import store.mas_ev_data_ver as mas_edv
    import datetime
    import random

    # TYPES:
    TYPE_MentalAppointment = "Appointment"

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="mental_return_from_appointment",
            unlocked=True,
            category=[store.mas_greetings.TYPE_MentalAppointment],
        ),
        code="GRE"
    )
#mentalroom_greeting_ear_disability

label mental_return_from_appointment:
    m 1hub "Welcome back, [player]!"
    if persistent._mental_player_therapytype == True:
        m 3eub "Did you learn any new skills?"
        m 7eub "Or maybe you learned more about yourself?"
        m 7hub "Either way, I am glad you are back, [mas_get_player_nickname()]!"

    if not persistent._mental_player_therapytype:
        m 3eub "I hope your appointment went well!"
        m 3eka "And if it didn't, I am always here for you, [player]."
        m 7hub "Either way, I am glad you are back, [mas_get_player_nickname()]!"

return

init 5 python:
    gmr.eardoor.append("mentalroom_greeting_ear_disability")

label mentalroom_greeting_ear_disability:
    m "Autism speaks?"
    m "That doesn't sound too bad...{w=2.0}{nw}"
    m "Oh my gosh!"
    m "Why would anyone say that about Autism?"
    jump monikaroom_greeting_choice

init 5 python:
    gmr.eardoor.append("mentalroom_greeting_research")

label mentalroom_greeting_research:
    m "Hmm..."
    m "There are a tone if things I haven't heard of here..."
    jump monikaroom_greeting_choice
