#MAIN

import Models
import SV


_entity = Models.ModelBook('C#','.netCore',5)

_sv = SV._svBook()
_sv.Insert(_entity)
