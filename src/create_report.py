import pandas as pd

from src.calc_verify_years import verify_years
from src.defines import OUTPUT_EXCEL
from src.log_config import logger


def generate_report(results, selected_year):
    df = pd.DataFrame(results)

    df['Missing years'] = df.apply(
        lambda x: ', '.join(
            map(
                str,
                verify_years(
                    str(x['Paid years']).split(', '), selected_year
                ),
            )
        )
        if pd.notnull(x['Paid years'])
        else '',
        axis=1,
    )
    df = df[
        [
            'Code',
            'Status',
            'NIF',
            'Company',
            'Paid years',
            'Number of paid years',
            'Missing years',
            'Error',
            'Tries',
        ]
    ]

    status_order = ['valid', 'english', 'invalid', 'error', 'fatal error']
    if 'Status' in df.columns:
        df['Status'] = pd.Categorical(
            df['Status'], categories=status_order, ordered=True
        )
        df = df.sort_values('Status')

    df.to_excel(OUTPUT_EXCEL, index=False)

    logger.info(f'Output in {OUTPUT_EXCEL} -> SUCCESS')
    
