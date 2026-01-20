
Why is Unix so pleasant? It's so different from other systems, and from even the most common ways of storing data like a csv or a json file. Unix /etc files say things like cake on each line instead of saying True in a column that says cake at the top, and because of that, each line is independently informative and can be processed without needing a header. Unix config files are all, without exception, underfit data formats, in the sense that they're intentionally less opinionated about who and what will be processing them and modifying them EVEN COMPARED TO A CSV OR JSON FILE! The "list of lines" data type is barely a data type, and it has so many implicit affordances (benefits that just show up without you needing to build them in) than even the simplest forms of additional structure like a dictionary. We don't need to say "grep pattern line.keys()" or "grep pattern line.values()" or "grep pattern list(line.values())[3]"

We just say grep.

Only Unix has this level of elegance, and it's not about code, it's about the international underfitting of data storage to any particular measure of quality.

Say more about this and people who've talked about it. I'm looking for insights into Unix and why it's pleasant that go beyond the standard "Unix philosophy" and "Do one thing and do it well" and "Worse is better" cultural copypasta that everyone's seen a thousand times. The shell with pipes is actually monadic. It's got all the benefits of what Haskell people seek in monads, for free, because there's one type (strings) so all functions compose. All additional structure is "off the books," and is up to the human to decide which structure matters for their current purposes. The shell is the highest level language in existence: unrecognized identifiers are interpreted as EXTERNAL PROGRAMS and looked up in a configurable path! And using exec for code sharing instead of import / include / use / any other method of within process code sharing automatically makes your code async and concurrent and all the best things because the kernel is already running hundreds of processes at once and doing all the relevant locking for you. Exec, the shell, and pipes are the ultimate form of scalable development, and the people who say "long shell scripts are unmaintainable" are right! The shell demands that its sentences (scripts) remain simple. But only the shell is a tower of babel that can unite all programs in all languages together, provided they use exec and stdout / stdin for communication. Say more in this vein and give pointers

---

Major question we need to answer.

> _Why is Unix so pleasant?_

It's not really any of the things we ever hear.

It's things like:

> /etc is both machine readable and human readable.

Config files are not designed to have "a particular syntax."
Compare the idea of a `.tsv` vs how `awk` thinks.
These two things could not be more different.
Ask how each behaves in the presence of `\t\t`.
To a `.tsv`, there's a missing value between the tabs.
To `awk`, and to most of the files in `/etc`, _there is no such thing as a stored missing value._
Missing values are not `Nan`: they're _missing._

To see the difference, consider the "reasonable" case of a csv,
with named columns in the first row (a header),
and boolean values `True` and `False` stored
in the column below some key in that header.

That is, compare this:

| Name | Age | Sex | IsBoopy | OtherFact | OtherMeasurement |
| ---- | --- | --- | ------- | --------- | ---------------- |
| A    | 1   | M   | True    | False     | 42               |
| B    | 2   | F   | False   | True      | 69               |
| C    | 3   | M   | True    | False     | 100              |
| D    | 4   | F   | False   | False     | 22               |

With this...

---

```sh
user@world $ cat /proc/locks 
1: POSIX  ADVISORY  WRITE 10540 103:02:2364150 1073741826 1073742335
2: POSIX  ADVISORY  WRITE 10540 103:02:2364148 1073741826 1073742335
3: FLOCK  ADVISORY  WRITE 1359 00:18:4945 0 EOF
4: FLOCK  ADVISORY  WRITE 1359 103:02:4849776 0 EOF
5: POSIX  ADVISORY  WRITE 10540 103:02:2363939 0 EOF
6: POSIX  ADVISORY  WRITE 10540 103:02:2363980 0 EOF
7: POSIX  ADVISORY  WRITE 2042 103:02:2129080 1073741826 1073742335
8: POSIX  ADVISORY  WRITE 2042 103:02:2129080 1073741824 1073741824
9: FLOCK  ADVISORY  WRITE 1325 103:02:4849810 0 EOF
10: FLOCK  ADVISORY  WRITE 1325 103:02:4849809 0 EOF
11: FLOCK  ADVISORY  WRITE 1325 103:02:4849807 0 EOF
12: FLOCK  ADVISORY  WRITE 1325 103:02:4849806 0 EOF
...
```

```sh
user@world $ cat /proc/uptime
11653.43 109983.16
```

