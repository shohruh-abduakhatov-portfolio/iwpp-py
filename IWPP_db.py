from modules.kinetic_core.Connector import db


async def warehouse_distances_put(data):
    return (await db.query(
        'INSERT INTO warehouse_distances(x1, y1, x2, y2, warehouses_fk)'
        'VALUES ($1, $2, $3, $4, $5)'
        'returning distance_id, current_timestamp',
        (data['x1'], data['y1'], data['x2'], data['y2'], data['warehouses_fk'])
    ))


async def warehouse_distances_get_by_id(data):
    return (await db.query(
        'select * from warehouse_distances where distance_id=$1',
        (data['distance_id'])
    ))


# get by xy points
async def warehouse_distances_get_by_coords(data):
    return (await db.query(
        'select * from warehouse_distances '
        'where x1 == $1, y1 == $2, x2 == $3, y2 == $4',
        (data['x1'], data['y1'], data['x2'], data['y2'])
    ))


# get by warehouse id
async def warehouse_distances_get_by_wh(data):
    return (await db.query(
        'select * from warehouse_distances where warehouses_fk=$1',
        (data['warehouses_fk'])
    ))


async def warehouse_distances_update(data):
    return (await db.query(
        'update warehouse_distances set x1 = $1 and y1 = $2 and x2 = $3 and y2 = $4 '
        'where distance_id = $5'
        'returning current_timestamp',
        (data['x1'], data['y1'], data['x2'], data['y2'], data['distance_id'])
    ))
