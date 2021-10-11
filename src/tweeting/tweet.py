import argparse
import os
import sys

from utils import filex
from utils.twitter import Twitter


def _stub():
    return True


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
    if not twtr:
        return sys.exit(-1)

    base_url = 'https://twitter.com/nuuuwan/status'
    for single_tweet_text in tweet_text.split('\n---'):
        if len(single_tweet_text) < 10:
            continue

        prev_id = None
        first_id = None
        for thread_paragraph_text in single_tweet_text.split('\n...'):
            if len(thread_paragraph_text.strip()) == 0:
                continue

            if not prev_id:
                prev_id = twtr.tweet(thread_paragraph_text).id
            else:
                prev_id = twtr.tweet(
                    thread_paragraph_text,
                    in_reply_to_status_id=prev_id,
                ).id

            if not first_id:
                first_id = prev_id
        if first_id:
            os.system('open -a safari %s/%d' % (base_url, first_id))


if __name__ == '__main__':
    _run()
