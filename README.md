# One Emoji, One Smile — 🫂

[![bounty](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/Nadanese93/u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/Nadanese93/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the [One Emoji, One Smile](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f) bounty on make.fun ($5 prize, top 10 paid).

## The emoji

**🫂 — people hugging (U+1FAC2)**

Two people hugging is the warmest literal reading of "make a stranger
smile": it shows warmth being given, not just felt. It reads as kind
and friendly at first glance, means the same thing to a stranger of
any age or background, feels deliberately picked rather than the first
smiley that comes to mind, and — as an emoji, not a real embrace —
carries no intimacy, sarcasm or flirtation from a stranger.

It is also the strongest unused pick in the field. Verified against
the public API (217 submissions fetched, 24 Nov 2026): the hugging
face 🤗 appears 80 times, heart hands 🫶 39 times, sunflower 🌻 19,
smiling face 😊 16, sun 🌞 16 — every one of them shares its rate
with its earlier copies. 🫂 appears **0 times**.

## How it works

`main.py` (Python 3 stdlib only, no network, deterministic) validates
the emoji against the gate — exactly one character, 1–8 characters,
not whitespace-only, single line — then writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing
newline, and reads the file back to prove it holds exactly what was
validated.

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"  # 🫂
```

## License

MIT — see [LICENSE](LICENSE).
