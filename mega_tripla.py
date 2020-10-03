palavra = raw_input()
palavra_contrario = ''

primeira_parte = ''
segunda_parte = ''

for i in range(len(palavra) - 1, - 1, -1):
	   
	  palavra_contrario += palavra[i] 
	   
for e in range(len(palavra_contrario)):
	
	if e % 2 == 0:
		
	   primeira_parte += palavra_contrario[e]	

	elif e % 2 != 0:
		
	   segunda_parte += palavra_contrario[e]

resultado_1 = primeira_parte + segunda_parte + palavra[-1] + palavra[0]

palavra = raw_input()

primeira_parte = ''
segunda_parte = ''

for i in range(len(palavra) - 1, -1, -1):
	
	if i % 2 == 0:
		primeira_parte += palavra[i]

for k in range(len(palavra)- 1, -1, -1):
	
	if k % 2 != 0:
		segunda_parte += palavra[k]
		
resultado_2 = primeira_parte + segunda_parte + palavra[len(palavra)-1] + palavra[0]


if resultado_1 == resultado_2:
	
   print resultado_1
   print ''
   print resultado_2
   print '\nIguais:'
	   
else: 

    print resultado_1
    print ''
    print resultado_2
    print '\nDiferentes:'		  
