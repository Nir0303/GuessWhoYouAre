import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3


personality_insights = PersonalityInsightsV3(
    version="2017-02-11",
	username="3227bdc5-91ca-4235-9deb-093c8f76bb92",
    password="RKKa3Goc4M1x"
	
	)

with open(join(dirname(__file__), '../output/profile.txt')) as \
        personality_text:
    print(json.dumps(personality_insights.profile(
        text=personality_text.read()), indent=2))