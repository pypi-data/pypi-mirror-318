import pandas as pd
from .BaseExtractor import BaseExtractor



class DeductionExtractor(BaseExtractor):
    
    def __init__(self):

        pass;


    @staticmethod
    def extract(df, grouped_columns, discount_amount_column, pure_revenue_column):
        _df = df[grouped_columns + [discount_amount_column, pure_revenue_column]];
        _df['discount_rate'] = _df[discount_amount_column]/_df[pure_revenue_column];
        _df['is_discount'] = (_df[discount_amount_column]>0).astype(int);
        deduction_fts = _df.groupby(by=grouped_columns)\
                            .agg(\
                                cnt = (discount_amount_column, "count"),\
                                _avg_deduction = ('discount_rate', 'mean'),\
                                _var_deduction = ('discount_rate', 'var'),\
                                discount_cnt = ('is_discount', 'sum')
                            )\
                            .reset_index();
        deduction_fts['_ratio_discount_camp_usage'] = deduction_fts.discount_cnt/deduction_fts.cnt
        deduction_fts = deduction_fts[grouped_columns + ['_avg_deduction', '_var_deduction', '_ratio_discount_camp_usage'] ]
        return deduction_fts;

    pass




