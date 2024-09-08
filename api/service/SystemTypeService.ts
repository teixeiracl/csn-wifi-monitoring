const systemTypeDAO = require('../dao/SystemTypeDao');

class SystemTypeService {
    createSystemtype(systemtypeDto: { description: any; }){
        const {description} = systemtypeDto;
        return systemTypeDAO.createSystemtype(description);
    }
}

module.exports = new SystemTypeService();