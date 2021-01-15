from tweetbot import TweetBot
from speedbot import SpeedBot

PROMISED_DOWN = 100.0
PROMISED_UP = 100.0
ACCEPTABLE_MARGIN = 0.9


def main():
    sb = SpeedBot()
    speed = sb.get_speed(45)
    tb = TweetBot()
    if speed['up'] > PROMISED_UP*ACCEPTABLE_MARGIN and speed['down'] > PROMISED_DOWN*ACCEPTABLE_MARGIN:
        message = "You guys are doing great with my internet speed"
    elif speed['up'] > PROMISED_UP*ACCEPTABLE_MARGIN:
        message = f"You could do better, my upload speed is fine but I only get {speed['down']} down"
    elif speed['down'] > PROMISED_DOWN*ACCEPTABLE_MARGIN:
        message = f"You could do better, my download speed is fine but I only get {speed['up']} up"
    else:
        message = f"You guys suck, my download speed is only {speed['down']} and my upload speed only {speed['up']}"

    tb.send_tweet(message)


if __name__ == '__main__':
    main()
