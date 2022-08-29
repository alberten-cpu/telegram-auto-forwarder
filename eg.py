try:
    # receiver user_id and access_hash, use
    # my user_id and access_hash for reference
    receiver = '475479102'

    # sending message using telegram client
    client.send_message(receiver, message, parse_mode='html')
except Exception as e:

    # there may be many error coming in while like peer
    # error, wwrong access_hash, flood_error, etc
    print(e);