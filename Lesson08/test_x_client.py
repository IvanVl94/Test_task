#import requests
#from CompanyApi import CompanyApi
#http://5.101.50.27:8000/docs#/   https://x-clients-be.onrender.com

#api = CompanyApi("https://x-clients-be.onrender.com")

#def test_get_companies():
    #body = api.get_company_list()
    #assert len(body) > 0
    
#def test_get_active_companies():
    # Получить список всех компаний
    #full_list = api.get_company_list()

    # Получить список активных компаний
    
    #filtered_list = api.get_company_list(params_tu_add={'active' : 'true'})

    # Проверить, что список 1 > списка 2
    #assert len(full_list) > len(filtered_list)
    

#def test_add_new(): 
    #получитьс список компаний
    #body = api.get_company_list()
    #len_before = len(body)

    #создать новую компанию
    #name = "Avtotest"
    #descr = "Descr"
    #result = api.cread_company(name, descr)
    #new_id = result["id"]

    #получить количество компаний
    #body = api.get_company_list()
    #len_after = len(body)

    
    #Проверить, что +1
    
    #assert len_after - len_before == 0 # не работает сайт
    
    #Проверить , что ид компании равен ответу из шага 2
    
    #assert body[-1]["name"] == name
    #assert body[-1]["description"] == descr
    #assert body[-1]["id"] == new_id
    #Получение конкретной компании
#def test_get_one_company():
    # создать компанию
    #name = "VC Code"
    #descr = "IDE"
    #result = api.cread_company(name, descr)
    #new_id = result["id"]
    
    # получить компанию
    
    #new_company = api.get_company(new_id)
    
    #assert new_company["id"] == new_id
    #assert new_company["name"] == name
    #assert new_company["description"] == descr
    #assert new_company["isActive"] == True
    
    #Редактирование компании
#def test_edit():
    #Создаем организацию
    #name = "Company tu bi"
    #descr = "Edit me"
    #result = api.cread_company(name, descr)
    #new_id = result["id"]
    
    # Редактируем
    
    #new_name = "UPDEATED"
    #new_descr = "Edit"
    #editet = api.edit(new_id, new_name, new_descr )
    #Проверяем
    #assert editet["id"] == new_id
    #assert editet["name"] == name
    #assert editet["description"] == descr
    #assert editet["isActive"] == True
    
    #Удаление
    
#def test_delete():
    #Создаем организацию
  #  name = "Company tu bi delete"
   
  #  result = api.cread_company(name)
  #  new_id = result["id"]
    
   # editet = api.delete(new_id )
    #Проверяем
  #  assert editet["id"] == new_id
  #  assert editet["name"] == name
  #  assert editet["description"] ==""
  #  assert editet["isActive"] == True
    #Проверяем количество компаний после удаления
  #  body = api.get_company_list()
   # assert body[-1]["id"] != new_id
    #Деактивируем компанию 
#def test_deactivate():
  #  name = "Company tu bi deactivate"
  #  result = api.cread_company(name)
  #  new_id = result["id"]
    
  #  body = api.set_active_state(new_id, False)
   # assert body["isActive"] == False 
     
     #Снова активировать
#def test_deactivate_and_activete_company():
  #  name = "Company tu bi deactivate"
  #  result = api.cread_company(name)
  #  new_id = result["id"]
    
    #api.set_active_state(new_id, False)
    
   # body = api.set_active_state(new_id, True)
    #assert body["isActive"] == True