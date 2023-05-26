init python:

    import store.mas_calendar as calendar
    import datetime

    calendar.addRepeatable("MentalHealthAwareness",_("Start of MHAM"),month=5,day=1,year_param=list())
    calendar.addRepeatable("MentalHealthAwarenessEnd",_("End of MHAM"),month=5,day=31,year_param=list())

#Setup The years for the Mental Health Awareness Month
default persistent._mentalhealthmonthstart = datetime.date(datetime.date.today().year, 5, 1)
default persistent._mentalhealthmonthend = datetime.date(datetime.date.today().year, 5, 31)
default persistent._mentalhealthleapyear = 4


#create a label to add a year after the event ends
#Also adds a system for leap years
label mentalhealthmonthsetup:
    python:
        if persistent._mentalhealthleapyear >= 4:
            persistent._mentalhealthmonthstart = datetime.timedelta(days=366) + persistent._mentalhealthmonthstart
            persistent._mentalhealthmonthend = datetime.timedelta(days=366) + persistent._mentalhealthmonthend
            persistent._mentalhealthleapyear = 0

        else:
            persistent._mentalhealthmonthstart = datetime.timedelta(days=365) + persistent._mentalhealthmonthstart
            persistent._mentalhealthmonthend = datetime.timedelta(days=365) + persistent._mentalhealthmonthend
            persistent._mentalhealthleapyear = persistent._mentalhealthleapyear + 1

    $ mas_getEV("MentalHealthMonth").start_date = persistent._mentalhealthmonthstart
    $ mas_getEV("MentalHealthMonth").end_date = persistent._mentalhealthmonthend
return

#Mental Health Awareness Month Dialogues
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="MentalHealthMonth",
            category=["you", "mental health"],
            prompt="Mental Health Awareness Month",
            action=EV_ACT_QUEUE,
            start_date=persistent._mentalhealthmonthstart,
            end_date=persistent._mentalhealthmonthend,
            random=False,
            rules={"no_unlock"},
            years=[]
            )
        )

label MentalHealthMonth:
    m 1eua "Do you know what month it is, [player]?"
    m 3hua "It's Mental Health Awareness Month!"
    m 1eub "I know the month sounds a bit silly, but it is meant to help bring awareness to different mental health issues."
    m 3eub "There are some places that host events this month, to help promote it too!"
    m 7eua "The month's motto is pretty simple; '{i}more than enough{/i}'."
    m 1eua "It's to say that waking up, or spending time with other people, is '{i}more than enough{/i}' to make others happy."
    m 3eub "There is even a specific color to mental health awareness month! {w=0.8}{nw}"
    extend 7sub "That color is green!"
    m 3eua "Ahaha, I guess it's almost too perfect for me of all people to celebrate this month with you. "
    if mas_getEV("MentalHealthMonth").shown_count >= 2:
        extend 1rusdlb "Even if it isn't the first time we have, [player]."
    else:
        pass
    m 1eub "Anyway, there are ton of acivities you can do online, or with a friend to help support Mental Health Awareness Month."
    m 3hub "One of them is to host a coffee breakfast!"
    m 1eubla "Doesn't that sound nice and relaxing, [player]?"
    if mas_getEV("mentalmeditation").shown_count >=1:
        m 7hublb "Or maybe we could meditate together too!"
        m 1dubsu "Just hearing our breaths, and focusing on nothing but our thoughts."
        m 3tua "You'd have to be careful not to get too distracted, ahaha!"
    m 3eub "There are a ton of things that you could do too, not just these few examples I gave you."
    m 1eua "Well, the most important thing that you can't forget, [player], is to tell someone that they are loved."
    m 3eua "Share some of your time with someone else, and let them know that you care about them."
    call mentalhealthmonthsetup
    if persistent._mas_pm_has_friends:
        m 7eub "Call or talk to your close friends, and plan something together."
        m 1eua "Just make sure to plan something relaxing. Everyone needs a break from something, and you'd be a great friend planing that out for them."
    else:
        m 7eua "Make sure to tell your parents that you care for them."
        m 1eud "Everyone needs a break from something, so reassuring them that you care can mean a lot to them, [player]."
    m 1eua "Anyways, [player]. I want to tell you that I really care for you, [mas_get_player_nickname()]."
    if persistent._mental_player_has_autism == True:
        m 3eubla "Your autism will never change how I think about you, and I will always do my best to make sure you feel welcomed."
        m 5eubsa "I really do love you, [mas_get_player_nickname(exclude_names=['my love', 'love'])]."
    elif persistent._player_has_disabilities == True:
        m 3eubla "Your disabilities will never change how I think of you, [player]."
        m 1hubsb "I will always be here for you, and I will make sure I will do everything I can to make you happy."
        m 5eubsa "I love you, [mas_get_player_nickname(exclude_names=['my love', 'love'])]."

    else:
        m 3eubla "No matter what you are going through, I will always be here for you, [mas_get_player_nickname()]."
        m 1eubsa "I will do my best to make sure you are happy, and to help you calm down whenever you get upset."
        m 5dubsa "I truly do love you, [mas_get_player_nickname(exclude_names=['my love', 'love'])]."
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalhealthmonthresettime",
            category=["monika"],
            prompt="Mental Health Variables",
            action=EV_ACT_QUEUE,
            start_date=datetime.date.today(),
            end_date=datetime.date(2023, 12, 31),
            random=False,
            rules={"no_unlock"}
            )
        )

label mentalhealthmonthresettime:
    m 1eua "Hey, [player]..."
    m 1eud "I am going to go check on something, I'll be right back..."
    call mas_transition_to_emptydesk
    pause 5.0
    call variablesresetmentalchange
    call mas_transition_from_emptydesk()
    m 1eua "I am back now, [player]."
return "derandom"

label variablesresetmentalchange:
    $ mas_getEV("mentalhealthcheckupdialoguefinal").action = EV_ACT_QUEUE
    $ mas_getEV("MentalHealthMonth").action = EV_ACT_QUEUE
    $ persistent._mentalhealthmonthstart = datetime.date(2024, 5, 1)
    $ persistent._mentalhealthmonthend = datetime.date(2024, 5, 31)
    $ persistent._mentalhealthleapyear = 0
    $ mas_getEV("MentalHealthMonth").start_date = persistent._mentalhealthmonthstart
    $ mas_getEV("MentalHealthMonth").end_date = persistent._mentalhealthmonthend
    $ persistent._lastmentalcheckup = datetime.date.today()
    $ persistent._nextmentalcheckup = datetime.date.today() + datetime.timedelta(days=1)
    $ persistent._mentalcheckupdeadline = persistent._lastmentalcheckup + datetime.timedelta(days=30)
    $ mas_getEV("mentalhealthcheckupdialoguefinal").start_date = persistent._nextmentalcheckup
    $ mas_getEV("mentalhealthcheckupdialoguefinal").end_date = persistent._mentalcheckupdeadline
return

