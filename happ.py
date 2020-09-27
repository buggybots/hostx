# Imports:
# import dill
import pandas as pd
# import plotly.express as px
import numpy as np
# import re
import streamlit as st
# st.write("Airbnb | Hosts")
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# ------------------------------------------------------------------------


st.image('./logo_title_white_2-1.PNG')
# st.image('qr-code.svg')

@st.cache(allow_output_mutation=True)
def get_data():
    # url = "http://data.insideairbnb.com/australia/vic/melbourne/2020-05-13/visualisations/listings.csv"
    return pd.read_csv("./model1_nc.csv")
df = get_data()

# st.title("Host+")
st.header("_because you only get one chance to make_")
st.header("_your first impression!_")

# png = 'qr-code.svg'
# url = "https://images.unsplash.com/photo-1495386786209-f284d613b8d0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"

# <a href="https://images.unsplash.com/photo-1464820453369-31d2c0b651af?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2000&q=80"><img onmouseover="bigImg(this)" onmouseout="normalImg(this)" src="https://images.unsplash.com/photo-1464820453369-31d2c0b651af?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2000&q=80" style="position:fixed; right:10px; top:20px; width:250px; height:250px; border:none; cursor:pointer; background:none;"></a>

leaf = "https://images.unsplash.com/photo-1566998299570-fe19ada82788?ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80"
rainbow_flower = "https://images.unsplash.com/photo-1495386786209-f284d613b8d0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"

st.markdown(
    """
<a href="https://images.unsplash.com/photo-1566998299570-fe19ada82788?ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80"><img onmouseover="bigImg(this)" onmouseout="normalImg(this)" src="https://images.unsplash.com/photo-1566998299570-fe19ada82788?ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80" style="position:fixed; right:10px; top:5px; width:480px; height:720px; border:none; cursor:pointer; background:none;"></a>


<script>
    function bigImg(x) {
    x.style.height = "80px";
    x.style.width = "80px";
    x.style.opacity = "0.1";
}

    function normalImg(x) {
    x.style.height = "80px";
    x.style.width = "80px";
    x.style.opacity = "10";
    }
</script>
""",
    unsafe_allow_html=True,
)


st.title(" ")


st.subheader('Are you `new host` on Airbnb or')
st.subheader('a `seasoned host` who wants to have more guests?')

st.title(" ")



st.write('''Our tool will recommend how guests will perceive your listing. 
Based on your description, this tool will give you a score and 
word recommendations to make your listing  _stand out_!''')


st.title(" ")

st.write("Let's first find out a little about your place.")
# st.header("Customary quote")
# st.markdown("> I just love to go home, no matter where I am [...]")
# st.map(df)
# st.dataframe(df.head())



neighbourhood = st.radio("Where would you like to host?", sorted(df.neighbourhood_cleansed.unique()))

accommodates = st.selectbox("How many guests would you like to host?", sorted(df.accommodates.unique()))

beds = st.selectbox("How many bedrooms do you have?", [int(x) for x in sorted(df.beds.unique())])

square_feet = st.selectbox("How big is your place (in square metres)?", [int(x) for x in sorted(df.square_feet.unique())])



st.title(" ")
    
# st.image("https://images.unsplash.com/photo-1464820453369-31d2c0b651af?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2000&q=80")

st.write('### How would you describe your place to a guest?')
# sentence = st.text_input(prompt)


# loading pickle file
# from joblib import dump, load
# # # dump(pipe, 'model_3_1_3.joblib')          # can create a new file and save it in that file
# my_model = load('model_31311.joblib') 

sentence = st.text_input(' ')
# sentence.split('')
# element = np.array([sentence, sentence])

# element = np.array([sentence, sentence[::-1]])
# st.write(type(sentence), sentence)
# st.write(element.shape, element)


# dill._dill._reverse_typemap['ClassType'] = type #Takes care of "KeyError" issue of dill while unpickling

# with open('model_31311.pkl', 'rb') as f:
#     pipe = dill.load(f)

# st.write(type(pipe))

# if sentence:
#     st.write(pipe.predict([[sentence]]))


    # st.write(my_model.predict_proba(element))

# source: https://discuss.streamlit.io/t/how-to-add-a-text-box/717/2

# st.write('Thanks for your patience, we are in the process of **Host+ ing** your listing! 🙂')

