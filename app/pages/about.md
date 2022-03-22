# Source of the corpus
We built this corpus by scraping Reddit. Specifically, we scraped the subreddit called "Change My View" (CMV; see [here](https://www.reddit.com/r/changemyview/)). CMV is a very popular community for online discussion dedicated to civil discourse. According to the organizers, this community is built around the idea that understanding comes first for resolving our differences. To that end, they promote productive conversations that are marked with respect and openness" (for more details, see [here](https://www.reddit.com/r/changemyview/wiki/index)).
Our motivation was to build a corpus that could be useful for argumentation mining. Even in English, argumentation mining is still a low-resourced domain (e.g., [Skeppstedt, et al., 2018](https://aclanthology.org/W18-5218/)). "What makes an argument persuasive?" "How do people justify their stance when succeeding in persuasion?" "Are there certain linguistic cues that make people feel respected and more open to other's opinion?" These are all important research questions that are yet to be answered to fill the gap between machine-generated text and human text. 
Possible applications will include a personal coaching bot with which corporate managers can simulate negotiation and brush up their communication skills, a counseling chatbot with which the patient can interact to develop social skills, and a ghost writer that can transform human text into more persuasive writing. 
CMV is a perfect choice for us because, not only it has a record history of constructive arguments, but also it has a special symbol, delta, to acknowledge the opinion that successfully changed someone's view. This approach has been employed in the literature, but the sizes of their corpora are very small (e.g., [Hidey, et al., 2017](https://aclanthology.org/W17-5102/)). This fact made our choice even more focused. Instead of just scraping all the text in CMV, we scraped multi-participant discourse that eventually led to 'Aha!', the moment that is signified by the symbol delta. 
For example, below is a thread from the topic "Roadside advertising should be illegal." Here, the participant Reddits_Worst_Night granted "delta" to the participant hucklebae, which was then confirmed by DeltaBot (Reddit's bot that checks the validity of deltas). The six light-gray lines to the left of the delta giver Reddits_Worst_Night signifies this thread contains six comments in total.

<p align="center">
<img src="https://raw.githubusercontent.com/yueshengluo/yueshengluo.github.io/master/delta_thread.png" alt="delta_thread" width="500"/ >
</p>

# Corpus Statistics
- Total number of documents: 2,235 submission posts and 2,513 delta threads
- Total number of words: 2,235,463 English words (997,477 words in the submissions + 1,237,986 words in the threads)
- For the purpose of the Web app, we extracted the threads related to climate change. Climate change is ranked among the hottest topics in Reddit, and we were able to extract 117 delta threads over 79 sub-topics (4,524 sentences; 98,164 words).
# Tf-Idf Results
## Top 10 trigrams
1. climate change denier
2. fight climate change
3. combat climate change
4. nuclear power plant
5. climate change denial
6. believe climate change
7. deny climate change
8. stop climate change
9. greenhouse gas emission
10. green house gas
## Top 10 bigrams
1. climate change
2. fossil fuel
3. global warming
4. change denier
5. carbon emission
6. renewable energy
7. electric car
8. greenhouse gas
9. nuclear energy
10. carbon tax
## Top 10 unigrams
1. climate
2. people
3. think
4. like
5. delta
6. point
7. thing
8. need
9. world
10. energy
## Some interesting keywords that are ranked below 10
'mass extinction', 'go extinct', 'existential threat', 'future generation', 'take action', 'human civilization'
## Other annotation ideas we discussed before finalizing our annotation plan
Below is a list of ideas we discussed other than the annotations we chose for this project.
- opinion-specific sentiment analysis: "blaming", "supporting", "neutral"
- opinion subjectivity: "expressive" (e.g. blathered) vs. "direct" (e.g. praised)
- argument structure: "claim", "premise", "agreement", "attack-rebuttal", "attack-undercutter"
- sarcasm
Coming up with the feasible annotation plan for the given timeline was a challenge. We learned that there are so many ways of annotating text. We also learned that the annotation scheme is about what kind of linguistic signals we want to amplify from the text. Depending on how we annotate it, the same set of text can emit different sets of signals, each having a different probability distribution. 