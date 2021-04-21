from pysnmp.hlapi import *

snmp_object = ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)
snmp_object2 = ObjectIdentity("1.3.6.1.2.1.2.2.1.2")
result = getCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.107", 161)),
                ContextData(),
                ObjectType(snmp_object))
result2 = nextCmd (SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.107", 161)),
                ContextData(),
                ObjectType(snmp_object2), lexicographicMode=False)

for i in result:
    result_list=list(i)
    result_list_field=result_list[3]
    print(result_list_field[0])

print()

for i in result2:
    result2_list_varBinds=list(i)
    result2_list_varBinds_fild=result2_list_varBinds[3]
    print(result2_list_varBinds_fild[0])