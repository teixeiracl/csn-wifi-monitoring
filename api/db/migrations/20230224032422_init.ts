import { Knex } from "knex";


export async function up(knex: Knex): Promise<void> {
    return knex.schema.createTable('peer', table => {
        table.increments('idpeer').primary();
        table.datetime('timestamp');
        table.double('latitude');
        table.double('longitude');
        table.double('altitude');
        table.double('speed');
        table.string('macsource')
        table.string('macdestination')
        table.integer('action');
        table.tinyint('enabled');
        table.integer('cost');
        table.integer('rate');
        table.integer('rssi');
        table.integer('signal_ok');
        table.integer('age');
        table.integer('stats');
        table.integer('encapId');
        table.string('ipv4Address');
        table.string('ip');
        table.integer('txpower');
        table.integer('version');
        table.string('linkLocalAddress');
    });
}


export async function down(knex: Knex): Promise<void> {
    return knex.schema.dropTable('peer');
}
