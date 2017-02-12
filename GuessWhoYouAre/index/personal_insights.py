import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3
from bokeh.plotting import figure, show, output_file
import os
import pandas as pd
from bokeh.charts import Bar, output_file, show

sTraits = []
percentile = []
d={}
def traits():
    with open(join(dirname(__file__), '..\\output\\profile.txt')) as personality_text:
        personality_insights = PersonalityInsightsV3(
            version="2017-02-11",
            username="3227bdc5-91ca-4235-9deb-093c8f76bb92",
            password="RKKa3Goc4M1x"
            )
        s=json.dumps(personality_insights.profile(text=personality_text.read()), indent=2)
        socialAttributes=json.loads(s)
        for item in socialAttributes:
            my_dict = {}
            if isinstance(socialAttributes[item], list):
                for i in socialAttributes[item]:
                    d={}
                    try:
                        d[i['name']]=i['percentile']
                        sTraits.append(i['name'])
                        percentile.append(i['percentile'])
                    except:
                        pass
            else:
                pass

    d['sTraits']=sTraits
    d['percentile'] = percentile
    df=pd.DataFrame(d)
    p = Bar(df, 'sTraits', values='percentile', title="Social Traits", plot_width=1200, plot_height=800)
    output_file('index/templates/index/traits.html')





if __name__=='__main__':
    pass
