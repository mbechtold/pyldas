import sys
sys.path.append(r'/data/leuven/317/vsc31786/miniconda/bin/')

from pyldas.interface import LDAS_io

exp='SMAP_EASEv2_M36_NORTH_SCA_SMOSrw_DA'
domain='SMAP_EASEv2_M36_NORTH'

#io = LDAS_io('ObsFcstAna', exp, domain)
#io.bin2netcdf()

io = LDAS_io('xhourly', exp, domain)
io.bin2netcdf()