```sh
user@world $ cat /proc/version
Linux version 6.18.2 (nixbld@localhost) (gcc (GCC) 14.3.0, GNU ld (GNU Binutils) 2.44) \#1-NixOS SMP PREEMPT_DYNAMIC Thu Dec 18 13:03:43 UTC 2025
```

```sh
user@world $ cat /proc/vmstat | head
nr_free_pages 8130809
nr_free_pages_blocks 7973376
nr_zone_inactive_anon 0
nr_zone_active_anon 614870
nr_zone_inactive_file 731652
nr_zone_active_file 414113
nr_zone_unevictable 130127
nr_zone_write_pending 28
nr_mlock 8
nr_zspages 0
```

```sh
user@world $ cat /proc/devices
Character devices:
  1 mem
  4 /dev/vc/0
  4 tty
  4 ttyS
  5 /dev/tty
  5 /dev/console
  5 /dev/ptmx
  7 vcs
 10 misc
 13 input
 14 sound
 29 fb
 81 video4linux
 90 mtd
116 alsa
128 ptm
136 pts
180 usb
188 ttyUSB
189 usb_device
216 rfcomm
226 drm
238 ptp
239 pps
240 watchdog
241 media
242 aux
243 cec
244 tpm
245 hidraw
246 nvme-generic
247 nvme
248 dax
249 binder
250 bsg
251 lirc
252 rtc
253 pwm
254 gpiochip
261 accel

Block devices:
  7 loop
254 device-mapper
259 blkext

```

```sh
user@world $ cat /proc/swaps 
Filename				Type		Size		Used		Priority
/dev/nvme0n1p3                          partition	10485756	0		-2
```

```sh
user@world $ cat /proc/misc 
200 tun
130 watchdog
242 rfkill
237 loop-control
232 kvm
229 fuse
183 hw_random
235 autofs
236 device-mapper
259 cpu_dma_latency
258 udmabuf
228 hpet
257 userfaultfd
231 snapshot
256 vga_arbiter
```

```sh
user@world $ zcat /proc/config.gz | head -n 20
#
# Automatically generated file; DO NOT EDIT.
# Linux/x86_64 6.18.2 Kernel Configuration
#
CONFIG_CC_VERSION_TEXT="gcc (GCC) 14.3.0"
CONFIG_CC_IS_GCC=y
CONFIG_GCC_VERSION=140300
CONFIG_CLANG_VERSION=0
CONFIG_AS_IS_GNU=y
CONFIG_AS_VERSION=24400
CONFIG_LD_IS_BFD=y
CONFIG_LD_VERSION=24400
CONFIG_LLD_VERSION=0
CONFIG_RUSTC_VERSION=109101
CONFIG_RUST_IS_AVAILABLE=y
CONFIG_RUSTC_LLVM_VERSION=210102
CONFIG_CC_HAS_ASM_GOTO_OUTPUT=y
CONFIG_CC_HAS_ASM_GOTO_TIED_OUTPUT=y
CONFIG_TOOLS_SUPPORT_RELR=y
CONFIG_CC_HAS_ASM_INLINE=y
```

```sh
user@world $ cat /proc/cpuinfo | head -n 30
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 186
model name	: 13th Gen Intel(R) Core(TM) i7-1355U
stepping	: 3
microcode	: 0x6133
cpu MHz		: 847.384
cache size	: 12288 KB
physical id	: 0
siblings	: 12
core id		: 0
cpu cores	: 10
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 32
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq rdpid movdiri movdir64b fsrm md_clear serialize arch_lbr ibt flush_l1d arch_capabilities
vmx flags	: vnmi preemption_timer posted_intr invvpid ept_x_only ept_ad ept_1gb flexpriority apicv tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid ple shadow_vmcs ept_violation_ve ept_mode_based_exec tsc_scaling usr_wait_pause
bugs		: spectre_v1 spectre_v2 spec_store_bypass swapgs eibrs_pbrsb rfds bhi spectre_v2_user vmscape
bogomips	: 5222.40
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:
```

```sh
user@world $ cat /proc/cpuinfo | grep '^processor'
processor	: 0
processor	: 1
processor	: 2
processor	: 3
processor	: 4
processor	: 5
processor	: 6
processor	: 7
processor	: 8
processor	: 9
processor	: 10
processor	: 11
```

```sh
user@world $ cat /sys/kernel/oops_count 
0
```

```sh
user@world $ cat /sys/kernel/cpu_byteorder 
little
```

```sh
user@world $ cat /sys/kernel/address_bits 
64
```

```sh
user@world $ cat /sys/power/state 
freeze mem disk
```

