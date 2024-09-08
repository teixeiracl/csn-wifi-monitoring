const systemtypeDb = require('../db/db');

class SystemTypeDAO {
    async createSystemtype(description: any){
        const [id] = await systemtypeDb('systemtype').insert({
            description
        })
        .returning('idsystemtype');

        return id;
    }

}

module.exports = new SystemTypeDAO();