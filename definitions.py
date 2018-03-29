#!/usr/bin/env python2
# -*- coding:utf-8 -*-

u'''Tokenized definitions of idiomatic expressions from IDIX/VNC/SemEval/PIE Corpus'''

# Mapping of PIEs to definitions
definition_mapping = {
u"kick one's heels": u"have to wait a long time", 
u'make a pile': 'earn a lot of money',
u"blow one's own trumpet": u"boast about one's achievements",
u"pull someone's leg": u"play a joke on someone",
u"pull one's weight": u"contribute to a project",
u'take heart': u"receive courage",
u'hit the roof': u"become extremely angry",
u'make a face': u"show disgust or dislike",
u'get the nod': u"be selected or approved",
u"find one's feet": u"grow in confidence in a new situation with experience",
u'see stars': u"see flashes of light after being hit on the head",
u'hit the road': u"set out on a journey",
u"lose one's head": u"lose one's composure",
u'pull the plug': u"put an end to activities or plans",
u'take a back seat': u"occupy a less important role",
u'deliver the goods': u"come up to expectations",
u'through the roof': u"very angry",
u'ring the bell': u"revive a distant memory",
u'lay it on thick': u"exaggerate praise excuses or blame",
u"raise one's eyebrows": u"show surprise or offence",
u'pull the strings': u"have secret control",
u'strike a chord': u"stir emotion or memory",
u'catch death': u"get a cold",
u"burn one's fingers": u"suffer an unpleasant consequence",
u'below the belt': u"unfair and unkind",
u'give someone the sack': u"terminate someone's employment",
u'keep tabs': u"monitor someone's activities",
u'take root': u"begin to have effect",
u"tighten one's belt": u"spend less money",
u'bread and butter': u"livelihood",
u'lay waste': u"ravage",
u'cook with gas': u"make rapid progress",
u"lose one's cool": u"lose one's composure or nerve",
u"lose one's temper": u"have an outburst of anger",
u'run a mile': u"avoid at any cost",
u"do one's homework": u"be thoroughly prepared",
u'see a man': u"go to the toilet",
u'in the bag': u"achieved with certainty",
u'come in from the cold': u"be accepted after previous rejection",
u'etched in stone': u"permanently fixed or established",
u'give notice': u"inform one's employer of one's resignation",
u'kick the habit': u"overcome an addiction",
u'get the drift': u"understand the general meaning",
u'up to here': u"having more than one can tolerate",
u'hold the fort': u"take care of a place in someone's absence",
u'be my guest': u"give permission", # Not an idiom, IMO
u'anything goes': u"everything is permitted",
u'clear the air': u"alleviate tension or confusion",
u'go under': u"fail or go bankrupt",
u'hold the torch': u"feel unrequited love",
u'have the misfortune': u"experience an undesirable event",
u'in the fast lane': u"in a very highly pressured or risky manner",
u'touch a nerve': u"evoke a strong emotional reaction",
u"show one's teeth": u"indicate hostility",
u'a cut above': u"noticeably superior or better",
u"lick one's lips": u"show signs of excitement or eagerness",
u'carry the can': u"take blame or responsibility",
u'put food on the table': u"earn enough money",
u'run out of steam': u"lose momentum and fail",
u'rub it in': u"remind one of one's failures",
u'in the same boat': u"in the same situation",
u"lose one's shirt": u"lose a lot of money",
u'get bent out of shape': u"become upset or angry",
u'connect the dots': u"understand the relationship between different things",
u'cut it close': u"complete something near its time limit",
u'move the goalposts': u"change conditions or rules unfairly",
u'be left holding the baby': u"be made responsible for a problem",
u'take the chair': u"become chairman or chairwoman",
u'a piece of cake': u"a very easy task",
u'drop a bomb': u"announce shocking or startling news",
u'see the light': u"understand something clearly at last",
u'peach and cream': u"a very enjoyable experience",
u'make the cut': u"meet the necessary requirements",
u'bring to the table': u"provide a useful skill or attribute",
u'drop the ball': u"make a mistake",
u'under the microscope': u"under intense scrutiny",
u'small potatoes': u"an insignificant thing",
u'carry a lot of weight': u"wield importance or influence",
u'bring luck': u"provide good fortune", # Not an idiom, IMO
u'lower the bar': u"lower requirements or standards",
u'set fire': u"start a fire", # Not an idiom, IMO
u"recharge one's batteries": u"regain one's energy and strength",
u'on the same page': u"be in agreement or have the same understanding",
u"show one's hand": u"reveal one's plans or intentions",
u'blow smoke': u"intentionally mislead or confuse",
u'breath of fresh air': u"a new and imaginative approach",
u'all the rage': u"be very popular and fashionable",
u"catch someone's attention": u"capture someone's attention", # Not an idiom, IMO
u'lose heart': u"lose courage or confidence",
u'first port of call': u"first place where one stops to begin a process",
u'catch imagination': u"inspire someone", # Not an idiom, IMO
u'make a fortune': u"earn a lot of money", # Not an idiom, IMO
u'feel the pinch': u"be affected by financial hardship",
u'bend over backwards': u"exert a lot of effort",
u'at the end of the day': u"when everything is taken into consideration",
u'miss the bus': u"fail to take advantage of an opportunity",
u'kick the bucket': u"die",
u'a notch above': u"noticeably superior or better",
u'hold the baby': u"responsible for a problem",
u'along the line': u"during the course of a situation",
u'in the toilet': u"in a miserable condition",
u'take it to the bank': u"trust and rely on it",
u'play ball': u"cooperate",
u"change one's tune": u"change one's attitude or opinion",
u'across the board': u"applying to all individuals in a group",
u'have a future': u"have potential for success",  # Not an idiom, IMO
u'go south': u"deteriorate",
u'hold sway': u"have great influence",
u'break a leg': u"good luck",
u'face the music': u"receive or accept punishment",
u'make hay': u"take advantage of an opportunity",
u'behind bars': u"in jail",
u'go hand in hand': u"accompany something harmoniously",
u'a cut below': u"significantly inferior or worse",
u'and count': u"a continuously increasing number", # Not an idiom, IMO
u'have a fling': u"have a short sexual relationship",
u'hold your horse': u"wait a moment or restrain your enthusiasm",
u'deer in the headlights': u"in a state of paralysing surprise or fear",
u'up the ante': u"increase what is at stake",
u'touch wood': u"good luck", # Not an idiom, IMO
u'bite the dust': u"die or break down",
u'sell like hot cakes': u"sold quickly in great quantities",
u'nuts and bolts': u"basic workings or knowledge",
u'spend a penny': u"go to the toilet",
u'day in, day out': u"continuously over a long period of time",
u'ring a bell': u"revive a distant memory",
u'take the plunge': u"commit to a course of action",
u'horses for courses': u"different people are suited to different roles or situations", # Not an idiom, IMO
u'for the time being': u"for the present moment",
u'make tracks': u"leave a place in a hurry",
u'hands down': u"easily or unquestionably",
u'spin a yarn': u"tell a story",
u'few and far between': u"rare or infrequent",
u'move heaven and earth': u"make extraordinary efforts",
u'break the ice': u"eliminate social awkwardness or tension",
u'rub shoulders': u"spend time with someone in a social environment",
u'see red': u"be in a state of extreme anger",
u'have a ball': u"enjoy yourself enormously",
u'on board': u"as a member of a team",
u'speak volumes': u"reveal a lot of information",
u"take a leaf out of someone's book": u"behave like someone else",
u'hot air': u"empty talk or nonsense",
u'long in the tooth': u"old",
u'strike a chord': u"stir emotion or memory",
u'on ice': u"held in reserve for future consideration",
u'in the dock': u"under investigation or on trial in court",
u'on the game': u"engaged in prostitution",
u'rise from the ashes': u"be renewed and successful after defeat or destruction",
u"grease someone's palm": u"bribe someone",
u'pour oil on troubled waters': u"calm down a tense situation",
u'bear fruit': u"yield good results",
u'join the club': u"solidarity or sympathy", # Not an idiom, IMO
u'come a cropper': u"fail completely or fall heavily",
u'go hand in hand': u"accompany something harmoniously",
u'on the rocks': u"experiencing difficulty or destitution",
u'in your face': u"aggressively obvious and assertive",
u'out of pocket': u"lacking money",
u'pass muster': u"meet the required standard",
u'have a heart': u"treat with kindness and compassion",
u'come clean': u"admit",
u'out of the blue': u"very unexpectedly",
u"bite someone's head off": u"speak very angrily to someone",
u'go for broke': u"risk everything in an all-out effort",
u'down the drain': u"wasted or lost or getting worse",
u'play with fire': u"take unnecessary and dangerous risks",
u'save face': u"retain respect and avoid humiliation",
u'take it or leave it': u"there are no other choices", # Not an idiom, IMO
u"pull the wool over someone's eyes": u"deceive someone",
u'call it a day': u"quit work for the rest of the day",
u'step on it': u"hurry up",
u'rule the roost': u"be the boss",
u'spring to mind': u"suddenly remember something",
u"in the driver's seat": u"in charge of a situation",
u'wide of the mark': u"inaccurate or wrong",
u'from scratch': u"without the aid of previous work",
u'up in the air': u"subject to change",
u'think the world of': u"have a very high regard for",
u'on edge': u"anxious and tense",
u'go to seed': u"decline in looks or status or utility",
u'hold water': u"stand up to critical examination",
u'neck of the woods': u"a neighbourhood or region",
u'run amok': u"get out of control",
u'tie the knot': u"marry",
u'against the grain': u"contrary to customs or natural inclination",
u'lose the plot': u"act in a disorganized manner",
u'larger than life': u"having an aura of greatness or strong personality",
u'sick and tired': u"thoroughly bored or wearied",
u'see the light': u"understand something clearly at last",
u'come of age': u"reach adulthood or become fully established",
u'point the finger': u"apportion blame",
u'up to scratch': u"meeting the required standard",
u'in the offing': u"in the future",
u'in the black': u"turning a profit",
u'hit the jackpot': u"find something exactly right",
u'get the picture': u"understand a situation",
u'sour grapes': u"disparage something as if it were never desirable",
u'play for time': u"delay or stall",
u'rags to riches': u"characterized by a rise from poverty to wealth",
u'in a nutshell': u"in summary",
u'on the money': u"exactly right",
u'piping hot': u"extremely hot",
u'wet behind the ears': u"young and inexperienced",
u'eat someone alive': u"exploit someone's weakness ruthlessly",
u'over the hill': u"past one's best and declining",
u'bag and baggage': u"with all one's possessions",
u'turn the tables': u"turn a position of disadvantage into one of advantage",
u'pull strings': u"use influence or power",
u'let bygones be bygones': u"forgive and forget past offences",
u'off the beaten track': u"unusual or in a remote place",
u'hit home': u"have a strong effect on someone",
u'get off the ground': u"get started successfully",
u'dead and buried': u"finally and irrevocably in the past",
u'make waves': u"cause trouble",
u'sitting duck': u"easy target of attack",
u'watering hole': u"pub or tavern",
u'go overboard': u"act without restraint",
u'flat out': u"clearly and definitely",
u'kiss of death': u"cause of downfall",
u'on tenterhooks': u"in a state of anxious anticipation",
u'my eye': u"dismissal or disbelief or disdain", # Not an idiom, IMO
u'to all intents and purposes': u"in all important respects",
u"in someone's pocket": u"under someone's control",
u'in the running': u"in competition in a contest",
u'on the blink': u"malfunctioning or drunk",
u'below par': u"not as good as required or normal",
u'streets ahead': u"greatly superior",
u'economical with the truth': u"untruthful or deceitful",
u"bob's your uncle": u"very easy to achieve", # Not an idiom, IMO
u'around the clock': u"all day and all night or nonstop",
u'stay the course': u"persevere in something difficult to its end",
u'out of sorts': u"in a grumpy mood",
u'in the hole': u"in debt",
u'all hell broke loose': u"a chaotic situation broke out",
u'by the same token': u"in the same manner or for the same reason",
u'under fire': u"under criticism",
u'cross swords': u"fight or argue",
u'stand the test of time': u"be well regarded or function well after a long time",
u'drop the ball': u"make a mistake",
u'on the face of it': u"based on superficial evidence",
u'all along': u"the entire time",
u'small beer': u"an insignificant thing",
u'out of the woods': u"out of trouble or danger",
u'all and sundry': u"everyone",
u'make the grade': u"meet the required standard",
u'take the mickey': u"tease or ridicule",
u'on the same page': u"thinking in the same manner",
u'in spades': u"to an extreme degree",
u'up for grabs': u"available to anyone",
u'lose heart': u"lose confidence or courage",
u"i'll be a monkey's uncle": u"express great surprise", # Not an idiom, IMO
u'word of mouth': u"informal or unofficial talk",
u'into thin air': u"completely disappeared or invisible",
u'no go': u"impossible",
u'fall from grace': u"experience reduced status or prestige",
u'fly in the face of': u"act in clear opposition of",
u'keep mum': u"remain silent",
u'the plot thickens': u"the situation is becoming more complicated",
u"bend someone's ear": u"talk to someone with great eagerness",
u'at the end of the day': u"when everything is taken into consideration",
u'chew the fat': u"chat or gossip",
u'do the trick': u"bring about the desired result",
u'open the floodgates': u"allow a great many things to happen or people to do something",
u'toe the line': u"adhere to rules or authority",
u'buy the farm': u"die",
u'steal the show': u"become the focus of attention",
u'on the skids': u"in decline",
u'behind closed doors': u"in secret",
u'by and large': u"in general",
u'turn a blind eye': u"knowingly ignore wrongdoing",
u'under a cloud': u"under suspicion",
u'hang by a thread': u"be perilously close to failing or dying",
u'on the shelf': u"not involved in work or social life or postponed",
u'go the distance': u"persevere in something difficult to its end",
u"child's play": u"a very easy task",
u'down and out': u"destitute and devoid of any resources",
u'stake a claim': u"assert one's ownership",
u'on the ropes': u"on the verge of defeat",
u'all over the place': u"everywhere or scattered",
u'slippery slope': u"a course that leads to catastrophe",
u'sink or swim': u"fail or succeed",
u'at sea': u"confused or perplexed",
u'neither here nor there': u"irrelevant and unimportant",
u'get a grip': u"recover your self-control",
u'on the cards': u"very likely to happen",
u'all bets are off': u"the outcome of the situation is unpredictable",
u'in the long run': u"over a long period of time",
u'jump ship': u"to leave a post or task",
u'go to the wall': u"go bankrupt or hold out to the end or lose a conflict",
u"big girl's blouse": u"a weak or oversensitive man",
u'on the trot': u"in quick succession",
u'left and right': u"from multiple sources with great frequency",
u'slip of the tongue': u"a speech error",
u'rule of thumb': u"general guideline or principle",
u'at the drop of a hat': u"immediately with little provocation",
u'in the pink': u"in very good health",
u'go through the motions': u"do something perfunctorily or without interest",
u'on the ball': u"knowledgeable and attentive",
u'in light of': u"considering",
u'on the level': u"dependably honest",
u'behind bars': u"in jail",
u'sweep the board': u"win all possible prizes",
u'muddy the waters': u"confuse the issue or situation",
u'on the take': u"taking bribes",
u'on the same wavelength': u"be in agreement or have the same understanding",
u'on the wagon': u"not drinking alcohol",
u'box clever': u"act to outwit someone",
u'walk the plank': u"be forced to leave your job or position",
u'a bit much': u"unnecessarily excessive",
u'cut a figure': u"convey a particular image",
u'laughing stock': u"subject of mockery or ridicule",
u"behind someone's back": u"without someone's knowledge",
u'warts and all': u"including all faults and shortcomings",
u'over the top': u"surpassing a goal or outrageous",
u'down at heel': u"with a poor appearance",
u'get away with murder': u"do something wrong without punishment",
u"make one's mark": u"achieve distinction",
u'come out in the wash': u"have a positive resolution",
u'fair game': u"a legitimate target for criticism or attack",
u'green light': u"permission to go ahead with a project",
u'old hat': u"old-fashioned or unoriginal",
u'in cold blood': u"without feeling",
u"blow one's top": u"quickly become very angry",
u'have a go': u"make an attempt",
u'gain ground': u"make progress",
u'hit the wall': u"encounter an insurmountable problem",
u'scream blue murder': u"shout loudly or make a complaint",
u'on the ground': u"where the actual work is done",
u'pull the trigger': u"make a final decision",
u'against the clock': u"with a shortage of time",
u"mum's the word": u"pledge to keep a secret",
u'get the sack': u"be fired from a job or task",
u'fire the first shot': u"be the first to take action",
u'high and mighty': u"self-important and arrogant",
u'have a word': u"have a conversation",
u'pass the buck': u"shift blame or responsibility",
u'make a scene': u"create a public disturbance or display",
u'by heart': u"completely from memory",
u'under the table': u"in secret or intoxicated",
u'out of the box': u"ready to use or unconventional",
u'odds and ends': u"small miscellaneous items",
u'get wind': u"gain knowledge of",
u'in the clear': u"judged innocent",
u'stop the show': u"give an impressive performance provoking laughter or applause",
u'all over the map': u"unorganised or in great variety or scattered over a great distance",
u'run the gauntlet': u"endure a series of problems or threats",
u'jump on the bandwagon': u"join or follow others in supporting a success or trend",
u'come to a head': u"reach a critical stage",
u'hair of the dog': u"an alcoholic drink to remedy a hangover",
u'on a roll': u"in the midst of a streak of successes",
u'pull your punches': u"restrain your commentary or criticism to prevent offence",
u'get cold feet': u"experience nervousness or anxiety",
u'spill the beans': u"disclose a secret",
u'throw in the towel': u"abandon a struggle or admit defeat",
u'bite the bullet': u"accept something difficult or unpleasant",
u'drop off the radar': u"fall into obscurity",
u'take out the trash': u"forcefully remove undesirable people from a place", # Not an idiom, IMO
u'pick up the tab': u"pay the bill",
u'in the red': u"in debt or losing money",
u'carved in stone': u"permanently fixed or established",
u'first come, first served': u"first people to arrive get the best choices", # Not an idiom, IMO
u'under the weather': u"ill or drunk",
u'put two and two together': u"infer something from the available evidence",
u'round the bend': u"crazy or having lost sanity or intoxicated from alcohol or drugs",
u"bite one's tongue": u"refrain from speaking out",
u'fit the bill': u"be suitable for a particular purpose",
u'fall by the wayside': u"fail to persist in an endeavour or be left without attention or help",
u'hard cheese': u"ironic sympathy over a small matter", # Not an idiom, IMO
u"hate someone's guts": u"feel a strong hatred for someone", 
u"tear one's hair out": u"show extreme anxiety or desperation",
u'out and about': u"engaging in normal activity after an illness",
u'bury the hatchet': u"make peace",
u'go dutch': u"share the cost or a bill equally",
u'bits and bobs': u"sundry little items or tasks",
u'sweep under the carpet': u"hide or ignore a failure or embarrassment",
u'rough and ready': u"rough or unrefined but useful and effective",
u'pay dividends': u"produce good results",
u'reach the top': u"achieve a high position", # Not an idiom, IMO
u'have kittens': u"show extreme surprise or anxiety",
u'make ends meet': u"earn enough money to pay bills",
u'as a rule': u"in general or usually",
u'coals to newcastle': u"bringing something to a place where there is plenty of it",
u'cut corners': u"save money or effort by ignoring rules or requirements",
u'out of this world': u"extraordinary or impressive",
u'blow the whistle': u"report wrongdoing",
u'rock the boat': u"disturb a situation",
u'make a killing': u"make a large profit",
u'give and take': u"compromise",
u'bite off more than one can chew': u"take on too much responsibility or tasks",
u"get one's feet wet": u"start into new territory",
u'in full swing': u"at the peak of activity",
u'over the moon': u"extremely happy",
u'back the wrong horse': u"support a person or effort which fails",
u'par for the course': u"matching with expectations",
u'send someone packing': u"rudely or abruptly dismiss someone",
u'throw down the gauntlet': u"declare or issue a challenge",
u'bounce off the wall': u"be full of activity or nervous excitement",
u'blow a gasket': u"lose one's self-control and become very angry",
u'on the nose': u"precisely accurate or lacking subtlety",
u'light at the end of the tunnel': u"the possibility of success or the end of difficulty",
u'go west': u"die or stop working",
u'place in the sun': u"a position of favour or advantage",
u'lose the thread': u"stop understanding an explanation",
u'head south': u"fall in value or make an escape or stop working",
u'break even': u"making neither a profit nor a loss",
u'kill the fatted calf': u"prepare an elaborate banquet as a welcome back",
u'know the score': u"understand the essentials of a situation",
u'cut a dash': u"have a stylish or impressive appearance",
u'make a hit': u"achieve great success or make a great impression",
u'out to lunch': u"uninformed or out of touch with the real world",
u'for a song': u"for a very low price",
u'scratch the surface': u"to investigate or understand something only in a superficial manner",
u'play it by ear': u"improvise depending on the circumstances",
u'set in stone': u"permanently fixed or established",
u'on the run': u"running away as a fugitive",
u'above board': u"honest and open",
u'by the book': u"according to the rules or regulations",
u'from the word go': u"from the very beginning",
u'go to town': u"act without restrained or with great energy",
u'fast and furious': u"swift and uncontrolled",
u'off the hook': u"freed from obligation or trouble",
u'blow a fuse': u"lose one's self-control and become very angry",
u'tempt fate': u"take a risk or invite bad luck",
u'blood in the water': u"detect a competitive weakness in an opponent",
u'turn the other cheek': u"to ignore abuse or insult",
u'hold your fire': u"delay or stop an attack",
u'tilt at windmills': u"attack imaginary enemies or evils",
u'nothing to write home about': u"mediocre or ordinary",
u'back to the wall': u"in a difficult situation with no escape",
u'swim against the tide': u"go against prevailing opinion or customs",
u'champ at the bit': u"be eager and impatient to take action",
u'turn the corner': u"pass a critical point towards improvement"}