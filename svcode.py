ha = 110

A = 100

th = 150
contagem = 0
for anos in range(A):
    ha += 3
    th += 2
    contagem +=1
    if ha>th:
        break
print(" o homem aranha sera mais alto que o thanos depois de:", contagem,"anos")