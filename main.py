import ecb

abc = ecb.kr.get_refinancing_rate()
print(abc)

abc = ecb.kr.get_deposit_rate()
print(abc)

abc = ecb.kr.get_marginal_rate()
print(abc)

abc = ecb.gdp.get_gdp_q()
print(abc)

abc = ecb.hicp.get_hicp()
print(abc)

print(ecb.__version__)
