# One Letter for Your Day

Entry for the make.fun bounty
[u-puan-one-letter-for-your-day-e54e9c36](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36).

![competition](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)
![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/emafajriana/u-puan-one-letter-for-your-day-e54e9c36-entry/rank.svg)
![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/emafajriana/u-puan-one-letter-for-your-day-e54e9c36-entry/reward.svg)

## The entry

One letter: **K**.

The whole entry is a single character — exactly one byte in
`/output/entry.txt`, no newline, no gloss. K stands for the day the
honest way: *knackered*. A sharp picture (finished, on the sofa),
a slang punchline that lands at once, and a hard K that fits the
word it carries. Backups considered: killer, kaput — every road
from K leads somewhere strong.

## How it runs

```sh
python3 main.py
```

`main.py` (Python standard library only) writes the single byte
`K` to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`),
then reads it back and verifies the file is exactly one byte and
that byte is a letter A–Z — a trailing newline would be 2 bytes
and fail the gate, so the write is binary and exact.

## License

MIT — see [LICENSE](LICENSE).
