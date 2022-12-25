# Plover plugin for Hangeul input
This is not a full-fledged Korean steno system, but merely a syllable-based system which allows you to input Hangeul.

## Installation

1. Navigate to the repo directory: `cd plover-hangeul`
2. Run `plover -s plover_plugins install -e .` (remember the final dot!)
3. Restart Plover.
4. Go to `Configure > System`, and change your system to `Hangeul`.

## Layout

```
HTPY* *JPHTD
SKRW* *LBGSZ
   AO EU

ㄱ K     ㄲ SK     ㅋ KP
ㄷ TK    ㄸ STK    ㅌ T
ㅂ PR    ㅃ SPR    ㅍ P
ㅈ KR    ㅉ SKR    ㅊ TP
ㄴ HTP   ㅁ HT     ㄹ R
ㅅ S     ㅆ HS     ㅎ H

ㅏ A     ㅑ YA     ㅘ WA
ㅐ AE    ㅒ YAE    ㅙ WAE
ㅓ OE    ㅕ YOE    ㅝ WO
ㅔ E     ㅖ YE     ㅞ WE
ㅗ O     ㅛ YO     ㅚ OEU
ㅜ U     ㅠ YU     ㅟ WEU
ㅡ AO    ㅣ EU     ㅢ AOEU

ㄱ -G    ㄲ -HG    ㄳ -GS
ㄴ -PB   ㄵ -JL    ㄶ -LH
ㄷ -D    ㄹ -L     ㄺ -LG
ㄻ -LPH  ㄼ -LB    ㄽ -LS
ㄾ -LT   ㄿ -LP    ㅀ -LH
ㅁ -PH   ㅂ -B     ㅄ -BS
ㅅ -S    ㅆ -Z     ㅇ -PBG
ㅈ -J    ㅊ -JP    ㅋ -BG
ㅌ -T    ㅍ -P     ㅎ -H
```
