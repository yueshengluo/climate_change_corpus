import json
import pandas as pd


def querydata(keyword,aspect,opinion):
    #import json hashmap for the index in excel related to keyword
    with open('static/keyword_hashmap_sentence_v2.json', 'r') as f:
        hashmap = json.load(f)
    df = pd.read_excel('static/integrated.xlsx').set_index('index')

    #check if keyword in hashmap
    if keyword in hashmap:
        index_list = hashmap[keyword]
    else:
        #when the keyword is not present, return warning message
        warning_str = 'keyword "'+keyword + '" not found'
        return {0:{'title':warning_str,'focus_sentence':'N/A','opinion':'N/A'}}
    #print(index_list)
    #filter data based on input keyword
    #filtered_df = df[df['id'].isin(index_list)]
    filtered_df = df.iloc[index_list]
    #filter data based on input aspect
    #if 'unannotated' selected for aspect
    if aspect=='unannotated':
        filtered_df = filtered_df[filtered_df['manual_annotation'].isna()]
        filtered_df['opinion'] = 'N/A'
        return filtered_df.to_dict('index')

    filtered_df = filtered_df[filtered_df[aspect].notnull()]

    #handle when none is selected for opinion, return all opinions for that aspect
    if opinion == 'none':
        filtered_df['opinion'] = df.loc[:, 'politics':'economy'].fillna(method='ffill', axis=1)['economy']
        output_df = filtered_df
    else:
        output_df = filtered_df[filtered_df[aspect] == opinion]
        output_df['opinion'] = output_df[aspect]

    return output_df.to_dict('index')
