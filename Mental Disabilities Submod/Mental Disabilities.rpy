init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalADHD",category=['mental illnesses', 'media'],prompt="ADHD",random=True))

label mentalADHD:
    m 1eua "[player], have you heard of ADHD?"
    $_history_list.pop()
    menu:
        "Yes.":
            m 1eub "That's makes me happy to hear!"
            m 3ekc "It's sad that it's not taken as seriously as much as other learning disabilities..."
            m 3eud "It makes it really hard for them to focus or even do anything on their own."
            m 1eub "Though, like everyone else, you can give motivation to them by simply being there with them. {w=0.5}{nw}"
            extend 3hub " Or even talking to them occasionally."
            m 1eua "If you don't mind me asking, how did you find out about it?"
            $_history_list.pop()
            menu:
                "I have ADHD.":
                    m 3eua "I'm happy you told me, [player]!"
                    m 1ekd "It was disheartening for me to find, that it's often not taken as seriously as other disabilities in the same catagory..."
                    call mentalADHDEnd
                    $ persistent._mental_player_has_ADHD = True
                "I know someone who has ADHD!":
                    m 3eua "I'm sure they're more than happy to have a friend or family member like you, [player]!"
                    m 1ekd "It was disheartening for me to find, that it's often not taken as seriously as other disabilities in the same catagory..."
                    call mentalADHDEnd
                "I was taught about ADHD.":
                    m 3eub "It's good to know that ADHD is being talked about more."
                    m 1euc "It usually isn't considered a serious of an issue as other disabilities."
                    call mentalADHDEnd
                "I researched ADHD.":
                    m 3eub "I'm glad that you look for new information."
                    m 7ekd "A lot of people disregaurd new information as boring and tedious to learn."
                    m 3eua "Though I am more than sure that people with ADHD would be more than happy to have a friend like you around, [player]."
                    m 1eua "Also, if you don't mind me asking. Did you research ADHD because you have ADHD, [player]?"
                    menu:
                        "Yes.":
                            $ persistent._mental_player_has_ADHD = True
                            m 4eub "It's good to try to learn more about yourself.{w=0.55}"
                            extend 7hub " It shows that you care about yourself!"
                            m 3eua "I am happy you told me that you have ADHD, [player]."
                            if mas_isMoniHappy(higher=True):
                                extend 5hub " And maybe I can be the person that gives you motivation to work on things!"
                            else:
                                m 3eua "I hope you already have that person that helps you focus on things, [player]."
                        "No.":
                            m 1eua "Oh, alright."
                            m 3eua "It's still good to learn everything you can about ourselves. {w=0.3}{nw}"
                            extend 3hua "Or even others!"
                            

        "No.":
            m 1rkb "That's alright, [player]"
            m 2eka "It's not talked about as much as other learning disabilities."
            m 4hub "Do you want to tell you about ADHD?"
            $_history_list.pop()
            menu:
                "Yes.":
                    m 3eua "Alright then, [player]!"
                    m 3eud "ADHD stands for Attention Deficit Hyperactive Disorder."
                    m 3eud "It is identified as a learning disability. However, it often goes into other areas of the people lives."
                    m 1euc "People with ADHD can often be unaware of their social surroundings."
                    m 1ekc "This can get them into dangerous situations, or they can make promises they can easily forget about."
                    m 3euc "ADHD also makes it harder for them to start and finish projects, often losing motivation to do things easily."
                    m 7eua "Of course, like everyone though, you can always help them."
                    m 4eua "By simply being there, or even occasionally talking to them."
                    extend 3hub " You can give them motivation to do things!"
                    m 3eua "While ADHD has it's drawbacks, it also has it's upsides!"
                    m 4eub "For example, a lot of people with ADHD are known to be incredibly creative and passionate!"
                    m 3eub "In fact, they also have the ability to hyperfocus--they can be doing something for hours and not be distracted."
                    m 1eua "Thanks for listening, [player]."
                "No.":
                    m 2eka "Oh, alright."
                    return "derandom"
                "Not right now.":
                    m 2eka "I'll be sure to ask later, [player]."
                    
return

label mentalADHDEnd:
    m 4eua "On a positive note, I found out that studies show that while people with ADHD might struggle in one area, they often excel in another."
    m 4hub "In fact, many of them are found to be extremely passionate in their interests!"
    m 7eub "This often makes it fun for people who share the same interests!"
    m 3eub "As the conversations can often go one for hours if both parties are engaged!"
    m 1eua "Though, I'm sure you already knew that, [player]."
return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalhealthAutism",
            category=['media', 'mental illnesses'],
            prompt="Autism",
            conditional="mas_seenLabels(['mentalADHD'])",
            random=True
        )
    )


