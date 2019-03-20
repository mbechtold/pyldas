import sys
sys.path.append(r'/data/leuven/317/vsc31786/miniconda/bin/')

from pyldas.interface import LDAS_io

exp='SMAP_EASEv2_M36_NORTH_SCA_SMOSrw_DA'
domain='SMAP_EASEv2_M36_NORTH'

exp='SMAPL4v3_M09_PM'
domain='SMAP_EASEv2_M09'

exp='BE_M36_EASEv2_SMAPin_L4SM_v001'
domain='SMAP_EASEv2_M36_GLOBAL'

exp='SMAP_EASEv2_M09_SI_SMOSfw_DA'
domain='SMAP_EASEv2_M09'

io = LDAS_io('ObsFcstAna', exp, domain)
io.bin2netcdf()

#io = LDAS_io('xhourly', exp, domain)
#io.bin2netcdf()

#io = LDAS_io('xhourly', exp, domain)
#io.bin2netcdf()

#io = LDAS_io('incr', exp, domain)
#io.bin2netcdf()

#io = LDAS_io('ensstd', exp, domain)
#io.bin2netcdf()
