import express from 'express';
const systemTypeController = require('../controllers/SystemTypeController');
const SystemController = require('../controllers/SystemController');
const PeerController = require('../controllers/PeerController');
const equipmentController = require('../controllers/EquipamentController');

const router = express.Router();

// Middleware para todas as rotas, adicionando "/mapeamento" à URL
router.use('/mapeamento', (req, res, next) => {
    next(); // Passe para a próxima etapa de roteamento
});

// Função para criar rotas usando a URL completa (incluindo "/mapeamento")
const createMappedRoute = (route: any) => {
    return `/mapeamento${route}`;
};

router.post(createMappedRoute('/systemtype'), systemTypeController.createSystemtype);
router.post(createMappedRoute('/systemtype/id/'), systemTypeController.show);
router.post(createMappedRoute('/systemtype/description/'), systemTypeController.showdescription);
router.put(createMappedRoute('/systemtype/:id'), systemTypeController.update);
router.delete(createMappedRoute('/systemtype/:id'), systemTypeController.delete);

router.post(createMappedRoute('/equipment'), equipmentController.createEquipament);
router.put(createMappedRoute('/equipment/:id'), equipmentController.update);
router.post(createMappedRoute('/equipment/id/'), equipmentController.show);
router.delete(createMappedRoute('/equipment/:id'), equipmentController.delete);

router.post(createMappedRoute('/system'), SystemController.createSystem);
router.post(createMappedRoute('/system/id'), SystemController.show);
router.put(createMappedRoute('/system/:id'), SystemController.update);
router.delete(createMappedRoute('/system/:id'), SystemController.delete);

router.post(createMappedRoute('/peer'), PeerController.createPeer);
router.post(createMappedRoute('/buscar-peers'), PeerController.show);
router.post(createMappedRoute('/rssi-peers'), PeerController.getPeersForRssi);
router.put(createMappedRoute('/peer/:id'), PeerController.update);
router.delete(createMappedRoute('/peer/:id'), PeerController.delete);

module.exports = router;
