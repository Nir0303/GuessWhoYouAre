import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3
from bokeh.plotting import figure, show, output_file
import os
import pandas as pd

# from bokeh.charts import Bar, output_file, show

sTraits = []
percentile = []
d = {}


def traits():
    with open(join(dirname(__file__), '\output\profile.txt')) as personality_text:
        personality_insights = PersonalityInsightsV3(
            version="2017-02-11",
            username="1162a6bd-7a0f-4d90-81f7-c38e6419194e",
            password="jGRcPZd8xo0C"
        )
        s = json.dumps(personality_insights.profile(text=personality_text.read()), indent=2)
        socialAttributes = json.loads(s)
        for item in socialAttributes:
            if isinstance(socialAttributes[item], list):
                for i in socialAttributes[item]:
                    d = {}
                    try:
                        d[i['name']] = i['percentile']
                        sTraits.append(i['name'])
                        percentile.append(i['percentile'])
                    except:
                        pass

    d['sTraits'] = sTraits
    d['percentile'] = percentile
    df = pd.DataFrame(d)
    p = Bar(df, 'sTraits', values='percentile', title="Social Traits", plot_width=1200, plot_height=800)
    output_file('index/templates/index/traits.html')

