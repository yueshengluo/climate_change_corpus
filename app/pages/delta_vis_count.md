# Overview of discourse factors leading to persuasion

To investigate into the context surrounding the 'Aha!' moment, we looked into the comments that are directly linked to that moment. Specifically, we extracted sentences from the comments that received a delta sign (a hallmark of 'Change My View', meaning that the comment changed someone's view) and also from the comments that gave a delta sign. (In CMV subreddit, anyone can give a delta to someone else's comment to acknowledge that comment successfully changed their view.) 

## Sentences by the commentators who were successful in persuasing someone else
<p align="center">
<img src="https://raw.githubusercontent.com/yueshengluo/yueshengluo.github.io/master/received_delta_aspect.png" alt="delta_thread" width="500"/ >
</p>
<p align="center">
<img src="https://raw.githubusercontent.com/yueshengluo/yueshengluo.github.io/master/received_delta_opinion.png" alt="delta_thread" width="500"/ >
</p>


Observations: In absolute terms, "humanity" and "science" aspects were touched upon the most when a person is successful in changing someone else's view. "concerned" was by far the most dominant opinion polarity.

Examples of an "concerned" opinion for "humanity" aspect: 
- "It is a rhetorical point and an extreme representation but I do think if the worst of climate change goes unaddressed then we are facing a severe crisis that threatens humanity."
- "They say they do, but they don't care enough to actually change their own spending habits."


## Sentences by the commentators who were persuaded
<p align="center">
<img src="https://raw.githubusercontent.com/yueshengluo/yueshengluo.github.io/master/gave_delta_aspect.png" alt="delta_thread" width="500"/ >
</p>
<p align="center">
<img src="https://raw.githubusercontent.com/yueshengluo/yueshengluo.github.io/master/gave_delta_opinion.png" alt="delta_thread" width="500"/ >
</p>


Observations: In line with the delta receiver's side (those who were successful in persuading), the most touched-upon subtopics were "humanity" and "science" with "concerned" opinion.

Examples of a "concerned" opinion for "humanity" aspect:
- "delta I realized that, to some degree, I have been conflating the the apocalyptic consequences with hitting the threshold under which feedback loops will make climate change much more difficult to fight."
- "Most people are not involved in energy innovation and research, which means they're producing carbon emissions without contributing to the betterment of these technologies."


## Conclusion
- Within our sample, people found a common ground for mutual understanding the most in  humanity and science domains.
- People are more likely to change their opinions when they are concerned about something.
- People are more likely to be changed their perspective when they are concerned about something.

Although constrained with the extremely limited size of annotated corpus (opinion polarity for 4 aspects and 2 binary flags for delta receiver and delta giver for 516 sentences = 3,096 annotations), we were able to find a few interesting patterns. These results show a promise of Reddit CMV as argumentation mining corpus. CMV is a serious discussion platform for controvertial issues, and people tend to use harsh languages or sarcasm. However, within the delta threads, we rarely saw sarcasm or harsh languages. Especially the sentences by successful persuaders were often nuanced, instead of judgemental. Their sentences tend to contain multiple aspects with different opinion polarity, as if trying to expand the listener's horizon. 

For future studies, this corpus has a potential of contributing to argumentation mining by:
- annotating the rest of this corpus with the same tag set we used
- annotating the rest of this corpus with a different tag set we used
- collecting the threads that did not reach mutual understanding (a.k.a. delta), and compare the results with those reached delta (we might see more sarcasm in non-delta threads?)
