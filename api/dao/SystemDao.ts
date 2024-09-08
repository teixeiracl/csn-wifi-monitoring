const systemDb = require('../db/db');

class SystemDAO {
    async createSystem(
        description: any,
        platform: any,
        uptime: any,
        idle: any,
        running: any,
        bridgeup: any,
        version: any,
        freeMemory: any,
        generateEntropy: any,
        factoryMode: any,
        networkId: any,
        ipv4address: any,
        subnet: any,
        gateway: any,
        dns: any,
        ipv6address: any,
        encapId: any,
        locked: any,
        reboot: any,
        legacyPlatform: any,
        temperature: any,
        isRebooting: any,
        bootCounter: any,
        idsystemtype_fk: any,
        idequipament_fk: any,
        ){
        const [id] = await systemDb('system').insert({
            description,
            platform,
            uptime,
            idle,
            running,
            bridgeup,
            version,
            freeMemory,
            generateEntropy,
            factoryMode,
            networkId,
            ipv4address,
            subnet,
            gateway,
            dns,
            ipv6address,
            encapId,
            locked,
            reboot,
            legacyPlatform,
            temperature,
            isRebooting,
            bootCounter,
            idsystemtype_fk,
            idequipament_fk,
        })
        .returning('idsystem');

        return id;
    }
}

module.exports = new SystemDAO();