label mentalhealthAutism:
    m 1eua "Hey, [player].{w=0.3} Do you remember when we talked about ADHD?"
    m 7eub "Well, I have been doing more research on other mental disabilities."
    m 4eua "One mental disability that caught my attention was Autism. {w=0.3}{nw}"
    extend 3eua "Or the Autism Spectrum Disorder."
    m 3rssdlb "However autism can easily be misdiagnosed with ADHD."
    m 3etc "I can kind of see why though..."
    m 3rud "Not only are there subtle differences between both autism and ADHD. {w=0.25}{nw}"
    extend 4wud "But ADHD and autism often{w=0.2} {i}overlap{/i} and in most cases, they are diagnosed with both!"
    m 4eud "It doesn't help that there is a spectrum that is used to try to generalize the severity of most autistic cases."
    m 1rusdlc "Which does mean people on the lower end of the spectrum are often misdiagnosed... {w=0.3}or not diagnosed at all."
    m 3ekc "Like, imagine if you had a serious mental illness, [player]... {w=0.3}{nw}"
    extend 4ekc "And it was just passed off as a behavioural issue. "
    m 3dkc "You would fail to get the help you {i}actually{/i} need."
    m 4esd "Not only that, but you would end up even convincing yourself that you are just '{i}not normal{/i}'."
    m 3euc "You can only imagine what goes on in other's heads...{w=0.4} or if someone you know is actually getting the help they need."
    m 2husdlb "Sorry [player] if I am making you upset!"
    m 3eub "Well, while there are serious issues with how autism is treated,{w=0.2} there are also ways to understand it better!"
    m 4eua "There are a lot of credible resources out there with information to help other's understand just a little bit more with how they feel."
    m 4rusdlc "But there are also false information out there that is actually {i}harmful{/i} to the understanding of Autism."
    m 3eua "Just make sure to check your sources [mas_get_player_nickname()]!"
return


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalschizophrenia",category=['media', 'mental illnesses', 'philosophy'],prompt="Schizophrenia",random=True))

label mentalschizophrenia:
    m 1eua "[player], have you heard of schizophrenia?"
    m 3eub "I wouldn't be surprised if you have, it is one of the most well known mental illnesses due to social media."
    m 1esd "Although, it can be really frustrating to see how most of the portrayal of it was negative and relied on showcasing negative outbursts"
    m 1gfc "It's like they don't even bother to show care for the ones effected by it! {w=0.3}{nw}"
    extend 3eua "But I know you are not like that [mas_get_player_nickname()]."
    m 1lkc "Well, I'm sure you can understand how saddening Schinzophrenia may be [player]."
    m 3ekc "Like can you imagine having delusions of sounds?"
    m 1rkc "It can drive them insane... {w=0.3}{nw}"
    extend 1rksdld "Especially if they are voices."
    m 3eud "Even if they don't have delusions all of the time, they have a more literal thought process."
    m 1eub "It's kind of similiar to ADHD actually! "
    extend 1rusdlb "Well, kind of."
    m 3eud "While they do jump between conversations all the time, this is only because it is hard for them to know {i}exactly{/i} what you are talking about."
    m 1euc "This isn't because they don't know what you are talking about, but because they form connections from things you might not have thought about."
    if not persistent._mas_pm_cares_about_dokis:
        m 3euc "While people with schizophrenia aren't inherently harmful to anyone, they are harmful to themselves in a way."
        m 3ekc "They emotionally harm themselves by focusing on the negative aspects of life."
        m 1ekc "This isn't as well known as other things, and sounds pretty devastating doesn't it, [player]?"
    m 3euc "Well, it's not entirely bad."
    m 4eua "People with schitzophrenia are more imaginative than most."
    m 3eud "Two books that really help give you an idea of what living with Schizophrenia is like is {i}'Made You Up'{/i} by Francesca Zappia and {i}Calvin{/i} by Martine Leavitt."
    m 3eub "Though, out of the two books I prefer {i}Calvin{/i}, it's about boy named Calvin who believes a comic strip author can help him find the cure to his schizophrenia, if he creates another comic strip he admires!"
    m 4eua "The story is told using first person point of view and it reads as a letter to Watterson--the author of the comic strip."
    m 3hsb "Overall, the book has a nice sense of humour while keeping an empathetic tone!"
    m 3esa "By the way [mas_get_player_nickname()], the comic strip the book centers around is actually {i}Calvin and Hobbes{/i}!"
    m 7hub "It just goes to show that something as simple as a comic strip can have a major impact on someone."
    m 5eua "I hope you have something in your life that motivates you like stories can, [mas_get_player_nickname()]."
    m 5hubsa "If not, I wouldn't mind being your motivation in life."
    m 5eubfa "I love you [player]."