top_words = list(set(["happy", "help", "live", "work", "home", "years", "love", "living,", "years", "ago", "melbourne", "smallest", "bars", "restaurants", "little", "george", "right", "city", "fitzroy", "freedom", "fitzroy", "think", "moved", "melbourne", "melbourne", "smallest", "urban", "city", "fitzroy", "bars", "music", "restaurants", "live", "public", "transport", "going", "soon", "reasons", "feel", "free", "thompson", "house", "historic", "preservation", "modern", "music", "street", "art", "cross", "station", "hi", "originally", "enjoying", "melbourne", "bars", "pubs", "restaurants", "cocktail", "bars", "home", "hundreds", "people", "boring", "relaxed", "world", "things", "live", "shared", "home", "hundreds", "old", "new", "home", "sounds", "bedside", "tables", "diversity", "kerstin", "thompson", "plugs", "bedside", "hear", "know", "brings", "melbourne", "rare", "areas", "fitzroy", "think", "home", "sounds", "guest", "room", "melbourne", "city", "home", "years", "thompson", "house", "home", "preservation", "modern", "architecture", "working", "class", "gentrification", "pad", "love", "hear", "usually", "enjoying", "preservation", "modern", "right", "city", "architecture", "right", "think", "going", "soon", "working", "class", "bedroom", "apartment", "george", "light", "filled", "ear", "plugs", "fully", "furnished", "gardens", "boring", "relaxed", "hope", "ll", "enjoy", "living", "hope", "ll", "kind", "pad", "love", "little", "george", "light", "know", "brings", "pubs", "chosen", "house", "best", "fitzroy", "friends", "freedom", "filled", "comfy", "welcome", "little", "new", "working", "class", "light", "filled", "level", "welcome", "little", "george", "love", "hear", "people", "arrive", "noisy", "ear", "live", "friends", "freedom", "art", "good", "hundreds", "people", "world", "modern", "architecture", "right", "area", "stay", "award", "fitzroy", "cafes", "boring", "relaxed", "odd", "great", "house", "walk", "away", "things", "vintage", "look", "forward", "hear", "know", "come", "stay", "best", "fitzroy", "kind", "pad", "nice", "melbourne", "smallest", "filled", "level", "carlton", "gardens", "parks", "restaurants", "city", "think", "going", "george", "light", "venues", "cocktail", "like", "kind", "short", "stay", "area", "stay", "class", "gentrification", "historic", "architecture", "right", "city", "happy help", "wouldn live", "work home", "years love living", "years ago", "melbourne smallest", "bars restaurants", "little george", "right city fitzroy", "freedom fitzroy think", "moved melbourne", "melbourne smallest urban", "city fitzroy", "bars music", "restaurants live", "public transport", "going soon reasons", "feel free", "thompson house", "historic preservation modern", "music street art", "cross station", "hi originally", "enjoying melbourne", "bars pubs", "restaurants cocktail bars", "home hundreds people", "boring relaxed", "world things live", "shared home hundreds", "old new", "home sounds", "bedside tables diversity", "kerstin thompson", "plugs bedside", "hear know brings", "melbourne rare", "areas fitzroy", "think home sounds", "guest room", "melbourne city", "home years", "thompson house home", "preservation modern architecture", "working class gentrification", "pad love hear", "usually enjoying", "preservation modern", "right city", "architecture right", "think going soon", "working class", "bedroom apartment", "george light filled", "ear plugs", "fully furnished", "gardens boring relaxed", "hope ll enjoy", "living hope ll", "kind pad love", "little george light", "know brings", "pubs chosen", "house best fitzroy", "friends freedom", "filled comfy", "welcome little", "new working class", "light filled level", "welcome little george", "love hear", "people arrive", "noisy ear", "live friends freedom", "art good", "hundreds people world", "modern architecture right", "area stay award", "fitzroy cafes", "boring relaxed odd", "great house", "walk away", "things vintage", "look forward", "hear know", "come stay", "best fitzroy", "kind pad", "nice melbourne smallest", "filled level", "carlton gardens", "parks restaurants", "city think going", "george light", "venues cocktail", "like kind", "short stay", "area stay", "class gentrification historic", "architecture right city"]))

# top_words = ["happy", "help", "wouldn", "live", "work"]


n = 0
wordlist = []
suggestions = top_words.copy()

for word in top_words:
    if word in sentence:
        n+=1
        wordlist.append(word)
        suggestions.remove(word)

if n==1:
    st.write(f'Your description has a top word!')

elif n>0:
    st.write(f'Your description uses `*`**top words**, {n} times!') 
    st.write(f'You have used these **top words**')
    st.write(', '.join(set(wordlist)))
    st.write('###### `*` **Top words** have been collected from over 7,000 host descriptions.')

st.title(" ")

st.subheader('Based on our analysis of over half a million guest reviews, we can suggest words that will boost your listing!')

agree = st.checkbox('Would you like our suggestions?')

if agree:
    st.write('Here are words and phrases that will make your listing stand out!')
    st.selectbox("", suggestions)

    
st.title(" ")
st.title(" ")
st.write('### Watch this space, we constantly _evolve_ to **Host+** your listing! 🙂')


