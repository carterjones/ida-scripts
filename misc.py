import idaapi
from idautils import *
from idc import *

# Gets the address of the first instruction of each basic block within a
# function.
# Note:
#  - The function used is the one in which 'address' resides.
#  - If no address is supplied, the currently selected address is used.
def get_function_basic_blocks(address=None):
  if address is None:
    address = idc.here()
  f = idaapi.FlowChart(idaapi.get_func(address))
  fl = []
  for block in f:
    fl += [block.startEA]
  return fl

# Add a breakpoint to the first instruction of each basic block within a
# function.
# Note:
#  - The function used is the one in which 'address' resides.
#  - If no address is supplied, the currently selected address is used.
def add_bpt_all_function_basic_blocks(address=None):
  if address is None:
    address = idc.here()
  blocks = get_function_basic_blocks(address)
  for block in blocks:
    AddBpt(block)

# Remove any breakpoints from the first instruction of each basic block
# within a function.
# Note:
#  - The function used is the one in which 'address' resides.
#  - If no address is supplied, the currently selected address is used.
def del_bpt_all_function_basic_blocks(address=None):
  if address is None:
    address = idc.here()
  blocks = get_function_basic_blocks(address)
  for block in blocks:
    DelBpt(block)
