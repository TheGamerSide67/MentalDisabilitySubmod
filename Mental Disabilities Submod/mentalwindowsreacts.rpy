init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mentalhealthwrs_rhythmgames",
            category=[r"(?i)Taiko no Tatsujin, Osu!|DJMAX RESPECT|Friday Night Funkin'"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle = True
        ),
        code="WRS"
    )

label mas_wrs_mentalhealthwrs_rhythmgames:
    python:
        title = mas_getActiveWindowHandle()
        titlereact = title.lower()

        if 'youtube' in titlereact:
            mentalrhythmgamesquips = [
                "Watching someone else play, [player]?",
                "This game looks really fun, [player]!",
                "Watching anything impressive, [player]?"
            ]
            
            mentalrhythmgamechoice = renpy.random.choice(mentalrhythmgamesquips)


            wrs_success = mas_display_notif(
                m_name,
                [mentalrhythmgamechoice],
                'Window Reactions'
            )        
            
            
            else:
            mentalrhythmgamesquips = [
            "Playing a rhythm game, [player]?",
            "This game looks really fun, [player]!",
            "Trying to get a new highscore, [player]?",
            "This look like it can be challenging! \nI hope that isn't an issue for you, [player].",
            "Mind if I watch you play, [player]?",
            "Going for a full combo? \nYou can do it, [player]!"
            ]
            
            mentalrhythmgamechoice = renpy.random.choice(mentalrhythmgamesquips)


            wrs_success = mas_display_notif(
                m_name,
                [mentalrhythmgamechoice],
                'Window Reactions'
            )





    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_mentalhealthwrs_rhythmgames')
    return
