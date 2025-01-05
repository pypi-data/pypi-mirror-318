from cianparser import *             ## необходимые модули для работы 
import time
import asyncio
import datetime
import os


class Parser():                      ## синхронная версия
    def init_folder(func):           ## инициализация папки с отчетами
        def craken(*args, **kwargs):
            if not os.path.isdir("reports"):
                print('папка reports не была найдена или отсутсвует')
                os.mkdir("reports")
                print('папка reports была создана')
            first_path = os.getcwd()
            os.chdir(r'reports')
            return_value = func(*args, **kwargs)
            os.chdir('..')
            os.chdir(first_path)
            return(return_value)
        return(craken)


    def help():                      ## функция поиощи по работе с библиотекой
        print('\n n - количество страниц(по умолчанию = 2), k - список городов, с - название определенного города',
              '\n функция get_info (n,k) - собирает информацию по всем типам недвижимости в переданных городах',
              '\n функция get_one_info (n,c) - собирает информацию по 1 городу',
              '\n функция get_async_one_information (n,c) - асинхронная версия функции get_one_info (n,c)  '
              '\n фукция get_async_information(n,k) - асинхронная версия функции get_info (n,k)',
              '\n пример запуска ассинхронной функции : asyncio.run(Parser.AsyncParser.get_async_one_information(count_pages=2,city="москва"))')
        

    @init_folder
    def get_info(count_page=None,citys_name = list,):  ## поиск информации по списку городов
        if count_page == None:
            count_page = 2
        data_homes = []
        data_sub = []
        print('начат поиск информации по городам')
        for city in citys_name:
            print('начат поиск информации по городу ' + city)
            sub_type = ["house", "house-part", "land-plot", "townhouse"]
            parser = cianparser.CianParser(location=str(city))
            data_homes_var = parser.get_flats(deal_type="sale", rooms=(1, 2), with_saving_csv=True, additional_settings={"start_page":1, "end_page":count_page})
            time.sleep(2)
            data_homes.append(data_homes_var)
            for type in sub_type:
                data_sub_var = parser.get_suburban(suburban_type=type, deal_type="sale", additional_settings={"start_page":1, "end_page":count_page})
                time.sleep(2)
                data_sub.append(data_sub_var)
        data ={'public_homes' :['информация по городским объектам', data_homes],
                 'private_homes' : ['информация по объектам частной территории', data_sub]}
        print('поиск информации по городам завершен')
        return(data)
    
    
    @init_folder
    def get_one_info(count_page=None,city_name = str):  ## поиск информации по 1 городу
        if count_page ==None:
            count_page = 2
        data_homes = []
        data_sub = []
        sub_type = ["house", "house-part", "land-plot", "townhouse"]
        print('начат поиск информации по городу')
        parser = cianparser.CianParser(location=city_name)
        data_homes_var = parser.get_flats(deal_type="sale", rooms=(1, 2), with_saving_csv=True, additional_settings={"start_page":1, "end_page":count_page})
        time.sleep(2)
        data_homes.append(data_homes_var)
        for type in sub_type:
            data_sub_var = parser.get_suburban(suburban_type=type, deal_type="sale", additional_settings={"start_page":1, "end_page":count_page})
            time.sleep(2)
            data_sub.append(data_sub_var)
                
        data ={'public_homes' :['информация по городским объектам', data_homes],
                 'private_homes' : ['информация по объектам частной территории', data_sub]}
        print('поиск информации завершен')
        return(data)
    



    class AsyncParser():             ## асинхронная версия
        
        def init_async_folder(func):
            async def craken(*args, **kwargs):
                if not os.path.isdir("reports"):
                    os.mkdir("reports")
                first_path = os.getcwd()
                os.chdir(r'reports')
                return_value = await func(*args, **kwargs)
                os.chdir('..')
                os.chdir(first_path)
                return(return_value)
            return(craken)
        
        
        async def get_async_one_info(city_name = str,count_pages=None):
            if count_pages == None:
                count_pages = 2
            data_homes = []
            data_sub = []
            sub_type = ["house", "house-part", "land-plot", "townhouse"]
            parser = cianparser.CianParser(location=str(city_name))
            data_homes_var =  parser.get_flats(deal_type="sale", rooms=(1, 2), with_saving_csv=True, additional_settings={"start_page":1, "end_page":int(count_pages)})
            asyncio.sleep(2)
            data_homes.append(data_homes_var)
            for type in sub_type:
                data_sub_var =  parser.get_suburban(suburban_type=type, deal_type="sale", additional_settings={"start_page":1, "end_page":int(count_pages)})
                asyncio.sleep(2)
                data_sub.append(data_sub_var)
            data ={'public_homes' :['информация по городским объектам', data_homes],
                 'private_homes' : ['информация по объектам частной территории', data_sub]}
            return(data)
        

        @init_async_folder
        async def get_async_one_information(count_pages=None,city=str):  ## поиск информации по 1 городу (асинхронно)
            print('начат поиск информации')
            task = asyncio.create_task(Parser.AsyncParser.get_async_one_info(city,count_pages))
            await task
            return(task)
        

        async def get_async_info(city=str,count_pages=None,):
            data_homes = []
            data_sub = []
            sub_type = ["house", "house-part", "land-plot", "townhouse"]
            parser = cianparser.CianParser(location=str(city))
            data_homes_var = parser.get_flats(deal_type="sale", rooms=(1, 2), with_saving_csv=True, additional_settings={"start_page":1, "end_page":count_pages})
            asyncio.sleep(2)
            data_homes.append(data_homes_var)
            for type in sub_type:
                data_sub_var = parser.get_suburban(suburban_type=type, deal_type="sale", additional_settings={"start_page":1, "end_page":count_pages})
                asyncio.sleep(2)
                data_sub.append(data_sub_var)
            data ={'public_homes' :['информация по городским объектам', data_homes],
                     'private_homes' : ['информация по объектам частной территории', data_sub]}
            return(data)
        
 
        @init_async_folder  
        async def get_async_information(citys,count_pages=None):  ## поиск информации по списку городов (асинхронно)
            if count_pages== None:
                count_pages =2 
            tasks = []
            for city in citys:
                print('начат поиск информации по городу ' + city)
                tasks.append(asyncio.create_task(Parser.AsyncParser.get_async_one_info(city,count_pages)))           
            for task in tasks :
                await task
            return(task)
        


if __name__ == '__main__' :                  ##тестирование времени работы программы
    st = ['москва','казань','пермь']
    tt = 'омск'
    start = datetime.datetime.now()
    #info = asyncio.run(Parser.AsyncParser.get_async_one_information(city='москва'))
    info = Parser.get_info(citys_name=st)
    finish = datetime.datetime.now()


    print(info)

    print('Время работы: ' + str(finish - start))

