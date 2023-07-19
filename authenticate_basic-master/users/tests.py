from django.test import TestCase

task_id = 1
username = "bob"
name = "zadanie"
def children(request):
    user = "пользователь"
    if request>0 : #проверяем, что метод пост
        form = request
        task = []
        if form>2:#проверям valid - на ли форма
            task.append(task_id)
            task.append(username)
            task.append(name)
            #task.save() сохраняем изменения
            return "открыто задание для детей"
    else:
        form = request
    return "вернуть к регистрации"
print(children(0))
