import pandas as pd

import ecb

abc = ecb.kr.get_refinancing_rate(start_date=pd.Timestamp(2022, 1, 1))
print(abc)

abc = ecb.kr.get_deposit_rate(start_date=pd.Timestamp(2022, 1, 1))
print(abc)

abc = ecb.kr.get_marginal_rate(start_date=pd.Timestamp(2022, 1, 1))
print(abc)

#abc = ecb.gdp.get_gdp_q()
#print(abc)

#abc = ecb.hicp.get_hicp()
#print(abc)

print(ecb.__version__)
