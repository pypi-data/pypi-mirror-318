import gzip
import pandas as pd
import tempfile

from roktools.c_ext import read_crx

def to_dataframe(filename:str, station:str = "none") -> pd.DataFrame:
    """
    Convert a Compressed (crx.gz) or uncompressed (crx) Hatanaka file into a
    DataFrame
    """

    if filename.endswith('crx.gz') or filename.endswith('crz'):
        with gzip.open(filename, 'rb') as f_in:
            with tempfile.NamedTemporaryFile(delete=False) as f_out:
                f_out.write(f_in.read())
                f_out.seek(0)
                array = read_crx(f_out.name)

    else:
        array = read_crx(filename)

    df = pd.DataFrame(array, columns=['epoch', 'sat', 'rinex3_code', 'value'])
    df['channel'] = df['rinex3_code'].str[-2:]
    df['signal'] = df['sat'] + df['channel']
    MAPPING = {'C': 'range', 'L': 'phase', 'D': 'doppler', 'S': 'snr'}
    df['obstype'] = df['rinex3_code'].str[0].map(lambda x: MAPPING.get(x, 'Unknown'))
    df = df.pivot_table(index=['epoch', 'signal', 'sat', 'channel'], columns=['obstype'], values='value')
    df.reset_index(inplace=True)
    df['station'] = station

    return df
