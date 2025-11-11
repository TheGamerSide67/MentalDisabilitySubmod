default persistent._mental_health_player_goes_to_therapy = None

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="mental_leave_therapist",
            unlocked=True,
            prompt="I'm going to an appointment.",
            pool=True
        ),
        code="BYE"
    )

label mental_leave_therapist:
    m 3eua "Going to an appointment?"
    m 7eub "I am happy that you are taking care of yourself!"
    m 3eud "Are you going to an appointment for your mental health, [player]?"
    menu:
        "Yes":
            m 1eua "I wish you the best of luck, [player]."
            m 3eua "I'll see you when you get back!"
            m 1hub "I love you~"
            $ persistent._mental_player_therapytype = True

        "No":
            m 1eua "I wish you the best of luck, [player]."
            m 3eua "I'll see you when you get back!"
            m 1hub "I love you~"
            $ persistent._mental_player_therapytype = False


$ persistent._mental_health_player_goes_to_therapy = True
$ persistent._mas_greeting_type_timeout = datetime.timedelta(hours=5)
$ persistent._mas_greeting_type = store.mas_greetings.TYPE_MentalAppointment
return "quit"

