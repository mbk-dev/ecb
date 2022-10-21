from importlib.metadata import version
from ecb.kr import (get_main_rate,
                    get_deposit_rate,
                    get_marginal_rate,
                    )
from ecb.gdp import get_gdp_q
from ecb.hicp import get_hicp
from ecb.request_data import get_data_frame

__version__ = version("ecb")
