import { Request, Response } from 'express';
const systemTypeService = require('../service/SystemTypeService');
const knex = require('../db/db');

class SystemTypeController {
    async createSystemtype(request: Request, response: Response) {
        try {
            const systemtypeid = await systemTypeService.createSystemtype(request.body);
            response.status(201).json(systemtypeid);
        } catch (err) {
            console.error(err);
        }
    }

    async update(request: Request, response: Response) {
        const { id } = request.params;
        const body = request.body;
        try {
            const newSystemType = await knex('systemtype').where('idsystemtype', id).update(body);
            if (!newSystemType) {
                return response.status(400).json({ message: 'systemtype not updated.' });
            }
            return response.json(newSystemType);
        } catch (err) {
            console.error(err);
        }
    }

    async show(request: Request, response: Response) {
        const { id } = request.body;

        let systemtype = undefined;

        if (id) {
            systemtype = await knex('systemtype').where('idsystemtype', id).first();
        }

        else {
            systemtype = await knex('systemtype').select('*');
        }

        if (!systemtype) {
            return response.status(400).json({ message: 'systemtype not found.' });
        }

        return response.json(systemtype);
    }

    async showdescription(request: Request, response: Response) {
        const { description } = request.body;

        const systemtype = await knex('systemtype').where('description', description).first();

        if (!systemtype) {
            return response.status(400).json({ message: 'systemtype not found.' });
        }

        return response.json(systemtype);
    }

    async delete(request: Request, response: Response) {
        const { id } = request.params;

        const systemtype = await knex('systemtype').where('idsystemtype', id).del();

        if (!systemtype) {
            return response.status(400).json({ message: 'systemtype not found.' });
        }

        return response.json({ message: 'systemtype deletado' });
    }

}

module.exports = new SystemTypeController();