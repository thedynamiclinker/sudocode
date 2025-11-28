
The solution to the Gödel implementation problem
found in the primeval history of lost+found/4/4
as revealed to the Nus by @2.

---

## Before @2 improvements

```python
>>> %time join(1024, 2)
Wall time: 1.65 s
3072

>>> %time join(1024, 3)
Wall time: 22.5 ms
3072

>>> %time join(1024, 4)
Wall time: 12.7 s
9216

>>> %time join(1024, 5)
Wall time: 18 ms
3072

>>> %time join(1024, 6)
Wall time: 25.7 s
15360
```

## After @2 improvements

```python
>>> %time join(1024, 2)
Wall time: 1.02 s
3072

>>> %time join(1024, 3)
Wall time: 14.3 ms
3072

>>> %time join(1024, 4)
Wall time: 6.85 s
9216

>>> %time join(1024, 5)
Wall time: 15.2 ms
3072

>>> %time join(1024, 6)
Wall time: 12.7 s
15360
```

---

The nus continue here.