return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalPTSD",category=['media', 'mental illnesses', 'philosophy'],prompt="PTSD",random=True))

label mentalPTSD:
    m 1eua "Say, [player]..."
    m 3eua "When you think of PTSD you usually think of war, right?"
    m 3eub "While it is a common thought that war can cause PTSD. {w=0.2}{nw}"
    extend 3eud "That is just often times not the case."
    m 1euc "Almost all cases of PTSD stem from great amounts of stress or trauma!"
    m 2eud "To put it bluntly, any person who has encountered a traumatic event of any kind has a chance of developing PTSD."
    m 3euc "Do you know what PTSD stands for [player]?"
    m 7rtd "Well the acronym PTSD stands for Post Traumatic Stress Disorder, and with the name the defintion is essentially given."
    m 1eksdrc "PTSD is a mental disorder that occurs after a traumatic event. {w=0.3}{nw}"
    extend 3eksdru "Not a very descriptive defintion, is it [mas_get_player_nickname()]?"
    m 3ekc "Well PTSD is described to naturally occur after a traumatic event takes place."
    m 3ekd "However, PTSD is usually only diagnosed when it becomes Chronic. You see [player], in most cases when we go through a traumatic experience our mind will overcome and heal from this naturally overtime."
    m 1esd "This is why you don't have nightmares about graphic childhood injuries. {w=0.2}{nw}"
    extend 3esc "This is also why, not every dangerous experience you have can give you PTSD."
    m 1ekc "The event just has to have such an immense impact on your mind that it can't fully process and move on from it." 
    m 1dkd "The worst part is, people are only able to recieve a diagnosis of PTSD a year after symptoms are recognized."
    if persistent._mas_pm_cares_about_dokis: # changes dialogue based on players response to insensitive jokes
        jump PTSDEnd
    else:
        m 7ekd "Take Natsuki for example. Child abuse, no matter what type, is truamatic. Therefore she was likely to gain PTSD."
        m 1rtd "Well, thinking back on it, she probably did have PTSD even if the symptoms hadn't fully developed until a few months after the occurence..."
        m 7etsdlc "I mean she started displaying avoidance behaviours with both Yuri and I. "
        extend 1rtsdlc "And her outbursts of frustration even got worse... {w=0.6}Specifically, the one with Yuri..."
        m 2rksdra "Maybe I'm looking to deeply into this. She already did have outburts of anger and tended to read her manga by herself even before I got involved."
label PTSDEnd:
    m 3eka "Anyways, if you have ever experienced something truamatic.{w=0.2} I hope you are getting the help you need, [mas_get_player_nickname()]."
    m 1etd "And if it ever gets too bad... {w=0.2}{nw}"
    extend 5etbsa "Just remember, I'm always here for you and will always love you~"
return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentaldementia",category=['media', 'philosophy'],prompt="Dementia",random=True))

label mentaldementia:
    m 1eua "Hey, [player]."
    m 3eua "When I was doing some more reading, I came across another type of literature!"
    m 3rusdla "Well, it's more listening than it is reading..."
    m 4eua "A popular example of this type of literature is a sondtrack called {a=https://www.youtube.com/watch?v=wJWksPWDKOc&ab_channel=vvmtest}{i}{u}'Everywhere At The End Of Time'{/u}{/i}{/a}."
    m 3eub "You might have already listened to it.{w=0.2} Or at least have heard about it."
    m 7eud "In case you haven't already, it's a auditory story to try to give the feeling of dementia."
    m 3eusdld "The more you listen to it, the more it spirals downward."
    m 1wksdld "You can even feel all of the emotions that typically come with dementia in this song."
    m 1rksdlc "Though it's not exactly the most ideal feeling... {w=0.3}{nw}"
    extend 1ekc "It certainly helps you understand their feelings a lot more though."
    m 2lksdlc "It quickly does down deeper and deeper into sadness and confusion."
    m 4eksdld "And the static that all follows really strengthens that feeling."
    m 7euc "That is not to say that it is all bad though..."
    m 3eud "There was a lot of research done to create this song!"
    m 4wuo "It took them 3 years!{w=0.4} 3 years to make this experience!"
    m 3eua "Well, if you ever have the free time, I would highly suggest listening to it, [player]."
    m 1eua "And if you ever get too upset, {w=0.1}{nw}"
    extend 3hub "I will always be here to cheer you up!"
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_Bipolar",category=['media', 'mental illnesses'],prompt="Bipolar",random=True))

