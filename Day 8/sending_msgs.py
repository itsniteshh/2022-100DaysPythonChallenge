text_msgs = ["bonjour","bonsair", "comment ca va"]
sent_msgs = []

def send_msgs(text_msgs, sent_msgs):
    while text_msgs:
        current_msg = text_msgs.pop()
        print(f"sending {current_msg} right now")
        sent_msgs.append(current_msg)

def sending_msg(sent_msgs):
    print(f"\nThe following messages have been sent: ")
    for msgs in sent_msgs:
        print(msgs)

send_msgs(text_msgs, sent_msgs)
sending_msg(sent_msgs)
