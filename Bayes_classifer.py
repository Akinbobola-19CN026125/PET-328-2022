print('Bayes Theorem')
loc_D = float(input('Enter the mean value of the dolomite:'))
scale_D = float(input('Enter the standard deviation value for dolomite:'))
loc_S = float(input('Enter the mean value of the shale:'))
scale_S = float(input('Enter the standard deviation value for shale'))
count_D = float(input('Enter count value for dolomite'))
count_S = float(input('Enter count value for shale'))
count_total = count_D + count_S
p_D = count_D / count_total
p_S = count_S / count_total

#p_gamma_D = p(gamma>60|D)
#p_gamma_S = p(gamma>60|S)
#p_D_gamma_60 = p(D|gamma>60)

import scipy.stats
p_gamma_D = 1-scipy.stats.norm(loc_D, scale_D).cdf(0.5)
p_gamma_S = 1-scipy.stats.norm(loc_S, scale_S).cdf(0.5)
p_D_gamma_60 = (p_D* p_gamma_D) / (p_D* p_gamma_D + p_S * p_gamma_S)


if p_D_gamma_60 >= 0.5:
    print('The formation interval is Dolomite, a pay lithology')

else:
    print('The formation interval is shale, a non pay lithology')
print('Therefore, the reservoir formation interval has been determined')
