from Service.task_service import Task_Service
from Service.user_service import User_Services


def main():
    task_service = Task_Service()
    user_service = User_Services()

    user_service.add_user(123,'Ajay',"ajaykumarjagu155@gmail.com")

    task_service.create_task(1,"Tech Data Science","Teach from scratch")
    task_service.create_task(2,"Python","Teach from scratch")
    task_service.create_task(3,"AI","teach from the scratch")

    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())


    history= task_service.get_task_history()
    for i in range(history.is_empty()):
        print(history.pop().title)

if __name__=="__main__":
    main()
