from ipaddress import ip_network, ip_address

import pytest

import pandas as pd
from tests.conftest import DATADIR, validate_host_shape


def validate_mroutes(df: pd.DataFrame):
    '''Validate the routes table for all values'''

    # assert (df.vrf != '').all()
    print(df.columns)
    assert (df.group != '').all()
    assert (df.source != '').all()


@ pytest.mark.parsing
@ pytest.mark.mroutes
@ pytest.mark.parametrize('table', ['mroutes'])
@ pytest.mark.parametrize('datadir', DATADIR)
# pylint: disable=unused-argument
def test_mroutes_parsing(table, datadir, get_table_data):
    '''Main workhorse routine to test parsed output for Routes'''

    df = get_table_data

    print(df)

    ns_dict = {
        'eos': 2
    }

    assert not df.empty
    validate_host_shape(df, ns_dict)
    validate_mroutes(df)
