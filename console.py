import pdb

from models.visit import Visit
from models.system import System
from models.planet import Planet

import repositories.visit_repository as visit_repository
import repositories.system_repository as system_repository
import repositories.planet_repository as planet_repository

# visit_repository.delete_all()
# system_repository.delete_all()

# pdb.set_trace()

system_1 = System("The end of time and matter")
system_repository.save(system_1)

system_2 = System("Solar System")
system_repository.save(system_2)

planet_1 = Planet("Earth", system_2)
planet_2 = Planet("Milliways", system_1)
planet_repository.save(planet_1)
planet_repository.save(planet_2)

system_repository.select_all()

selected_system = system_repository.select(1)

visit_1 = Visit("Watch the universe end alongside a slap up meal.", system_1, planet_2)
visit_repository.save(visit_1)

visit_2 = Visit("Have a pint or four at The Red Lion before the earth is destroyed to make way for hyperspace-bypass ", system_2, planet_1)
visit_repository.save(visit_2)

planet_repository.select_all()

planet_repository.select(1)






# visit_repository.delete(1)
# system_repository.delete(1)

# visit_repository.update(visit_2)
# system_repository.update(system_2)

