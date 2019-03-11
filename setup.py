import setuptools

setuptools.setup(
    name='RGISlackBot',
    version='0.0.1',
    packages=['venv.Lib.site-packages.idna', 'venv.Lib.site-packages.certifi', 'venv.Lib.site-packages.chardet',
              'venv.Lib.site-packages.chardet.cli', 'venv.Lib.site-packages.urllib3',
              'venv.Lib.site-packages.urllib3.util', 'venv.Lib.site-packages.urllib3.contrib',
              'venv.Lib.site-packages.urllib3.contrib._securetransport', 'venv.Lib.site-packages.urllib3.packages',
              'venv.Lib.site-packages.urllib3.packages.backports',
              'venv.Lib.site-packages.urllib3.packages.ssl_match_hostname', 'venv.Lib.site-packages.requests',
              'venv.Lib.site-packages.websocket', 'venv.Lib.site-packages.websocket.tests',
              'venv.Lib.site-packages.slackclient', 'rgislackbot', 'rgislackbot.tests'],
    url='https://github.com/raginggeek/RGISlackBot',
    license='MIT',
    author='Geoff Finch',
    author_email='gfinch1@gmail.com',
    description='A Slackbot Collaboratively Developed for the RGI Slack environment'
)
