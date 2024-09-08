import { Knex } from "knex";


export async function up(knex: Knex): Promise<void> {
    return knex.schema.createTable('system', table => {
        table.increments('idsystem').primary();
        table.string('description');
        table.string('platform');
        table.double('uptime');
        table.double('idle');
        table.tinyint('running');
        table.tinyint('bridgeup');
        table.string('version');
        table.integer('freeMemory');
        table.tinyint('generateEntropy');
        table.tinyint('factoryMode');
        table.integer('networkId');
        table.string('ipv4address').primary();;
        table.string('subnet');
        table.string('gateway');
        table.string('dns');
        table.string('ipv6address');
        table.integer('encapId');
        table.tinyint('locked');
        table.tinyint('reboot');
        table.string('legacyPlatform');
        table.integer('temperature');
        table.tinyint('isRebooting');
        table.integer('bootCounter');
        table.bigint('idsystemtype_fk').references('idsystemtype').inTable('systemtype');
        table.bigint('idequipament_fk').references('idequipament').inTable('equipament');
    });
}


export async function down(knex: Knex): Promise<void> {
    return knex.schema.dropTable('system');
}
