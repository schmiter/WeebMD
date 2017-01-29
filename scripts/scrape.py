import json
import twitter
from watson_developer_cloud import ToneAnalyzerV3

twit = twitter.Api(consumer_key='MzWIqFLnQFGIGAMT4XM9cdJfL',
                  consumer_secret='zgCGNQRbEUmR53eIa8XZzJODDYEWhx8NAeRIpgvJyM8bnQySx4',
                  access_token_key='825504042734460930-vidX4bDGvjgQeHe4qdv4nUR8CwfjWID',
                  access_token_secret='Nmy8pis2VasXL6IrCrokZZkWR01JHdmjE2C6ZTdfn4l4V')

tone = ToneAnalyzerV3(username="8b10c4d0-0974-4b4b-961a-86bc393ff41a",
                      password="foHeuL8LVy1c",
                      version="2016-05-19")

def scrape_tag(tag, count=100):
    data = twit.GetSearch(term=tag, lang="en", count=count, result_type="recent")
    
    data = '\n'.join([d.text for d in data])
    data = data.replace('"', '') # remove double quotes
    data = data.replace("'", '') # remove single quotes/apostraphes
    data = data.replace('\\','') # remove backslashes
    data = data.encode('ascii', 'ignore')
    
    return data

def get_tone(tag, sample_size):
    data = tone.tone(text=scrape_tag(tag, count=sample_size))["document_tone"]
    emo = data["tone_categories"][0]["tones"]
    lan = data["tone_categories"][1]["tones"]
    soc = data["tone_categories"][2]["tones"]
    
    return {
        "emotion_tone": {
            "anger": emo[0]["score"],
            "disgust": emo[1]["score"],
            "fear": emo[2]["score"],
            "joy": emo[3]["score"],
            "sadness": emo[4]["score"]
        },
        "language_tone": {
            "analytical": lan[0]["score"],
            "confident": lan[1]["score"],
            "tentative": lan[2]["score"]
        },
        "social_tone": {
            "openness": soc[0]["score"],
            "conscientiousness": soc[1]["score"],
            "extraversion": soc[2]["score"],
            "agreeableness": soc[3]["score"],
            "emotional_rage": soc[4]["score"]
        }
    }

if __name__ == "__main__":
    print get_tone("#pomodoro", 100)

