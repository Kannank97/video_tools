<img src="./logo/easy_editor_logo.png" height=100 width=100>

# Easy Editor

Easy Editor is a python based tool for video editing.

## Using the easy editor

### Commands

| Commands | Description |
| ---- | ---- |
| [`version`](#version) | View version details |
| [`help`](#help) | To view command informations |
| [`play`](#play) | Play any video files | 


## **`version`**
Get the version information of the **easy editor**.

```
usage: easy_edit.py --version [-v]
```

Example:

```
$ python3 easy_edit.py --version
```
```

                                     ___ __
  ___  ____ ________  __   ___  ____/ (_) /_____  _____
 / _ \/ __ `/ ___/ / / /  / _ \/ __  / / __/ __ \/ ___/
/  __/ /_/ (__  ) /_/ /  /  __/ /_/ / / /_/ /_/ / /
\___/\__,_/____/\__, /   \___/\__,_/_/\__/\____/_/
               /____/                               
                                                


Version 0.1.0

```

## **`help`**
To view the details of all the commands available on **easy editor**

```
Usage: easy_editor.py --help [-h]
```

Example:

```
python3 easy_editor.py --help
```
```
Usage: easy_edit.py [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version  Version details
  --help         Show this message and exit.

Commands:
  play  Play your videos with easy editor
```
## **`play`**

To play any video using `easy editor`, use the command `play`

```
Usage: easy_edit.py play [OPTIONS] INPUT_FILE

  Play your videos with easy editor

Options:
  -i, --input  Pass your input video file to play  [required]
  --help       Show this message and exit.
```

Example;
```
$ python3 easy_editor.py play -i my_video.mp4
```

If you want to create cool text banners like this, refer this [page](https://www.tecmint.com/create-ascii-text-banners-in-linux-terminal/)

