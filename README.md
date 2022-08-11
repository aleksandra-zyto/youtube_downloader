# youtube_downloader
YouTube video downloader.

Uses the TKinter module for the UI and the pytube module for interactions with YouTube.

It gives the user an option to insert a link and fetches data from YouTube about the resolution.
Unfortunately the resolutions list is limited by the "progressive" value being True. That ensures that downloaded file contains both audio and video.

The Submit and Sonwload button are deactivated after their functions are finished so the user is not able to download the same thing multiple times.
After the download is complete the user can choose whether they want to contionue using the app, in which case the functionality of the buttons is restored, and the entry field is cleared. 
They can also choose to close the app in which case the window closes. 
