const peerDb = require('../db/db');

class PeerDAO {
    async createPeer(
        timestamp: any,
        latitude: any,
        longitude: any,
        altitude: any,
        speed: any,
        macsource: any,
        macdestination: any,
        action: any,
        enabled: any,
        cost: any,
        rate: any,
        rssi: any,
        signal_ok: any,
        age: any,
        stats: any,
        encapId: any,
        ipv4Address: any,
        ip: any,
        txpower: any,
        version: any,
        linkLocalAddress: any,
        ){
        const [id] = await peerDb('peer').insert({
        timestamp,
        latitude,
        longitude,
        altitude,
        speed,
        macsource,
        macdestination,
        action,
        enabled,
        cost,
        rate,
        rssi,
        signal_ok,
        age,
        stats,
        encapId,
        ipv4Address,
        ip,
        txpower,
        version,
        linkLocalAddress,
        })
        .returning('idpeer');

        return id;
    }
}

module.exports = new PeerDAO();