# Plover plugin for Hangeul input
This is not a full-fledged Korean steno system, but merely a syllable-based system which allows you to input Hangeul.

## Installation

1. Navigate to the repo directory: `cd plover-hangeul`
2. Run `plover -s plover_plugins install -e .` (remember the final dot!)
3. Restart Plover.
4. Go to `Configure > System`, and change your system to `Hangeul`.

## Layout

```
STPH* *JPHTD
SKWR* *LBGSZ
   AO EU

ㄱ K     ㄲ SK     ㅋ KP
ㄷ TK    ㄸ STK    ㅌ T
ㅂ TP    ㅃ STP    ㅍ P
ㅈ KR    ㅉ SKR    ㅊ KH
ㄴ TPH   ㅁ PH     ㄹ R
ㅅ S     ㅆ ST     ㅎ H
ㅇ TKPW (fingerspelling only)

ㅏ A     ㅑ AU     ㅘ WA
ㅐ AE    ㅒ AEU    ㅙ WAE
ㅓ OE    ㅕ OEU    ㅝ WO
ㅔ E     ㅖ AOE    ㅞ WE
ㅗ O     ㅛ OU     ㅚ WOE
ㅜ U     ㅠ AOU    ㅟ WEU
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
