If python3 isnt there I can get a better shell just by typing
```
script /dev/null -c bash
```


but the full thing would be:

```
script /dev/null -c bash
Hit Ctrl+Z, then:
stty raw -echo; fg
Then reset and export TERM=xterm. That should give you a proper PTY for su.
```

running process mongodb on port 27117
