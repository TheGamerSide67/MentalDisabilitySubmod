init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mentalhealthwrs_rhythmgames",
            category=["Taiko no Tatsujin", "Osu!", "DJMAX RESPECT", "Friday Night Funkin'"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

#oddly enough, the only way for new windows reacts to be made, is by only using the prefix "mas_wrs_"
#Anything else results in errors or problems


#I plan to change this later, allowing Monika to detect if it's on Youtube, a store, or the game itself
#so dialog is more personalized with everyone
label mas_wrs_mentalhealthwrs_rhythmgames:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Playing a rhythm game, [player]?",
            "This game looks really fun, [player]!",
            "Trying to get a new highscore, [player]?",
            "This look like it can be challenging! /nI hope that isn't an issue for you, [player].",
            "Mind if I watch you play, [player]?",
            "Going for a full combo?/nYou can do it, [player]!"
        ],
        'Window Reactions'
    )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_mentalhealthwrs_rhythmgames')
    return