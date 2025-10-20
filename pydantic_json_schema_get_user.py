from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
# Вместо CreateUserRequestDict импортируем CreateUserRequestSchema
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()

# Вместо CreateUserRequestDict используем CreateUserRequestSchema
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",  # Передаем аргументы в формате snake_case вместо camelCase
    first_name="string",  # Передаем аргументы в формате snake_case вместо camelCase
    middle_name="string"  # Передаем аргументы в формате snake_case вместо camelCase
)
create_user_response = public_users_client.create_user(create_user_request)

# Используем атрибуты вместо ключей
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

# Используем атрибуты вместо ключей
get_user_response = private_users_client.get_user(create_user_response.user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(instance=get_user_response, schema=get_user_response_schema)