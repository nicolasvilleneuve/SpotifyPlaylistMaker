# SpotifyPlaylistMaker
By filling in the proper credentials for main.py, you will be able to generate fun playlists comprised of the top 100 billboard songs for the date that you chose to specify. 

## Description
All you need to do is fill in your info for the environmental variables and, so long as you have access to the Spotify API, you can then generate a playlist on spotify, with the billboard top 100 songs for the date you chose to specify. 

In order to make the program work for you, you simply need to change the lines of code that deal with authenticating the user in the main.py file. Such is exemplified by Figure 1, below. 

<img src="https://github.com/nicolasvilleneuve/SpotifyPlaylistMaker/blob/main/figures/Figure1.png" alt="Figure1"> 
Figure 1. The lines of code which need be switched out with the user's authentication credentials. 

## Usage
You can freely access and utilize this program so long as you have a version of python 3 (this was made in python 3.9.1), the proper credentials to access the spotify API, BeautifulSoup (bs4), the json module, and the datetime module. While as I am aware I could simply export all of my credentials to the environment and pull those to make this program work directly with this code, that would compromise all of my credentials.


## Contributing/Support
If you would like to create a PULL request, please feel free. Whether the intent be to pilfer from the code as you like some elements of the app, or to suggest improvements, you are most welcome to. If the changes are to be major, however, please open an issue first so we can discuss if/what you would like to change. Should you have a problem in doing so, please feel free to let me know (my email is on my website so please find it there in case it has changed since writing this).


## License

MIT License

Copyright (c) 2021 Nicolas Villeneuve

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
