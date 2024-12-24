import asyncio
import datetime
import aiohttp
from models import Session, SwapiPeople, close_orm, init_orm


async def get_people(person_id: int, session: aiohttp.ClientSession):
    http_response = await session.get(f"https://swapi.py4e.com/api/people/{person_id}/")
    json_data = await http_response.json()
    if 'detail' not in json_data:
        homeworld_response = await session.get(json_data['homeworld'])
        homeworld_json_data = await homeworld_response.json()
        json_data['homeworld'] = homeworld_json_data['name']
        if len(json_data['species']) > 0:
            species_response = await session.get(json_data['species'][0])
            species_json_data = await species_response.json()
            json_data['species'][0] = species_json_data['name']
        for i in range(len(json_data['films'])):
            film_response = await session.get(json_data['films'][i])
            film_json_data = await film_response.json()
            json_data['films'][i] = film_json_data['title']
        if len(json_data['starships']) > 0:
            for j in range(len(json_data['starships'])):
                starships_response = await session.get(json_data['starships'][j])
                starships_json_data = await starships_response.json()
                json_data['starships'][j] = starships_json_data['name']
        if len(json_data['vehicles']) > 0:
            for k in range(len(json_data['vehicles'])):
                starships_response = await session.get(json_data['vehicles'][k])
                starships_json_data = await starships_response.json()
                json_data['vehicles'][k] = starships_json_data['name']
    return json_data


async def insert_results(results: list[dict]):
    async with Session() as session:
        orm_objs = [SwapiPeople(birth_year=swapi_json['birth_year'],
                                eye_color=swapi_json['eye_color'],
                                films=", ".join(swapi_json['films']),
                                gender=swapi_json['gender'],
                                hair_color=swapi_json['hair_color'],
                                height=swapi_json['height'],
                                name=swapi_json['name'],
                                homeworld=swapi_json['homeworld'],
                                mass=swapi_json['mass'],
                                skin_color=swapi_json['skin_color'],
                                species=swapi_json['name'],
                                starships=", ".join(swapi_json['starships']),
                                vehicles=", ".join(swapi_json['vehicles'])
                                ) for swapi_json in results if 'detail' not in swapi_json]
        session.add_all(orm_objs)
        await session.commit()


async def main():
    await init_orm()
    async with aiohttp.ClientSession() as session:
        coros = [get_people(i, session) for i in range(1, 100)]
        results = await asyncio.gather(*coros)
        await insert_results(results)
    await close_orm()


start = datetime.datetime.now()
asyncio.run(main())
print(datetime.datetime.now() - start)
