
import numpy as np
import scipy.stats.distributions as dist

n1 = 1 # кол-во единиц в первой серии
N1 = 5 # кол-во бинарных испытаний в первой серии

n2=10 # кол-во единиц во 2й серии
N2=55 # кол-во бинарных испытаний во 2й серии

#-----------ВАР_1 для двухвыборочного случая считаю п-валью вручную!
# рассчитываем значение статистики критерия
total_proportion = (n1 + n2)/(N1+N2)
variance = total_proportion * (1 - total_proportion)
standard_error = np.sqrt(variance * (1 / N1 + 1 / N2))
test_stat = (n1/N1 - n2/N2) / standard_error

# рассчитываем  p-value
pvalue = 2*dist.norm.cdf(-np.abs(test_stat)) # Multiplied by two indicates a two tailed testing.
print("Computed P-value is", pvalue)

#-----------ВАР_2 для двухвыборочного случая считаю п-валью библиотекой за одну стркчку!
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
counts = np.array([n1, n2])
nobs = np.array([N1, N2])
stat, pval = proportions_ztest(counts, nobs)
print ("pval by statsmodels ="+str(pval))

#-----------ВАР_3 для одновыборочного случая считаю п-валью библиотекой за одну стркчку!
predicted_p = .5 # дано - это помнится в predicted(id)
stat, pval = proportions_ztest(n1, N1, predicted_p)
print('pval in one sample test =' + str(pval))