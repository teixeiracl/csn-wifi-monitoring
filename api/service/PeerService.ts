const peerDAO = require('../dao/PeerDao');

class PeerService {
    createPeer(peerDto: { 
        timestamp: string,
        latitude: number,
        longitude: number,
        altitude: number,
        speed: number,
        macsource: string,
        macdestination: string,
        action: number,
        enabled: number,
        cost: number,
        rate: number,
        rssi: number,
        signal_ok: number,
        age: number,
        stats: number,
        encapId: number,
        ipv4Address: string,
        ip: string,
        txpower: number,
        version: number,
        linkLocalAddress: string;
        
         }){
        const {
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
        } = peerDto;
        return peerDAO.createPeer(
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
        linkLocalAddress,);
    }
}

module.exports = new PeerService();