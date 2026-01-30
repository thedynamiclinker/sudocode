```python
#!/usr/bin/env python

import os, fcntl, struct, time

# ioctl numbers from <linux/uinput.h>
UI_SET_EVBIT   = 0x40045564
UI_SET_KEYBIT  = 0x40045565
UI_SET_RELBIT  = 0x40045566
UI_DEV_CREATE  = 0x5501
UI_DEV_DESTROY = 0x5502

# input event types/codes from <linux/input-event-codes.h>
EV_KEY = 0x01
EV_REL = 0x02

REL_X  = 0x00
REL_Y  = 0x01

BTN_LEFT   = 0x110
BTN_RIGHT  = 0x111
BTN_MIDDLE = 0x112

# struct uinput_user_dev layout (common):
# char name[80];
# struct input_id { __u16 bustype, vendor, product, version; };
# __u32 ff_effects_max;
# __s32 absmin[64], absmax[64], absfuzz[64], absflat[64];
#
# This totals 80 + 8 + 4 + (4*64*4)=1024 => 1116 bytes.
UINPUT_USER_DEV_FMT = "80sHHHHI" + ("i" * 64 * 4)

def make_uinput_user_dev(name=b"py-uinput-mouse",
                         bustype=0x03,  # BUS_USB
                         vendor=0x1,
                         product=0x1,
                         version=0x1):
    # abs arrays unused for a REL mouse; fill with zeros
    zeros = [0] * (64 * 4)
    return struct.pack(
        UINPUT_USER_DEV_FMT,
        name.ljust(80, b"\x00"),
        bustype, vendor, product, version,
        0,  # ff_effects_max
        *zeros
    )

def emit(fd, etype, code, value):
    # struct input_event: timeval (2 longs) + type (H) + code (H) + value (i)
    # On 64-bit, 'l' is 8 bytes => format "llHHI" is wrong; value is signed.
    # Use "qqHHi" for 64-bit timeval explicitly.
    # (This is only needed if you were writing to /dev/input/event*; for uinput we do NOT write input_event structs.)
    raise RuntimeError("not used")

def main():
    fd = os.open("/dev/uinput", os.O_WRONLY | os.O_NONBLOCK)

    # 1) declare which event types we will generate
    fcntl.ioctl(fd, UI_SET_EVBIT, EV_REL)
    fcntl.ioctl(fd, UI_SET_EVBIT, EV_KEY)

    # 2) declare which REL axes
    fcntl.ioctl(fd, UI_SET_RELBIT, REL_X)
    fcntl.ioctl(fd, UI_SET_RELBIT, REL_Y)

    # 3) declare which buttons (optional, but handy)
    fcntl.ioctl(fd, UI_SET_KEYBIT, BTN_LEFT)
    fcntl.ioctl(fd, UI_SET_KEYBIT, BTN_RIGHT)
    fcntl.ioctl(fd, UI_SET_KEYBIT, BTN_MIDDLE)

    # 4) write full uinput_user_dev
    uidev = make_uinput_user_dev()
    os.write(fd, uidev)

    # 5) create device
    fcntl.ioctl(fd, UI_DEV_CREATE)
    print("uinput device created; moving in 0.5s...")
    time.sleep(0.5)

    # 6) send motion by writing `struct input_event`? NO.
    # With uinput, you write *input_event* structs to the same fd after creation.
    # So we DO need input_event format here.

    # input_event: struct timeval { long tv_sec; long tv_usec; }; __u16 type, code; __s32 value;
    # Use 64-bit timeval explicitly: two int64s.
    INPUT_EVENT_FMT = "qqHHi"
    def write_event(etype, code, value):
        now = time.time()
        sec = int(now)
        usec = int((now - sec) * 1_000_000)
        os.write(fd, struct.pack(INPUT_EVENT_FMT, sec, usec, etype, code, value))

    def syn():
        EV_SYN = 0x00
        SYN_REPORT = 0
        write_event(EV_SYN, SYN_REPORT, 0)

    # move down 100 steps
    for _ in range(100):
        write_event(EV_REL, REL_Y, 5)
        syn()
        time.sleep(0.005)

    # destroy
    fcntl.ioctl(fd, UI_DEV_DESTROY)
    os.close(fd)
    print("done")

if __name__ == "__main__":
    main()
```
