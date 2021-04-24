import pdb

from models.visit import Visit
from models.system import System

import repositories.visit_repository as visit_repository
import repositories.system_repository as system_repository

visit_repository.delete_all()
system_repository.delete_all()

system_1 = System("The end of time and matter")
system_repository.save(system_1)

system_2 = System("Betelgeuse")
system_repository.save(system_2)

system_repository.select_all()

selected_system = system_repository.select(1)

visit_1 = Visit("Watch the universe end alongside a slap up meal.", system_1)
visit_repository.save(visit_1)

visit_repository.select_all()

selected_visit = visit_repository.select(1)



