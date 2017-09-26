# PesaBot-py

PesaBot Python API Wrapper (Beta) for [PesaBot](https://pesabot.com) official [API](https://pesabot.com/api/docs/)

## Get started

    pip install git+https://github.com/pesabot/pesabot-py.git#master
    
## Authenticate

We use basic auth, so make sure you grab your email and password i.e the one you used during registration.

## Example

    pb = PesaBot({'email': 'your_email', 'password': 'your_password'})

    # Get a list of bots created by you
    print pb.call('bot', method='GET')
    
    # Get a list of intent
    print pb.call('intents', method='GET')

    # Test a bot. Preview AI interpretation based on your training
    print pb.call('preview-bot', method='POST', payload={'text': 'hi'})