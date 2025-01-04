import hvac
from decouple import config
from api_evaluations import GetEvaluations as api_old
from get_evaluations import GetEvaluations as api_new
from api_evaluations import DataProcessing as dp_old
from data_processing import DataProcessing as dp_new


old_api = api_old()
new_api = api_new()
old_dp = dp_old()
new_dp = dp_new()


vault_addr = config('VAULT_ADDR')
vault_user = config('VAULT_USER')
vault_pwd = config('VAULT_PWD')
username = 'sodexo1716126165'
# username = 'estapar1716125789'
vault_mount_point = 'analytics_secrets'
vault_api_clients = 'api_clients'
survey_id = '44668'
# survey_id = '25133'


# Connection to vault
client = hvac.Client(url=vault_addr)
_ = client.auth.userpass.login(
    username=vault_user,
    password=vault_pwd,
)['auth']['client_token']

response = client.secrets.kv.v2.read_secret_version(
    mount_point=vault_mount_point,
    path=vault_api_clients,
    raise_on_deleted_version=True,
)['data']['data']

# Get creds from vault
api_password = response[username]


evaluations_old = old_api.get_evaluations(
    username,
    api_password,
    survey_id,
    start_datetime='2024-12-01T00:00:00',
    end_datetime='2024-12-03T23:59:59',
)


type(evaluations_old)
evaluations_old
evaluations_old.shape
evaluations_old.columns.tolist()
df_old = old_dp.data_processing(evaluations_old)
df_old.shape
df_old.columns.tolist()


evaluations_new = new_api.get_evaluations(
    username,
    api_password,
    survey_id,
    start_datetime='2024-12-01T00:00:00',
    end_datetime='2024-12-03T23:59:59',
)


type(evaluations_new)
evaluations_new
evaluations_new.shape
evaluations_new.columns.tolist()
df_new = new_dp.process_data(evaluations_new)
df_new.shape
df_new.columns.tolist()
