import { Knex } from "knex";


export async function up(knex: Knex): Promise<void> {
    return knex.schema.createTable('systemtype', table => {
        table.increments('idsystemtype').primary();
        table.string('description');
    });
}


export async function down(knex: Knex): Promise<void> {
    return knex.schema.dropTable('systemtype');
}

