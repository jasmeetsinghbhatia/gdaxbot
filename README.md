# gdaxbot
A slack bot for getting cryptocurrency prices from GDAX exchange

## Pre requisite stuff

1. Register for a slack workspace (you need to be admin of that workspace) visit https://slack.com/create
<br>Once completed the registration move to step 2

2. Create a new slack app, visit https://api.slack.com/apps?new_app=1
<img width="1670" alt="screen shot 2018-01-20 at 3 51 30 pm" src="https://user-images.githubusercontent.com/5153163/35189275-e47238b0-fdfb-11e7-940e-444c82ad6f77.png">
<img width="551" alt="screen shot 2018-01-20 at 3 52 16 pm" src="https://user-images.githubusercontent.com/5153163/35189276-e68124e0-fdfb-11e7-8065-205551017ea3.png">

3. Configure your new app and bundle it with a bot user
<img width="1040" alt="screen shot 2018-01-20 at 4 06 33 pm" src="https://user-images.githubusercontent.com/5153163/35189287-39718802-fdfc-11e7-8d12-2fc7e6742cfc.png">

4. Copy your Bot user OAuth access token, you will need it to make your code talk to the bot after this setup
<img width="1030" alt="screen shot 2018-01-20 at 4 08 07 pm" src="https://user-images.githubusercontent.com/5153163/35189333-f7eb6b36-fdfc-11e7-8f61-0028a96b333f.png">

5. Define an environment variable for OAuth access token in a terminal on your local machine
  <br> **export SLACK_BOT_TOKEN='your bot user access token here'**

At this point, you should be authorized to use the Slack RTM and Web APIs as a bot user.

## Running the bot and using it inside the Slack client

1. Clone this repo locally 
2. From the root directory of this repo, install the slack client **pip install slackclient**
3. **source activate** (as usual)
4. **python gdaxbot.py**

At this point, your script will be able to establish a connection with RTM API
<img width="846" alt="screen shot 2018-01-20 at 5 55 54 pm" src="https://user-images.githubusercontent.com/5153163/35189973-6b573ce0-fe0b-11e7-83d4-1a25b9cfa9c3.png">

## Ready to ask @gdaxbot some questions ??

1. Get the slack client for your Mac/windows/linux or you can also access the web application at https://<your workspace>.slack.com
2. Invite the bot to a channel of your choice using command **/invite @gdaxbot** or directly access the bot under apps section 
3. Type something and see how the bot responds. <br> Soon you will discover the right commands to give to the @gdaxbot. 

<img width="1445" alt="screen shot 2018-01-20 at 6 00 39 pm" src="https://user-images.githubusercontent.com/5153163/35189999-2338f916-fe0c-11e7-947e-efdda2de187b.png">


## Next Steps
1. Add support for more features and not just getting latest price for currencies
2. Add user auth to access data within slack
3. Coinbase wallet access? Maybe.
