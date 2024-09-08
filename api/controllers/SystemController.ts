import { Request, Response } from 'express';
const systemService = require('../service/SystemService');
const knex = require('../db/db');

class SystemController {
    async createSystem(request: Request, response: Response) {
        try {
            const systemid = await systemService.createSystem(request.body);
            response.status(201).json(systemid);
        } catch (err) {
            console.error(err);
        }
    }

    async show(request: Request, response: Response) {
        const { id } = request.body;
        let system = undefined;

        if (id) {
            system = await knex('system').where('idsystem', id).first();
        }
        else {
            system = await knex('system').select('*');
        }

        if (!system) {
            return response.status(400).json({ message: 'system not found.' });
        }

        return response.json(system);
    }

    async update(request: Request, response: Response) {
        const { id } = request.params;
        const body = request.body;
        try {
            const system = await knex('system').where('idsystem', id).update(body);
            if (!system) {
                return response.status(400).json({ message: 'system not updated.' });
            }
            return response.json(system);
        } catch (err) {
            console.error(err);
        }
    }

    async delete(request: Request, response: Response) {
        const { id } = request.params;

        const system = await knex('system').where('idsystem', id).del();

        if (!system) {
            return response.status(400).json({ message: 'system not found.' });
        }

        return response.json({ message: 'system deletado' });
    }

}

module.exports = new SystemController();