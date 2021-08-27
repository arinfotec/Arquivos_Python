# Codigo para levantamento de informações de Hardware e software do computador
# objetivo utilizar para fazer inventário de hardware em rede
# by André R. Mendes - Ago/21
# versão 1.0   - Em desenvolvimento e aperfeiçoamento.

import platform, psutil, wmi, cpuinfo, socket, os

#inicio
print("Configuração de Hardware e SO do equipamento\n")

#nome da maquina
name = platform.node()
print('Hostname: {}'.format(name))
#tipo de SO
tipo_so = platform.system()
print('Tipo de SO: {}'.format(tipo_so))
# versao_so
versao_so = platform.release()
print('Versão SO: {}'.format(versao_so))
# release_so
release_so = platform.version()
print('release SO: {}'.format(release_so))

# tipo_proc = platform.processor()0
# tipo_proc = platform.architecture()
# print('Tipo Processador: {}'.format(tipo_proc))

#qtd nucelo do processador - false naomostra treads
proc_nucleo = psutil.cpu_count(logical=False)
print("Quant. Nucleo Processador: {}".format(proc_nucleo))
#qtd memoria em GB
memoria = str(round(psutil.virtual_memory().total / (1024.0 ** 3)))
print('Quantidade Memória Ram (GB): {}'.format(memoria))

#placa mae e processador
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]
#placa mae marca e modleo
#print(f"Manufacturer: {my_system.Manufacturer}")
marca_plmae = my_system.Manufacturer
print('Marca Pl. Mae: {}'.format(marca_plmae))
mod_plmae = my_system.Model
print('Modelo Pl. Mae: {}'.format(mod_plmae))
#print(f"Model: {my_system.Model}")

# modelo processador
my_system = platform.uname()
mod_cpu = cpuinfo.get_cpu_info()['brand_raw']
print('Modelo Processador: {}'.format(mod_cpu))

# disco em bytes convertido em Gb
hd = psutil.disk_usage("c:\\")[0]
hd = int(hd / 1024 / 1024 / 1024)
print(('Tamanho HD (Mb): {}'.format(hd)))

#mostra a % livre dos discos - nao preciso
# conn = wmi.WMI()
# for disk in conn.Win32_LogicalDisk():
#     if disk.size != None:
#         print(disk.Caption, "is {0:.2f}% free".format(
#             100 * float(disk.FreeSpace) / float(disk.Size))
#               )

# end ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
print('End. IP: {}'.format(ip))

# Usuário Logado
user = os.getlogin()
print('Usuário: {}'.format(user))

#fim
print(' ')
print('Fim do Levantamento.')

# fontes consultadas
# https://docs.python.org/3/library/platform.html
# https://acervolima.com/obtenha-as-informacoes-do-seu-sistema-usando-o-script-python/
# https://stackoverflow.com/questions/4842448/getting-processor-information-in-python
# https://psutil.readthedocs.io/en/latest/
# https://www.delftstack.com/pt/howto/python/get-ip-address-python/
# https://qastack.com.br/programming/842059/is-there-a-portable-way-to-get-the-current-username-in-python

