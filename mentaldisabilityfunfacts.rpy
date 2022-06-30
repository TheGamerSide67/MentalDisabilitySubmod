init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="mental_illnesses",
        ),
        code="FFF"
    )

label mental_illnesses:
    m 3euc "Did you know that there are actually over 300 mental disabilities?"
    m 3eud "This is an insane amount isn't it [player]?"
    m 2euc "Though these are only the documented disabilities."
    m "I am sure there are much more out there that aren't even documented yet!"
    m "That just means there is always more to learn!"
    #Call the end
    call mas_fun_facts_end
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="mental_misdiagnoseshistory",
        ),
        code="FFF"
    )

label mental_misdiagnoseshistory:
    m 3euc "Did you know that autism used to be diagnosed as schizophrenia back in 1908."
    m 3eud "This is because before research was done and the offical term autism was created, only the similarities of schizophrenia were recognized."
    m 7eud "Obviously this changed more after the 1940s, after Grunya Sukhareva has started to study more of these cases and even created the theory of autism!"
    m 3euc "Though her work is not quoted in any modern studies of autism..."
    m 1eud "There is a lot of history to autism here... " 
    extend 3eub "It's really interesting too!"
    call mas_fun_facts_end
return