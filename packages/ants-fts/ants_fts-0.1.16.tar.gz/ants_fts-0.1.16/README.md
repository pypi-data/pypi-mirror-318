# ants-fts
This repository is used to extract features from Antsomi's features.

# Example

```python
import pandas as pd
from datetime import datetime, timedelta
from ants_extractor.IntervalExtractor import IntervalExtractor
from ants_extractor.SkewnessScoreExtractor import SkewnessScoreExtractor
from ants_extractor.DatetimeExtractor import DatetimeExtractor
from ants_extractor.DeductionExtractor import DeductionExtractor
from ants_extractor.PurchasingPowerExtractor import PurchasingPowerExtractor
from ants_extractor.RFMExtractor import RFMExtractor
from datetime import datetime, timedelta
import warnings 
warnings.filterwarnings('ignore')

data = {'encoded_id': {35452: '640327a34',
  40030: '640327a34',
  54858: 'be3e7573a',
  72959: 'be3e7573a',
  73009: 'be3e7573a',
  84052: '89a90516c',
  85677: '89a90516c',
  99817: 'be3e7573a',
  106287: 'be3e7573a',
  123339: '89a90516c',
  134011: '89a90516c',
  150009: '89a90516c',
  168649: 'be3e7573a',
  200112: '640327a34',
  228401: '640327a34',
  234409: '640327a34'},
 'date': {
  35452:  Timestamp('2024-11-10 10:00:00'),
  40030:  Timestamp('2024-11-06 12:30:00'),
  54858:  Timestamp('2024-10-28 20:15:00'),
  72959:  Timestamp('2024-09-20 19:05:00'),
  73009:  Timestamp('2024-09-19 21:55:00'),
  84052:  Timestamp('2024-09-24 18:40:00'),
  85677:  Timestamp('2024-09-24 18:35:00'),
  99817:  Timestamp('2024-08-24 20:20:00'),
  106287: Timestamp('2024-09-29 20:30:00'),
  123339: Timestamp('2024-05-01 14:45:00'),
  134011: Timestamp('2024-06-14 17:10:00'),
  150009: Timestamp('2024-05-01 13:40:00'),
  168649: Timestamp('2024-03-10 20:25:00'),
  200112: Timestamp('2024-04-19 18:40:00'),
  228401: Timestamp('2024-02-19 19:15:00'),
  234409: Timestamp('2024-04-22 12:10:00')},
 'discount': {35452: 0.0,
  40030: 0.0,
  54858: 76000.0,
  72959: 105000.0,
  73009: 74000.0,
  84052: 108000.0,
  85677: 900000.0,
  99817: 164500.0,
  106287: 187000.0,
  123339: 0.0,
  134011: 345000.0,
  150009: 150000.0,
  168649: 159000.0,
  200112: 0.0,
  228401: 106000.0,
  234409: 0.0},
 'pure_revenue': {35452: 100000.0,
  40030: 1700000.0,
  54858: 780000.0,
  72959: 244000.0,
  73009: 1040000.0,
  84052: 1970000.0,
  85677: 1995000.0,
  99817: 1945000.0,
  106287: 2175000.0,
  123339: 100000.0,
  134011: 2790000.0,
  150009: 15745000.0,
  168649: 1990000.0,
  200112: 1050000.0,
  228401: 1900000.0,
  234409: 0.0},
 'revenue': {35452: 100000.0,
  40030: 1700000.0,
  54858: 704000.0,
  72959: 139000.0,
  73009: 966000.0,
  84052: 1862000.0,
  85677: 1095000.0,
  99817: 1780500.0,
  106287: 1988000.0,
  123339: 100000.0,
  134011: 2445000.0,
  150009: 15595000.0,
  168649: 1831000.0,
  200112: 1050000.0,
  228401: 1794000.0,
  234409: 0.0}}

df = pd.DataFrame(data)
fts_01 = IntervalExtractor.extract(df, ['encoded_id'], 'date');
fts_02 = SkewnessScoreExtractor.extract(df, ['encoded_id'], 'date');
fts_03 = DatetimeExtractor.extract(df, ['encoded_id'], 'date');
fts_04 = DeductionExtractor.extract(df, ['encoded_id'], 'discount', 'pure_revenue');
fts_05 = PurchasingPowerExtractor.extract(df, ['encoded_id'], "revenue");
fts_06 = RFMExtractor.extract(df, ['encoded_id'], 'date', "revenue", "2024-12-15 00:00:00");
fts = fts_01.merge(fts_02, how="left").merge(fts_03,how='left').merge(fts_04,how='left').merge(fts_04,how='left').merge(fts_05,how='left').merge(fts_06,how='left');

fts.round(3).T.to_markdown()
|:---------------------------|:----------|:-----------|:----------|
| encoded_id                 | 640327a34 | 89a90516c  | be3e7573a |
| _cnt                       | 5         | 5          | 6         |
| _avg_itv                   | 66.154    | 36.552     | 46.399    |
| _var_itv                   | 8441.535  | 2338.825   | 4681.767  |
| _skewness_score            | 0.415     | 0.366      | -2.106    |
| _weekend_rate              | 0.2       | 0.0        | 0.5       |
| _weekday_rate              | 0.8       | 1.0        | 0.5       |
| _monday_rate               | 0.4       | 0.0        | 0.167     |
| _tuesday_rate              | 0.0       | 0.4        | 0.0       |
| _wednesday_rate            | 0.2       | 0.4        | 0.0       |
| _thurday_rate              | 0.0       | 0.0        | 0.167     |
| _friday_rate               | 0.2       | 0.2        | 0.167     |
| _saturday_rate             | 0.0       | 0.0        | 0.167     |
| _sunday_rate               | 0.2       | 0.0        | 0.333     |
| _am_rate                   | 0.2       | 0.0        | 0.0       |
| _pm_rate                   | 0.8       | 1.0        | 1.0       |
| _dawn_rate                 | 0.0       | 0.0        | 0.0       |
| _morning_rate              | 0.2       | 0.0        | 0.0       |
| _afternoon_rate            | 0.4       | 0.6        | 0.0       |
| _evening_rate              | 0.4       | 0.4        | 1.0       |
| _midnight_rate             | 0.0       | 0.0        | 0.0       |
| _avg_deduction             | 0.014     | 0.128      | 0.142     |
| _var_deduction             | 0.001     | 0.035      | 0.02      |
| _ratio_discount_camp_usage | 0.2       | 0.8        | 1.0       |
| _total_revenue             | 4644000.0 | 21097000.0 | 7408500.0 |
| _aov                       | 928800.0  | 4219400.0  | 1234750.0 |
| _median_ov                 | 1050000.0 | 1862000.0  | 1373250.0 |
| _percentage_rank           | 0.333     | 1.0        | 0.667     |
| _recency                   | 34.582    | 81.223     | 47.157    |
| _frequency                 | 5         | 5          | 6         |
| _monetary                  | 4644000.0 | 21097000.0 | 7408500.0 |

```