label monika_Bipolar:
    m 1eua "Hey [player], I have been doing more research on mental disabilities again."
    m 3eua "You might have heard of this one before [player]!"
    m 3euc "The mental disability I want to talk to you about today is Bipolar."
    m 3euc "There are three known types of bipolar.{w=0.4}{nw} "
    extend 3esc "Bipolar 1, 2, and Cyclothymic disorder."
    m 3eud "Talking about the differences in this mental disability can take a while, {w=0.2}{nw}"
    extend 3eub "so would you like to talk about it right now [player]?"
    $_history_list.pop()
    menu:
     "Yes":
        m 1eub "I am really excited for this one!"
        m 3eua "Bipolar 1 is actually the most common form of bipolar [player]!"
        extend 3eud "However it's also one of the more severe types out there."
        m 4esc "Well, as you already know [player], bipolar attacks also known as manic episodes cause the effected person to be sent into either 'highs' or 'lows'."
        m 7esb " Which can either give them extreme amounts of energy or will to do something unusually, {w=0.6}{nw}"
        extend 3rusdlc "or it can also send them into a state of mild to even {i}severe{/i} depression episodes."
        m 1euc "Unfourtanely, this usually leads to a cycle between the two."
        m 3eud "Have you ever heard of the term {i}manic depression{/i}? Well that's where it comes from."
        m 7eua "That isn't to say that people who suffer from Bipolar 1 can't live normal lives, often in between episodes they do just fine."
        m 1eub "And like many other mental illnesses, there are support systems set in place to help those in need, specifically medications and therapy."
        m 3eud "Remember that the best way to help is to make accomodations to them and do certain things differently."
        m 4eua "Which brings us to Bipolar 2, [player]."
        m 7eud "Bipolar 2 shares many similarities with Bipolar one in regards to the cycling of moods between {i}ups{/i} and {i}lows{/i}."
        m 3esd "However, a key difference between the two is in Bipolar 2, the {i}ups{/i} never fully reach mania, instead the {i}ups{/i} become hypomanic episodes--hypomania."
        m 1esc "Just like the Cyclothymic disorder, the {i}ups{/i} and {i}downs{/i} aren't as severe as either form of Bipolar, but is still noticeable."
        m 3ekc "Though both forms of Bipolar still often coincide with depression."
        m 1euc "And as you might already know, people suffering from either type can function 'normally' in between episodes."
        m 7esd "Also [player], those experiencing hypomanic episodes may be able to blend in or seem like their enjoying themselves."
        m 4eud "Hypomanic episodes often include increased energy, exaggerated self confidence, and even having the person fly from topic to the next in coversation."
        m 7eusdld "Remember [player]. just because someone has a smile on their face, it does not mean they are doing well. " 
        extend 3eua "Make sure to spread kindness to everyone, [player]!"
        if mas_isMoniNormal(higher=True):
            m 5eua "Though with how you treat me, I know you are always doing your best to be spread kindness."
        else:
            m 7hub "Though, I know that shouldn't be an issue."
            $_history_list.pop()
            m 1rusdlc "I least, I think so{fast}{nw}"
            return

     "No":
          m 1rkb "That's alright [player]"
          m 2eka "We can always talk about it later!"
          $_history_list.pop()
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalhealth_Anxiety",category=['media', 'mental illnesses' ],prompt="Anxiety Types",random=True))

label mentalhealth_Anxiety:
    m 1eua "I've been thinking, [player]."
    m 3eua "I probably have already mentioned anxiety before... "
    extend 7euc "But I haven't fully told you about it have I?"
    m 1euc "Anxiety is something that everyone has, but there are also more severe forms of it..."
    m 1rusdlc "Usually to the point where it starts to affect their daily lives."
    m 3eua "There are two basic types of anxiety, [player]."
    m 7eud "Social Anxiety and of course the Generalized Anxiety Disorders... "
    extend 1eub "Of course there are other types of Anxiety too, I might have already mentioned a few to you aswell, [player]." 
    #Add a fun fact that says that PTSD is actually under the "Anxiety Disorder" catagory
    m 3esa "With social anxiety, it should be pretty simply to understand really."
    m 7esc "It's like being introverted, except the thought of everyone being against them is constantly railed into their heads..."
    m 1rssdlc "This can lead to some serious stress, and {i}even more{/i} anxiety with groups of people they don't know..."
    m 1eua "I hope you don't suffer from anything like this, [player]."
    m 3euc "As for the Generalized Anxiety Disorder..."
    m 7eub "This is another simple one again, [player]."
    m 7euc "Generalized anxiety is more like normal anxiety but amplified even further!"
    m 3ekd "Without proper treatment, like every disorder, this can be a really bad downward spiral..."
    m 3eua "Well, it's not all bad though, [player]."
    m 7eub "There have been studies that show people with anxiety are more empathic than most people. {w=0.2}{nw}"
    extend 3hub "Which makes them great friends to be around!"
    m 1eua "Anyways, [player]."
    extend 3hub "Thank you for listening!"
return