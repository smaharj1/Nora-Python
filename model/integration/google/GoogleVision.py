import argparse
import base64

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


def get_photo_description(photo_file):
    """Run a label request on a single image"""

    # Need something for the photo file here

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
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
        labelResponses = response['responses'][0]['labelAnnotations']
        
        label = ""

        try: 
            logoResponses = response['responses'][0]['logoAnnotations']
            for logo in logoResponses:
                label += logo['description'] + " "
        except:

        for oneR in labelResponses:
            label = label + oneR['description'] + " "
            
        print('Found label: %s for %s' % (label, photo_file))

        return label

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    main(args.image_file)