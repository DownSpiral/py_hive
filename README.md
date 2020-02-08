## Py Hive
#### Porting the original [Hive](https://github.com/Brentwish/hive/tree/master/hive) to python.

##### Pygame
https://www.pygame.org/wiki/MacCompile
`pip install git+https://github.com/pygame/pygame.git`

https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
https://talkpython.fm/episodes/show/168/10-python-security-holes-and-how-to-plug-them


##### Windows 10

When using WSL, Pygame will error on trying to find a video driver. To support this you must install an X11 forwarding
application on Windows, and run it along side the terminal.

MobaXterm is free and seems to do the trick. Install and run this application:

https://mobaxterm.mobatek.net/download-home-edition.html

and then in your terminal paste the following:

export DISPLAY=:0
export LIBGL_ALWAYS_INDIRECT=1
