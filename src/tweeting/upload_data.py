"""Uploaded data to nuuuwan/tweeting:data branch."""

import os


def upload_data():
    """Upload data."""
    os.system('echo "test data" > /tmp/tweeting.test.txt')
    os.system('echo "# tweeting" > /tmp/README.md')


if __name__ == '__main__':
    upload_data()
