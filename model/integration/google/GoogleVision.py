import argparse
import base64
import requests

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


def get_photo_description(imageUrl):
    """Run a label request on a single image"""

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)

    response = requests.get(imageUrl).content

    image_content = base64.b64encode(response)
    service_request = service.images().annotate(body={
        'requests': [{
            'image': {
                'content': image_content.decode('UTF-8')
            },
            'features': [{
                'type': 'LABEL_DETECTION',
            },
            {
                'type':'LOGO_DETECTION'
            }]
        }]
    })
    response = service_request.execute()

    labelResponses = []

    try:
        labelResponses = response['responses'][0]['labelAnnotations']
        
    except:
        pass
    
    label = ""

    try: 
        logoResponses = response['responses'][0]['logoAnnotations']
        for logo in logoResponses:
            label += logo['description'] + " "
    except:
        pass
    
    for oneR in labelResponses:
        label = label + oneR['description'] + " "
    
    return label.split()
