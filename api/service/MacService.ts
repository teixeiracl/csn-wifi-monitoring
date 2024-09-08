const macDAO = require('../dao/MacDao');

class MacService {
    createMac(macDto: { 
        macaddress: any,
        idsystemfk: any,
        interface_: any;
         }){
        const {
            macaddress,
            idsystemfk,
            interface_,
        } = macDto;
        return macDAO.createMac(
            macaddress,
            idsystemfk,
            interface_,);
    }
}

module.exports = new MacService();