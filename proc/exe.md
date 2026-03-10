〇：

零：

```sh
grep -Po '(?<=: ).*?(?= 64)' <(file $(readlink -f $(which $0)))
```

/proc/self/exe