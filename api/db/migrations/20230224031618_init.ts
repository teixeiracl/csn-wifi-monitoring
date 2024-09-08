import { Knex } from "knex";


export async function up(knex: Knex): Promise<void> {
    return knex.schema.createTable('equipament', table => {
        table.increments('idequipament').primary();
        table.string('equipament');
        table.string('description');
        table.string('sigla');
    });
}


export async function down(knex: Knex): Promise<void> {
    return knex.schema.dropTable('equipament');
}
