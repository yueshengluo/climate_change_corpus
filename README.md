# Reddit CMV: Climate Change


<h2>Introduction</h2>

<p>
We created this website interface using FastAPI, Jinja2Templates and Bootstrap. The website includes a sidebar and a top navigation bar. In the sidebar, you can find information on the data source and our annotation methods. There is also a data visualization page on delta distribution study in the sidebar. The top navigation bar contains three main functions that lets you get access to information from our annotated corpus.
</p>

<h4>Search</h4>
<p>In the search page, you can input a keyword in a search box and click search, the interface will return the comments containing this keyword. It will also allow the user to select from a list of aspects (politics, humanity, science, economy), as well as a list of opinions (concerned, not concerned, neutral, conflicted, none). The interface can display the corresponding sentences given the specified aspect and opinion. The “none” selection in the opinions, allows you to search for all the comments from your selected aspect, despite the opinion of the comment. </p>

<h4>Visualization</h4>
<p>In the visualization page, similarly you can choose from the list of aspects and opinions. After selecting, the interface shows a pie graph for the distribution of delta comments among the corresponding sentences. There will also be two bar graphs, one for the number of sentences for each aspect and another one for the number of sentences for each opinion. In addition, there are two wordcloud graphs for the keyword in each aspect and opinion you selected.</p>

<h4>Pictures</h4>
<p>In an additional “pictures” page, you can see the pictures related to the keywords from our collected corpus. It allows you to refresh and see random new pictures from that keyword. This page provides direct information for the user to experience the beauty of our current living planet and the effect of human activities on global warming. </p>

## Python environment

3.9.6

## Requirements

```sh
requests==2.26.0
fastapi==0.70.0
uvicorn==0.15.0
python-dotenv==0.19.1
aiofiles==0.7.0
python-multipart==0.0.5
jinja2==3.0.2
Markdown==3.3.4
pytest==6.2.5
```
