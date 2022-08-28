```plantuml
@startuml

!theme plain
top to bottom direction
skinparam linetype ortho

class auth_group {
   name: varchar(150)
   id: integer
}
class auth_group_permissions {
   group_id: integer
   permission_id: integer
   id: integer
}
class auth_permission {
   content_type_id: integer
   codename: varchar(100)
   name: varchar(255)
   id: integer
}
class auth_user {
   password: varchar(128)
   last_login: datetime
   is_superuser: bool
   username: varchar(150)
   last_name: varchar(150)
   email: varchar(254)
   is_staff: bool
   is_active: bool
   date_joined: datetime
   first_name: varchar(150)
   id: integer
}
class auth_user_groups {
   user_id: integer
   group_id: integer
   id: integer
}
class auth_user_user_permissions {
   user_id: integer
   permission_id: integer
   id: integer
}
class blog_category {
   name: varchar(64)
   id: integer
}
class blog_comments {
   create_date: datetime
   text: text
   author_id: integer
   post_id: bigint
   status: bool
   id: integer
}
class blog_post {
   title: varchar(200)
   text: text
   created_date: datetime
   published_date: datetime
   author_id: integer
   id: integer
}
class blog_post_category {
   post_id: bigint
   category_id: bigint
   id: integer
}
class django_admin_log {
   action_time: datetime
   object_id: text
   object_repr: varchar(200)
   change_message: text
   content_type_id: integer
   user_id: integer
   action_flag: smallint unsigned
   id: integer
}
class django_content_type {
   app_label: varchar(100)
   model: varchar(100)
   id: integer
}
class django_migrations {
   app: varchar(255)
   name: varchar(255)
   applied: datetime
   id: integer
}
class django_session {
   session_data: text
   expire_date: datetime
   session_key: varchar(40)
}
class sqlite_master {
   type: text
   name: text
   tbl_name: text
   rootpage: int
   sql: text
}
class sqlite_sequence {
   name: unknown
   seq: unknown
}

auth_group_permissions      -[#595959,plain]-^  auth_group                 : "group_id:id"
auth_group_permissions      -[#595959,plain]-^  auth_permission            : "permission_id:id"
auth_permission             -[#595959,plain]-^  django_content_type        : "content_type_id:id"
auth_user_groups            -[#595959,plain]-^  auth_group                 : "group_id:id"
auth_user_groups            -[#595959,plain]-^  auth_user                  : "user_id:id"
auth_user_user_permissions  -[#595959,plain]-^  auth_permission            : "permission_id:id"
auth_user_user_permissions  -[#595959,plain]-^  auth_user                  : "user_id:id"
blog_comments               -[#595959,plain]-^  auth_user                  : "author_id:id"
blog_comments               -[#595959,plain]-^  blog_post                  : "post_id:id"
blog_post                   -[#595959,plain]-^  auth_user                  : "author_id:id"
blog_post_category          -[#595959,plain]-^  blog_category              : "category_id:id"
blog_post_category          -[#595959,plain]-^  blog_post                  : "post_id:id"
django_admin_log            -[#595959,plain]-^  auth_user                  : "user_id:id"
django_admin_log            -[#595959,plain]-^  django_content_type        : "content_type_id:id"
@enduml

```

'''
Блог с категориями: Спотрсменки, Актрисы, Певицы.
Категории добавлять к постам через админку.
С регистрацией и авторизацией.
Добавление, удаление, редактирование постов.
Добавление комментариев.
Частично подключен bootstrap 4.
Написан на фреймворке Django.
Запуск: python3 manage.py runserver
'''
