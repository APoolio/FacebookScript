import json
import os
from datetime import datetime
import plotly.graph_objects as go
from texttable import Texttable

# def findUserAds():
#     adsAssociated = '{}/ads/ads_interests.json'.format(FacebookData)
#     #print(adsAssociated)

#     with open(adsAssociated, 'r') as adsData:
#         ads_dict = json.load(adsData)

#     #print(ads_dict)

def findAdvertisersWithContact():
    contactReleased = '{}/ads/advertisers_who_uploaded_a_contact_list_with_your_information.json'.format(FacebookData)
    t = Texttable()
    i = 0

    t.add_row(['Advertisment Name', '#'])

    with open(contactReleased, 'r') as ads:
        contactReleasedDict = json.load(ads)

        for key, values in contactReleasedDict.items():
            for value in values:
                t.add_row([value, i+1])
                i = i + 1
        print('List of advertisers who have uploaded your contact data. \n')
        print(t.draw())
            

    

def appsAndWebsites():
    websiteArray = []
    dateArray = []
    apps_and_websites_associated = '{}/apps_and_websites/apps_and_websites.json'.format(FacebookData)

    with open(apps_and_websites_associated, 'r') as apps_and_webs:
        webAppsDict = json.load(apps_and_webs)

        for webApp in webAppsDict['installed_apps']:
            websiteArray.append(webApp['name'])
            dt_object = datetime.fromtimestamp(webApp['added_timestamp'])
            dateArray.append(dt_object)

    websiteArray = websiteArray[::-1]
    dateArray = dateArray[::-1]
    fig = go.Figure(data=go.Scatter(x=websiteArray, y=dateArray, mode='markers'))
    fig.update_layout(title='Apps and websites you have accessed through Facebook')
    fig.show()
            
    

#Finds donwloaded Facebook Data folder with all of the users info
def find_facebookData():
    for dirName in os.listdir():
        #print(dirName)
        if dirName == 'Facebook Data':
            return dirName
        
    print("No folder named 'Facebook Data' in workspace folder")

if __name__ == '__main__':
    FacebookData = find_facebookData()
    findAdvertisersWithContact()
    appsAndWebsites()
