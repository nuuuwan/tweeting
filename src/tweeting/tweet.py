import argparse
import sys

from utils import filex
from utils.twitter import Twitter


def _stub():
    return True


def split_text(text):
    MAX_SPLIT_CHARS = 240
    sentences = text.split('.')
    split_text_list = ['']
    for sentence in sentences:
        if len(split_text_list[-1]) + len(sentence) > MAX_SPLIT_CHARS + 2:
            split_text_list.append('')
        split_text_list[-1] += sentence + '.'

    return split_text_list


def _run():
    parser = argparse.ArgumentParser(description='Tweeting Tools')
    for twtr_arg_name in [
        'twtr_api_key',
        'twtr_api_secret_key',
        'twtr_access_token',
        'twtr_access_token_secret',
        'tweet_text',
        'tweet_text_file',
    ]:
        parser.add_argument(
            '--' + twtr_arg_name,
            type=str,
            required=False,
            default=None,
        )
    args = parser.parse_args()

    tweet_text = args.tweet_text
    tweet_text_file = args.tweet_text_file
    if not (tweet_text_file or tweet_text):
        print('One of tweet_text or tweet_text_file is required!')
        return sys.exit(-1)

    if not tweet_text:
        tweet_text = filex.read(tweet_text_file)

    twtr = Twitter(
        args.twtr_api_key,
        args.twtr_api_secret_key,
        args.twtr_access_token,
        args.twtr_access_token_secret,
    )
    prev_id = None
    for tweet_text_single in split_text(tweet_text):
        if not prev_id:
            prev_id = twtr.tweet(tweet_text_single).id
        else:
            prev_id = twtr.tweet(
                tweet_text_single, in_reply_to_status_id=prev_id
            ).id


if __name__ == '__main__':
    _run()
