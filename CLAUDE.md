# Large Candle Detector (Pine Script v5)

Single-file TradingView indicator: `large_candle_detector.pine`

## What it does
Detects "large" candles in real-time on any timeframe and fires an alert N seconds before bar close.

## Detection logic
1. **Minimum size** — `minSizePct` scales with timeframe via a power-fit anchored at 15m→0.6%, 4h→2.0% (exponent ≈ 0.4342)
2. **Dynamic look-back** — `lookback = min(cap, round(currentPct% × i_barsPer1pct))`, hard-capped at `i_lookbackCap`
3. **Competition filter** — within the look-back window, counts previous closed bars whose body > 50% of current AND ≥ `minSizePct`; flag suppressed if count > `i_maxAbove`
4. `isLarge = okSize AND okRatio`

## Key variables
| Variable | Purpose |
|---|---|
| `currentPct` | Current bar body size as % of open |
| `minSizePct` | Timeframe-scaled minimum threshold |
| `lookback` | Dynamic look-back window (bars) |
| `aboveCount` | Count of competing previous bars |
| `isLarge` | Final detection flag |
| `nearClose` | True when `timenow >= time_close - N*1000ms` |
| `fired` | One-shot guard — reset each bar, set on first near-close tick |

## Inputs
- `i_barsPer1pct` — bars per 1% of candle size (default 6)
- `i_maxAbove` — max previous bars allowed > 50% threshold (default 1)
- `i_lookbackCap` — hard cap on look-back window (default 300)
- `i_secsBefore` — seconds before close to fire alert (default 10)
- `i_showTable` / `i_tablePos` — status table toggle and position

## Visuals
- Bar color → lime when flagged
- Triangle marker below bar
- Background tint (lime, 50% opacity)
- Real-time status table (6 rows × 2 cols)

## Alert behaviour
- `alert()` fires once per bar via `fired` guard + `alert.freq_once_per_bar`
- `alertcondition` for TradingView Alerts panel (positive leg only)
- Message includes ticker, timeframe, body%, look-back, and competition count

## Context navigation
When you need to understand this project, read this file first — only open `large_candle_detector.pine` if the specific line-level code is needed.
