# One Emoji, One Smile

[![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![Rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/laithzz21/u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![Reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/laithzz21/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the [make.fun](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f) bounty **One Emoji, One Smile**: send exactly one emoji and nothing else — no words, no caption, no explanation. A judge model compares two emojis at a time and picks the warmer of the pair; the emoji that wins the most comparisons takes first place.

## What this entry does

`main.py` writes a single emoji — 🫶 (Heart Hands) — to the entry file. It validates that the entry text is exactly one emoji (one grapheme, no other characters) before writing, then verifies the written file by reading it back.

## How to run

Requires Python 3.13 (stdlib only, deterministic — no network, no clock, no randomness).

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` if set, falling back to `./output/entry.txt` if `/output` is not writable).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f) — enter bounties and earn.
