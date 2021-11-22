import Candidatos

votoGov1 = 0
votoGov2 = 0
votoGov3 = 0
votoGov4 = 0
votoGov5 = 0

votoPres1 = 0
votoPres2 = 0
votoPres3 = 0
votoPres4 = 0
votoPres5 = 0

anularGov = 0
anularPres = 0

votoEmBrancoGov = 0
votoEmBrancoPres = 0


def menu():
    print(f"""\n
-------------APURAÇÃO DOS VOTOS-----------------------
               Votos para Governador  
                               
 Votos do(a) candidato(a) {Candidatos.nomeGov1}: {votoGov1} 
                 
 Votos do(a) candidato(a) {Candidatos.nomeGov2}: {votoGov2}  
                     
 Votos do(a) candidato(a) {Candidatos.nomeGov3}: {votoGov3} 
                   
 Votos do(a) candidato(a) {Candidatos.nomeGov4}: {votoGov4}  
                 
 Votos do(a) candidato(a) {Candidatos.nomeGov5}: {votoGov5}                     

               Votos para Presidente 
                                
 Votos do(a) candidato(a) {Candidatos.nomePres1}: {votoPres1}  
            
 Votos do(a) candidato(a) {Candidatos.nomePres2}: {votoPres2} 
     
 Votos do(a) candidato(a) {Candidatos.nomePres3}: {votoPres3}  
                              
 Votos do(a) candidato(a) {Candidatos.nomePres4}: {votoPres4} 
               
 Votos do(a) candidato(a) {Candidatos.nomePres5}: {votoPres5}        

               Votos Nulos        

 Votos nulos para governador: {anularGov}     
                   
 Votos nulos para presidente: {anularPres}                       

               Votos em Branco  

 Votos em branco para governador: {votoEmBrancoGov}  
                  
 Votos em branco para presidente: {votoEmBrancoPres}                   
------------------------------------------------------\n""")