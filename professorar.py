professor = []

#PARA SALVAR CADASTRO, ATUALIZAÇÃO E REMOÇÃO
def salvar_cadastrop():
    global professor
    arq = open('professor.txt', 'w', encoding = "utf-8")
    for i in professor:
        nome_professor = str(i[0])
        cpf_professor = str(i[1])
        dpt_professor = str(i[2])
        arq.write('%s %s %s\n' %(nome_professor, cpf_professor, dpt_professor))
    arq.close()


#CADASTRO
def cadastro_prof():
    while True:
        try:
            op = int(input("Para cadastrar professor digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                nome_professor = input("Digite seu nome para cadastro aqui: ") #ADICIONAR DADOS DO PROFESSOR
                cpf_professor = input("Digite seu cpf para cadastro aqui: ")
                dpt_professor = input("Digite seu departamento para cadastro aqui: ")
                for i in range(len(professor)):
                    if cpf_professor in professor[i][1]: #CASO ELE SEU CPF JÁ ESTEJA NA LISTA, SIGNIFICA QUE JÁ ESTÁ CADASTRADO
                        print("Professor já cadastrado. ")
                else:
                    professor.append([nome_professor, cpf_professor, dpt_professor]) #CASO CONTRÁRIO, ELE SERÁ ADICIONADO À LISTA DE PROFESSORES
                    print("Cadastro realizado com sucesso: {}, {}, {}".format(nome_professor, cpf_professor, dpt_professor))
                    salvar_cadastrop()  #FUNÇÃO PARA SALVAR CADASTRO
                    break
            elif op == 2: #CASO ELE ESCOLHA A OPÇÃO 2, O PROGRAMA SERÁ FINALIZADO
                break
            else:
                print("Opção inválida.") #CASO ELE ESCOLHA QUALQUER OUTRA OPÇÃO, SERÁ CONSIDERADA INVÁLIDA
        except EOFError:
            break


#REMOVER CADASTRO
def remover_cadastro():
    while True:
        try:
            op = int(input("Para remover o cadastro digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                del_professor = input("Para a remoção de cadastro, digite seu cpf aqui: ") #PARA EXERCUTAR A REMOÇÃO É PRECISO INFORMAR O CPF
                for i in range(len(professor)):
                    if del_professor in professor[i][1]: #CASO O ALUNO ESTEJA CADASTRADO, A REMOÇÃO É EFETUADA
                        professor.remove(professor[i])
                        print("Professor removido com sucesso.")
                        salvar_cadastrop()
                else:
                    print("Cadastro não encontrado.") #CASO CONTRÁRIO, SERÁ INFORMADO DE QUE ESTE CPF NÃO ESTÁ CADASTRADO
                    break
            elif op == 2: #CASO ELE ESCOLHA A OPÇÃO 2, O PROGRAMA DEIXARÁ DE RODAR
                break
            else:
                print("Operação inválida.") #CASO ELE ESCOLHA OUTRA OPÇÃO, ELA SERÁ CONSIDERADA INVÁLIDA
        except EOFError:
            break


#CONSULTAR CADASTRO
def consultar_cadastro():
    while True:
        try:
            op = int(input("Para consultar cadastro digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                consulta_prof = input("Para consulta, digite seu cpf aqui: ") #PARA A CONSULTA É NECESSÁRIO A VERIFICAÇÃO DO CPF
                for i in range(len(professor)):
                    if professor[i][1] == consulta_prof: #SE O CPF ESTIVER NA LISTA, O CADASTRO SERÁ CONSULTADO NORMALMENTE
                        print("NOME: {}\nCPF: {}\nDEPARTAMENTO: {}".format(professor[i][0], professor[i][1], professor[i][2]))
                    else:
                        print("Cadastro não encontrado.") #CASO CONTRÁRIO, SRÁ INFORMADO DE QUE NÃO HÁ CADASTRO COM ESTE CPF
            elif op == 2:
                break #FINALIZAR PROGRAMA
            else:
                print("Operação inválida.") #CASO A OPÇÃO DELE SEJA DIFERENTE DAS APRESENTADAS, ELA SERÁ CONSIDERADA INVÁLIDA
        except EOFError:
            break


#ATUALIZAR CADASTRO
def atualizar_prof():
    while True:
        try:
            op = int(input("Para atualizar cadastro digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                alt_professor = input("Digite seu CPF para ter acesso à atualização: ")
                for i in range(len(professor)):
                    if alt_professor in professor[i][1]:
                        opc = int(input("Para atualizar o nome digite 1, para atualizar o cpf digite 2, e 3 para departamento: "))
                        if opc == 1:
                            nome = input("Digite seu nome aqui: ")
                            professor[i][0] = nome
                            print("NOME: {}\nPROFESSOR: {}\nDEPARTAMENTO: {}".format(professor[i][0], professor[i][1], professor[i][2]))  # ENFEITAR + ESSA PARTE!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            print("Cadastro alterado com sucesso.")
                            salvar_cadastrop()
                        elif opc == 2:
                            cpf = input("Digite seu cpf: ")
                            professor[i][1] = cpf
                            print("NOME: {}\n CPF: {}\n DEPARTAMENTO: {}".format(professor[i][0], professor[i][1], professor[i][2]))  # ENFEITAR ESSA PARTE!!!!!!!!!!!!!!!!!!!!!!!
                            print("Cadastro alterado com sucesso.")
                            salvar_cadastrop()
                        elif opc == 3:
                            dpt = input("Digite seu departamento aqui: ")
                            professor[i][2] = dpt
                            print("NOME: {}\nCPF: {}\n DEPARTAMENTO: {}".format(professor[i][0], professor[i][1], professor[i][2]))
                            print("Cadastro alterado com sucesso")
                            salvar_cadastrop()
                            break
                    else:
                        print("Cadastro não encontrado.")
            elif op == 2:
                break
            else:
                print("Operação inválida.")
        except EOFError:
            break
            
