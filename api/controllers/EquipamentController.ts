import { Request, Response } from 'express';
const knex = require('../db/db');

class EquipamentController {
    async createEquipament(request: Request, response: Response) {
        try {
            const { equipament,  description, sigla } = request.body;

            const [equipamentId] = await knex('equipament')
                .insert({ equipament, description, sigla })
                .returning('idequipament');

            response.status(201).json(equipamentId);
        } catch (err) {
            console.error(err);
            response.status(500).json({ message: 'Internal Server Error' });
        }
    }

    async update(request: Request, response: Response) {
        const { id } = request.params;
        const body = request.body;
        try {
            const updatedEquipament = await knex('equipament')
                .where('idequipament', id)
                .update(body);
            if (!updatedEquipament) {
                return response.status(400).json({ message: 'Equipament not updated.' });
            }
            return response.json(updatedEquipament);
        } catch (err) {
            console.error(err);
            response.status(500).json({ message: 'Internal Server Error' });
        }
    }

    async show(request: Request, response: Response) {
        const { id } = request.body;

        let equipament = undefined;

        if (id) {
            equipament = await knex('equipament').where('idequipament', id).first()
        } else {
            equipament = await knex('equipament').select('*');
        }

        if (!equipament) {
            return response.status(400).json({ message: 'Equipament not found.' });
        }

        return response.json(equipament);
    }

    async delete(request: Request, response: Response) {
        const { id } = request.params;

        try {
            const deletedEquipament = await knex('equipament').where('idequipament', id).del();
            if (!deletedEquipament) {
                return response.status(400).json({ message: 'Equipament not found.' });
            }
            return response.json({ message: 'Equipament deleted' });
        } catch (err) {
            console.error(err);
            response.status(500).json({ message: 'Internal Server Error' });
        }
    }
}

module.exports = new EquipamentController();
