from func.MboxReader import MboxReader

mboxReader = MboxReader('data.mbox')
with mboxReader as mbox:
    for message in mbox:
        # print(message.as_string() + "\n\n\n")
        # print(message['from'])
        # print(message['subject'])
        print(message['X-Gmail-Labels'].split(',')[0] + "\n\n")
        # print(message)