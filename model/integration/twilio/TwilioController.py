import twilio.twiml


class TwilioController:

    @staticmethod
    def getMessage(req):
        from_number = req.values.get('From')
        messageURL = req.values.get('MediaUrl0')
        return (from_number,messageURL)

   