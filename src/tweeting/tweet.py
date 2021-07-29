import argparse

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
    tweet_text_file = args.tweet_text
    if not (tweet_text_file or tweet_text):
        print('One of tweet_text or tweet_text_file is required!')
        return False

    twtr = Twitter(
        args.twtr_api_key,
        args.twtr_api_secret_key,
        args.twtr_access_token,
        args.twtr_access_token_secret,
    )
    if not twtr:
        return False

    twtr.tweet(tweet_text)


if __name__ == '__main__':
    _run()
