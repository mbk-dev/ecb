import ecb

abc = ecb.kr.get_refinancing_rate()
print(abc.tail(5))

abc = ecb.kr.get_deposit_rate()
print(abc.tail(5))

abc = ecb.kr.get_marginal_rate()
print(abc.tail(5))

abc = ecb.gdp.get_gdp_q()
print(abc.tail(5))

abc = ecb.hicp.get_hicp()
print(abc.tail(5))

print(ecb.__version__)
