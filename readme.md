# YT Playlist Updater

People love listening to music and most of them would be keeping a playlist to store tall their favourite tracks in a single place. While most people use music applications like Spotify, Gaana and Saavn, some people like me use Youtube since some old and regional tracks won't be available on the above mentioned applications. However, since these are old tracks, there is a high chance that some of them would face copyright strikedowns and will be deleted from Youtube. The problem is that when you open the playlist after a track is deleted, there's no way you can find out which track was deleted.

YT Playlist Updater is a simple Python script to periodically save your Youtube Playlists locally and notify you if any of the tracks are deleted by displaying the list of deleted tracks in an HTML page. The user can later manually add new videos of those tracks. 

:house_with_garden:
The script is implemented using the following technologies:

1. Python
2. Selenium
3. HTML
4. Windows Task Scheduler

To use the code, `git clone` the repository and inside the `code.json`, edit the `URL` variable to suit your needs.

The `URL` variable is in the format:

```
URL = {
        'M_URL' : "Language 1 Playlist link",
        'T_URL' : "Language 2 Playlist link",
        'E_URL' : "Language 3 Playlist link",
        'H_URL' : "Language 4 Playlist link"
    }
```

The video data is stored in JSON format:
```
{
    'Lang1' : {
        'tracks' : [
            {
            'name' : '...',
            'link' : '...'
        },
        {
            'name' : '...',
            'link' : '...'
        }
        ],
        'deleted' : [
            'Video1',
            'Video2'
        ]
    },
    'Lang2' : {
        'tracks' : [
            {
            'name' : '...',
            'link' : '...'
        },
        {
            'name' : '...',
            'link' : '...'
        }
        ],
        'deleted' : [
            'Video1',
            'Video2'
        ]
    }
} 
```
To schedule the script, do the following:
1. Open Windows Task Scheduler
2. Click Create Basic Task
3. Enter a name for the task and click Next
4. Click the option corresponding to the frequency of script execution
5. Enter the frequency details
6. Click Start a program
7. In the Program/Script field, enter the path to your Python executable
8. In the Add arguments files, enter 'code.json'
9. In the Start in folder, enter the path to the directory in which you have saved 'code.json'
10. Click Finish

Now the task is scheduled and will be executed in a timely manner. The list of deleted tracks if any, will be opened in a new browser tab.

---

# THANK YOU!




