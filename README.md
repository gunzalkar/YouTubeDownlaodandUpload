Instruction to Download from and Upload Video on YouTube Simultaneously. 

Creat a Youtube API service to start with it.

Steps to Create an YouTube API service :
1. Visit and Enable YouTube API https://console.cloud.google.com/marketplace/product/google/youtube.googleapis.com 
2. https://console.cloud.google.com/ 
3. Select API and Service from Navigation Menu.
4. Select OAuth concent Screen. 
5. Select Create APP , Select Extern Use. 
6. Fill out the Star Marked details and rest as default.
7. Select the Testers as the Email ID's you want to Upload the videos with.
8. Click on Credentials, Create Credentials OAuth Client ID
9. Select Application Type in most cases it is Desktop App or Web Appilaction.
10. Click on create, Downlaod the Credintials .json file and Rename it to googleAPI.json

Set Time to UTC +0 to instatnt upload the Video.

Paste the link of Video in downlaod.py to downlado and upload the video on and from YouTube.
Run python3 main.py
