# bot_initializer.py

BOT_NAME = "RPA_FINANCEIRO_01"
MAX_RETRIES = 3
EXECUTION_TIMEOUT = 30.0
IS_PRODUCTION = False

print("=== INICIALIZAÇÃO DO ROBÔ ===")

print("Nome do robô:", BOT_NAME, "| Tipo:", type(BOT_NAME))
print("Máximo de tentativas:", MAX_RETRIES, "| Tipo:", type(MAX_RETRIES))
print("Tempo limite de execução:", EXECUTION_TIMEOUT, "segundos | Tipo:", type(EXECUTION_TIMEOUT))
print("Ambiente de produção:", IS_PRODUCTION, "| Tipo:", type(IS_PRODUCTION))