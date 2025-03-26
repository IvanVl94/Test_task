# Пользователи Windows: запустите в терминале VS Code команду

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
Затем команду:
scoop install allure
 > Теперь терминал распознает команду - allure
Введите команду ниже — сгенерируется отчет о тестах:
 > allure serve allure-results
Отчет откроется на локальном сервере в окне вашего браузера.
Overview — раздел с общей информацией: сколько всего тестов запустили, процент успешных тестов, доля успешных и неуспешных тестов.
# Allure умеет генерировать отчет в файл — его можно выгружать. Для этого используется команда:
 > allure generate название папки (allure-result)
В файле index.html хранится результат отчета. Его можно запустить вручную — он откроется в окне браузера. А еще результаты в index.html можно запускать с помощью команды:
 > allure open allure-report
Если вы отправите папку allure-report коллеге, то он сможет открывать этой командой результаты у себя на компьютере.
