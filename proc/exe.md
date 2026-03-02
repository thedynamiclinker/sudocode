〇：

零：

```sh
grep -Po '(?<=: ).*?(?= 64)' <(file $(readlink -f $0))
```

/proc/self/exe